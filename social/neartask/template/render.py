"""NearTask full-bleed photo template (v2). Usage: python3 render.py
Renders each POST below to out/<slug>.png at 1080x1350."""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
PHOTOS = HERE.parent / "photos"
OUT = HERE / "out"; OUT.mkdir(exist_ok=True)

POSTS = [
    dict(slug='2026-11-21-urgent-shifts', photo='2026-11-21-urgent-shifts.jpg', pos='40% 25%', tag='URGENT SHIFTS', l1='Short notice?', l2='Alert locals.', sub='', credit='Foo Visuals / Unsplash'),
    dict(slug='2026-11-22-get-found', photo='2026-11-22-get-found.jpg', pos='50% 25%', tag='FIND WORK', l1='Looking for work?', l2='Get found.', sub='', credit='Gabriel Arancibia / Unsplash'),
    dict(slug='2026-11-23-kitchen-profile', photo='2026-11-23-kitchen-profile.jpg', pos='30% 20%', tag='KITCHEN WORK', l1='Kitchen work?', l2='Make a profile.', sub='', credit='Sebastian Coman Photography / Unsplash'),
    dict(slug='2026-11-24-cleaning-profile', photo='2026-11-24-cleaning-profile.jpg', pos='60% 25%', tag='CLEANING WORK', l1='Cleaning work?', l2='Get found.', sub='', credit='CDC / Unsplash'),
    dict(slug='2026-11-25-trades', photo='2026-11-25-trades.jpg', pos='50% 30%', tag='PAINTERS & DECORATORS', l1='More local jobs,', l2='no lead fees.', sub='', credit='Roselyn Tirado / Unsplash'),
    dict(slug='2026-11-26-find-work-waiter', photo='2026-11-26-find-work-waiter.jpg', pos='40% 30%', tag='FIND WORK', l1='Looking for', l2='local work?', sub='', credit='Peter Muniz / Unsplash'),
    dict(slug='2026-11-27-trades-electrician', photo='2026-11-27-trades-electrician.jpg', pos='50% 40%', tag='ELECTRICIANS', l1='More local jobs,', l2='no lead fees.', sub='', credit='colsan ltda / Unsplash'),
    dict(slug='2026-11-28-find-work-carer', photo='2026-11-28-find-work-carer.jpg', pos='50% 30%', tag='FIND WORK', l1='Local work,', l2='near you.', sub='', credit='Rodrigo Rodrigues / Unsplash'),
    dict(slug='2026-11-29-trades-gardener', photo='2026-11-29-trades-gardener.jpg', pos='60% 40%', tag='FOR TRADES', l1='More local jobs,', l2='no lead fees.', sub='', credit='Michael Kahn / Unsplash'),
    dict(slug='2026-11-30-find-work-warehouse', photo='2026-11-30-find-work-warehouse.jpg', pos='70% 25%', tag='FIND WORK', l1='Find shifts', l2='near you.', sub='', credit='Kseniia Ilinykh / Unsplash'),
    dict(slug='2026-12-01-trades-plumber', photo='2026-12-01-trades-plumber.jpg', pos='50% 25%', tag='PLUMBERS', l1='More local jobs,', l2='no lead fees.', sub='', credit='Timur Shakerzianov / Unsplash'),
    dict(slug='2026-12-02-trades-flooring', photo='2026-12-02-trades-flooring.jpg', pos='50% 45%', tag='FOR TRADES', l1='More local jobs,', l2='no lead fees.', sub='', credit='Ernys / Unsplash'),
    dict(slug='2026-12-03-trades-removals', photo='2026-12-03-trades-removals.jpg', pos='50% 45%', tag='FOR TRADES', l1='More local jobs,', l2='no lead fees.', sub='', credit='Marvin Alexander Avila / Unsplash'),
    dict(slug='2026-12-04-trades-assembler', photo='2026-12-04-trades-assembler.jpg', pos='50% 35%', tag='FOR TRADES', l1='More local jobs,', l2='no lead fees.', sub='', credit='Alba Calbetó / Unsplash'),
    dict(slug='2026-12-05-looking-for-work-cafe', photo='cafe.jpg', pos='50% 30%', tag='FIND WORK', l1='Looking for', l2='work?', sub='', credit='Ali Aziz / Unsplash'),
    dict(slug='2026-12-06-hire-local-people', photo='2026-12-06-hire-local-people.jpg', pos='50% 30%', tag='HIRING?', l1='Hire local people', l2='for free.', sub='', credit='Brooke Cagle / Unsplash'),
    dict(slug='2026-12-07-grow-your-business-plumber', photo='2026-12-07-grow-your-business-plumber.jpg', pos='50% 35%', tag='FOR TRADES', l1='Grow your business', l2='locally.', sub='', credit='Divaris Shirichena / Unsplash'),
    dict(slug='2026-12-08-find-local-services', photo='garden.jpg', pos='50% 30%', tag='GET LOCAL HELP', l1='Need a hand', l2='at home?', sub='', credit='Lara John / Unsplash'),
    dict(slug='2026-12-09-find-work-hotel-restaurant', photo='2026-12-09-find-work-hotel-restaurant.jpg', pos='40% 40%', tag='FIND WORK', l1='Hotel & restaurant work', l2='near you.', sub='', credit='Ashwini Chaudhary / Unsplash'),
    dict(slug='2026-12-10-looking-for-staff', photo='bakery.jpg', pos='50% 25%', tag='HIRING?', l1='Looking for', l2='staff?', sub='', credit='Dominic Chasse / Unsplash'),
    dict(slug='2026-12-11-find-more-local-customers', photo='2026-12-11-find-more-local-customers.jpg', pos='50% 35%', tag='FOR TRADES', l1='Find more', l2='local customers.', sub='', credit='nikkan Navidi / Unsplash'),
    dict(slug='2026-12-12-connecting-people', photo='2026-12-12-connecting-people.jpg', pos='50% 35%', tag='NEARTASK', l1='Work, jobs and help,', l2='all local.', sub='', credit='Alba Calbetó / Unsplash'),
    dict(slug='2026-12-13-find-work-fast', photo='2026-12-13-find-work-fast.jpg', pos='50% 40%', tag='FIND WORK', l1='Find work', l2='fast.', sub='', credit='John Kakuk / Unsplash'),
    dict(slug='2026-12-14-stop-scrolling', photo='2026-12-14-stop-scrolling.jpg', pos='60% 35%', tag='FIND WORK', l1='Stop scrolling.', l2='Start working.', sub='', credit='Travis Fish / Unsplash'),
]

