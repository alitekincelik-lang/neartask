-- NearTask: admin-editable settings (support email)
-- Run once in Supabase → SQL Editor. Safe to run again. Touches no existing table.

create table if not exists public.app_settings (
  key text primary key,
  value text not null,
  updated_at timestamptz not null default now(),
  updated_by uuid references auth.users(id) on delete set null
);

alter table public.app_settings enable row level security;

drop policy if exists "app_settings public read" on public.app_settings;
create policy "app_settings public read" on public.app_settings
  for select to anon, authenticated using (true);

grant select on public.app_settings to anon, authenticated;

insert into public.app_settings (key, value)
values ('support_email', 'info@artwin.co.uk')
on conflict (key) do nothing;

-- Only accounts with profiles.is_admin = true can change a setting.
create or replace function public.admin_set_setting(k text, v text)
returns void
language plpgsql
security definer
set search_path = public
as $$
begin
  if not exists (select 1 from public.profiles where id = auth.uid() and is_admin) then
    raise exception 'NOT_ADMIN';
  end if;
  if k not in ('support_email') then
    raise exception 'BAD_KEY';
  end if;
  v := lower(trim(v));
  if k = 'support_email' and v !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' then
    raise exception 'BAD_EMAIL';
  end if;
  insert into public.app_settings (key, value, updated_at, updated_by)
  values (k, v, now(), auth.uid())
  on conflict (key) do update
    set value = excluded.value, updated_at = now(), updated_by = auth.uid();
end
$$;

revoke all on function public.admin_set_setting(text, text) from public, anon;
grant execute on function public.admin_set_setting(text, text) to authenticated;
