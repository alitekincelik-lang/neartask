import sys
from playwright.sync_api import sync_playwright
D=[
 ("w16","cc01.jpg","center 88%","COFFEE &amp; CAKE","for two · <b>£9.95</b>","MONDAY – FRIDAY · 11AM – 6PM","Two coffees and two slices of cake<br>by the bar – the perfect afternoon pause"),
 ("w17","cc10.jpg","center 48%","COFFEE &amp; CAKE","just <b>£9.95</b> for two","MONDAY – FRIDAY · 11AM – 6PM","Meet a friend, slow down and treat<br>yourselves at the Manor"),
 ("w21","roast_lamp.jpg","center 55%","SUNDAY ROAST","Tomorrow","HOMEMADE · FROM 12PM","Proper homemade roasts with all<br>the trimmings – book your table today"),
 ("w22","roast_rib.jpg","center 45%","SUNDAY ROAST","is served today","HOMEMADE · FROM 12PM","Gather the family for a proper<br>Sunday lunch at the Manor"),
]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for n,img,pos,h,s,r,t in D:
        open(n+'.html','w').write(f'<html><head><link rel=stylesheet href=tpl.css></head><body><div class=photo style="background-image:url({img});background-position:{pos}"></div><div class=mid><div class=h>{h}</div><div class=s>{s}</div><div class=rule>{r}</div><div class=t>{t}</div></div><img class=foot src=footer.png><div class=frame></div></body></html>')
        pg.goto(f'file:///home/claude/omh/ph/{n}.html'); pg.wait_for_timeout(1200)
        print(n,pg.evaluate("(()=>{const m=[...document.querySelectorAll('.mid > *')].pop().getBoundingClientRect();const f=document.querySelector('.foot').getBoundingClientRect();const r=document.querySelector('.rule');return [Math.round(m.bottom),Math.round(f.top),r.scrollWidth<=r.clientWidth]})()"))
        pg.screenshot(path=f'/home/claude/omh/ph/{n}.jpg',type='jpeg',quality=90)
    b.close()
