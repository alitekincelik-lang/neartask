import sys
from playwright.sync_api import sync_playwright
FIT="""document.fonts.ready.then(()=>{
 const fit=(el,max)=>{let fs=parseFloat(getComputedStyle(el).fontSize);while(el.getBoundingClientRect().width>max&&fs>10){fs-=1;el.style.fontSize=fs+'px'}};
 fit(document.querySelector('.l1'),990);fit(document.querySelector('.r2'),970);
 document.querySelectorAll('.rule').forEach(r=>{r.style.display='table';r.style.marginLeft='auto';r.style.marginRight='auto'});
 const rs=[...document.querySelectorAll('.rule')];let fs=21;rs.forEach(r=>r.style.fontSize=fs+'px');
 while(Math.max(...rs.map(r=>r.getBoundingClientRect().width))>980){fs-=0.5;rs.forEach(r=>r.style.fontSize=fs+'px')}
 const l=document.querySelector('.l1').getBoundingClientRect().left;document.getElementById('tg').style.marginLeft=(l+3)+'px'})"""
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    pg.goto('file:///home/claude/sera/p14r.html'); pg.wait_for_timeout(900); pg.evaluate(FIT); pg.wait_for_timeout(300)
    print(pg.evaluate("document.querySelector('.mid').getBoundingClientRect().bottom"))
    pg.screenshot(path='sera_2026-11-14.jpg',type='jpeg',quality=92)
    # layers
    pg.add_style_tag(content='.mid,.foot{visibility:hidden}'); pg.screenshot(path='L_bg_photo.png')
    pg.add_style_tag(content='.ph{visibility:hidden}'); pg.screenshot(path='L_bg.png')
    pg.add_style_tag(content='body{background:transparent!important}'); 
    pg.evaluate("document.body.style.background='transparent'")
    pg.add_style_tag(content='.ph{visibility:visible}'); pg.screenshot(path='L_photo.png',omit_background=True)
    pg.add_style_tag(content='.ph{visibility:hidden}.mid,.foot{visibility:visible}'); pg.screenshot(path='L_text.png',omit_background=True)
    b.close()