def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

ICON = ('<svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="512" height="512" rx="112" fill="#fff"/>'
        '<ellipse cx="256" cy="420" rx="120" ry="30" fill="none" stroke="#FFC93C" stroke-width="22"/>'
        '<path d="M256 70c-70 0-126 55-126 124 0 86 99 162 118 177a12 12 0 0 0 16 0c19-15 118-91 118-177 0-69-56-124-126-124z" fill="#0E7C7B"/>'
        '<path d="M193 196l43 43 83-83" fill="none" stroke="#fff" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def fonts():
    css = ""
    for w in (500, 700, 800):
        css += (f"@font-face{{font-family:PJS;font-weight:{w};src:url(data:font/woff2;base64,"
                f"{b64(HERE / f'plus-jakarta-sans-latin-{w}-normal.woff2')}) format('woff2')}}")
    return css

def html(p):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{fonts()}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:PJS;overflow:hidden;background:#0E7C7B}}
.ph{{position:absolute;left:0;right:0;top:0;height:1110px;background:url(data:image/jpeg;base64,{b64(PHOTOS / p['photo'])}) {p['pos']}/cover}}
.panel{{position:absolute;left:0;right:0;top:1110px;bottom:0;background:#0E7C7B}}
.logo{{position:absolute;left:56px;top:52px;display:flex;align-items:center;gap:18px;background:#fff;padding:12px 26px 12px 12px;border-radius:24px;box-shadow:0 6px 20px rgba(0,0,0,.18)}}
.logo svg{{width:72px;height:72px}}
.logo span{{color:#0E7C7B;font-weight:800;font-size:40px;letter-spacing:-.5px}}
.tag{{position:absolute;left:56px;top:1084px;background:#FFC93C;color:#0b2b2b;font-weight:800;font-size:24px;letter-spacing:1.5px;padding:11px 22px;border-radius:999px}}
h1{{position:absolute;left:56px;right:56px;top:1150px;color:#fff;font-weight:800;font-size:64px;line-height:1;letter-spacing:-1.5px;white-space:nowrap}}
h1 em{{font-style:normal;color:#FFC93C}}
.foot{{position:absolute;left:56px;right:56px;bottom:36px;display:flex;justify-content:space-between;align-items:baseline}}
.url{{color:#fff;font-weight:800;font-size:38px;letter-spacing:-.5px}}
.pts{{color:#FFC93C;font-weight:700;font-size:24px}}
.cr{{position:absolute;right:14px;top:1076px;color:#fff;font-size:15px;font-weight:500;text-shadow:0 1px 4px rgba(0,0,0,.6)}}
</style></head><body>
<div class="ph"></div><div class="panel"></div>
<div class="logo">{ICON}<span>NearTask</span></div>
<div class="tag">{p['tag'].replace('&','&amp;')}</div>
<h1 id="h">{p['l1'].replace('&','&amp;')} <em>{p['l2']}</em></h1>
<div class="foot"><div class="url">neartask.co.uk</div><div class="pts">Free · No commission · Anywhere in the UK</div></div>
<div class="cr">Photo: {p['credit']}</div>
<script>const h=document.getElementById('h');let f=64;while(h.scrollWidth>h.clientWidth&&f>40){{f-=2;h.style.fontSize=f+'px'}}</script>
</body></html>"""

with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    only = sys.argv[1:]
    for p in POSTS:
        if only and p["slug"] not in only: continue
        pg.set_content(html(p)); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT / f"{p['slug']}.png"))
        print("ok", p["slug"])
    b.close()
