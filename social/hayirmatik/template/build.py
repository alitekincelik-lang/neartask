import sys,glob,os
from PIL import Image
from playwright.sync_api import sync_playwright
here=os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':190})
    pg.goto('file://'+here+'/footer.html'); pg.wait_for_timeout(600)
    pg.screenshot(path=here+'/footer.png',omit_background=True); b.close()
ft=Image.open(here+'/footer.png').convert('RGBA')
os.makedirs(here+'/out',exist_ok=True)
for f in sorted(glob.glob(sys.argv[1]+'/*.jpg')):
    im=Image.open(f).convert('RGB')
    for y in range(1150,1350):
        im.paste(im.getpixel((20,y)),(0,y,1080,y+1))
    im.paste(ft,(0,1160),ft)
    im.save(here+'/out/'+os.path.basename(f),quality=95,subsampling=0)
    print(f)
