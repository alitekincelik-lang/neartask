const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const n of process.argv.slice(2)){
 const p=await b.newPage({viewport:{width:794,height:1123},deviceScaleFactor:2});
 await p.goto('file://'+process.cwd()+'/'+n+'.html');await p.evaluate(()=>document.fonts.ready);
 const r=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((pg,i)=>{const inn=pg.querySelector('.in'),f=pg.querySelector('.foot');const kids=[...inn.children];const last=kids[kids.length-1].getBoundingClientRect().bottom;const ib=inn.getBoundingClientRect();const over=[...pg.querySelectorAll('.it')].filter(e=>e.scrollWidth>e.clientWidth+1).length;return {page:i+1,contentBottom:Math.round(last-ib.top),avail:Math.round(ib.height),slack_mm:+((ib.bottom-last)/3.7795).toFixed(1),hOverflow:over}}));
 console.log(n,JSON.stringify(r));
 await p.pdf({path:n+'.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
 const pages=await p.$$('.page');for(let i=0;i<pages.length;i++)await pages[i].screenshot({path:`${n}-p${i+1}.png`});
}
await b.close();})();
