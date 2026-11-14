import html, base64, pathlib
H = html.escape
F = 'node_modules/@fontsource'
LOGO = 'data:image/png;base64,' + base64.b64encode(open('omh-logo-hr.png','rb').read()).decode()

CSS = f"""
@font-face{{font-family:PF;src:url({F}/playfair-display/files/playfair-display-latin-600-normal.woff2);font-weight:600}}
@font-face{{font-family:PF;src:url({F}/playfair-display/files/playfair-display-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:PFI;src:url({F}/playfair-display/files/playfair-display-latin-400-italic.woff2)}}
@font-face{{font-family:PSC;src:url({F}/playfair-display-sc/files/playfair-display-sc-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:CG;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:CG;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:CG;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-500-italic.woff2);font-style:italic;font-weight:500}}
@font-face{{font-family:CG;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-600-italic.woff2);font-style:italic;font-weight:600}}
@page{{size:A4;margin:0}}
:root{{--bg:#fbf5ea;--bur:#741822;--gold:#b8924a;--ink:#2f2420;--mute:#5c4a3e;--red:#b3121c}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:var(--bg)}}
body{{font-family:CG,serif;color:var(--ink);font-variant-numeric:lining-nums;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;position:relative;overflow:hidden;background:var(--bg);page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto;break-after:auto}}
.frame{{position:absolute;inset:7mm;border:1.4pt solid var(--gold)}}
.frame:after{{content:"";position:absolute;inset:1.6mm;border:.5pt solid var(--gold)}}
.in{{position:absolute;left:19mm;right:19mm;top:15mm;bottom:22mm;display:flex;flex-direction:column}}
.logo{{display:block;margin:0 auto;width:62mm;height:auto}}
.logo.sm{{width:46mm}}
.title{{font-family:PSC;font-weight:700;color:var(--bur);text-align:center;font-size:19pt;letter-spacing:3pt;margin-top:4.5mm}}
.sub{{text-align:center;font-style:italic;font-size:12pt;color:var(--mute);margin-top:1mm}}
.sub b{{font-style:normal;font-weight:700;color:var(--ink)}}
.note{{text-align:center;font-size:10.2pt;line-height:1.25;color:var(--mute);margin:2.2mm 6mm 0;font-style:italic}}
.orn{{display:flex;align-items:center;justify-content:center;gap:3mm;margin:3.2mm auto 0;width:60%}}
.orn:before,.orn:after{{content:"";flex:1;height:.6pt;background:var(--gold)}}
.orn i{{width:2.2mm;height:2.2mm;background:var(--gold);transform:rotate(45deg)}}
.sec{{display:flex;align-items:center;gap:4mm;margin:5mm 0 2mm;break-inside:avoid}}
.sec:before,.sec:after{{content:"";flex:1;height:.6pt;background:var(--gold)}}
.sec h2{{font-family:PSC;font-weight:700;color:var(--bur);font-size:14pt;letter-spacing:2.4pt;white-space:nowrap}}
.sec h2:before,.sec h2:after{{content:"\\25C6";color:var(--gold);font-size:6pt;vertical-align:middle;margin:0 2.4mm;position:relative;top:-1pt}}
.intro{{text-align:center;font-style:italic;font-size:10.8pt;color:var(--mute);line-height:1.25;margin:-.5mm 4mm 2mm}}
.intro b{{font-style:normal;color:var(--bur)}}
.it{{display:flex;align-items:baseline;gap:5mm;padding:1.25mm 0;break-inside:avoid}}
.it .t{{flex:1;min-width:0}}
.n{{font-family:PF;font-weight:600;font-size:11pt;color:var(--ink);letter-spacing:.15pt}}
.d{{font-style:italic;font-size:11.2pt;color:var(--mute);line-height:1.2;margin-top:.3mm}}
.tag{{font-family:CG;font-weight:700;font-size:8.6pt;color:var(--gold);letter-spacing:.6pt;margin-left:1.6mm;white-space:nowrap}}
.p{{font-family:PF;font-weight:600;font-size:11pt;color:var(--bur);white-space:nowrap}}
.sup{{font-style:italic;font-weight:600;font-size:10.2pt;color:var(--bur);white-space:nowrap}}
.box{{border:.6pt solid var(--gold);background:rgba(184,146,74,.08);padding:3.4mm 6mm 3.6mm;text-align:center;margin-top:4.5mm;break-inside:avoid}}
.box h3{{font-family:PSC;font-weight:700;color:var(--bur);font-size:12.5pt;letter-spacing:2pt;margin-bottom:1.2mm}}
.box p{{font-size:11.4pt;line-height:1.28;color:var(--ink)}}
.box p b{{color:var(--bur);font-family:PF;font-weight:600;font-size:10.6pt}}
.red{{color:var(--red);text-align:center;font-weight:700;font-style:italic;font-size:11pt;line-height:1.25;margin:3mm 4mm 0}}
.prices{{display:flex;justify-content:center;gap:9mm;margin-top:3mm;font-family:PF;font-weight:600;color:var(--bur);font-size:13.5pt}}
.prices span{{color:var(--gold);font-size:10pt;align-self:center}}
.mnote{{text-align:center;font-style:italic;font-size:10.8pt;color:var(--mute);margin:1.5mm 0 1mm}}
.foot{{position:absolute;left:19mm;right:19mm;bottom:12.5mm;text-align:center;font-size:9.6pt;color:var(--mute)}}
.foot .sc{{font-style:italic;font-size:10.4pt;color:var(--ink)}}
.foot .ad{{font-family:PSC;font-weight:700;font-size:7.4pt;letter-spacing:1.4pt;color:var(--gold);margin-top:.8mm}}
.grow{{flex:1}}
.tight .in{{left:17mm;right:17mm;top:13.5mm}}
.tight .logo{{width:46mm}} .tight .note{{margin-top:1.6mm}} .tight .logo.sm{{width:42mm}}
.tight .title{{margin-top:3mm}}
.tight .it{{padding:.75mm 0}}
.tight .sec{{margin:3.6mm 0 1.3mm}}
.tight .d{{font-size:10.9pt}}
.tight .orn{{margin-top:2.4mm}}
.boxes{{display:flex;gap:4mm}} .boxes .box{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.loose .it{{padding:2.3mm 0}} .pg2 .it{{padding:1.72mm 0}} .pg2 .sec{{margin:5mm 0 2mm}} .s1 .it{{padding:4.1mm 0}} .s1 .logo{{width:76mm}} .s1 .sec{{margin:12mm 0 3mm}} .s1 .title{{font-size:22pt;margin-top:6mm}} .s2 .it{{padding:3.2mm 0}} .s3 .it{{padding:3.7mm 0}} .s3 .sec{{margin:9mm 0 3mm}} .s3 .d{{font-size:11.8pt}} .s3 .n{{font-size:11.6pt}} .loose .sec{{margin:7mm 0 3mm}} .loose .d{{font-size:11.8pt}} .loose .n{{font-size:11.6pt}}
.info h4{{font-family:PSC;font-weight:700;color:var(--bur);font-size:11.8pt;letter-spacing:1.6pt;margin:6.6mm 0 1.4mm}}
.info p,.info li{{font-size:12pt;line-height:1.38;color:var(--ink)}}
.info ul{{margin-left:5mm}}
.info li{{margin:.6mm 0}}
.info .lead{{text-align:center;font-style:italic;font-size:12.2pt;color:var(--mute);margin-top:3mm}}
.info .end{{text-align:center;font-family:PF;font-weight:600;font-style:normal;color:var(--bur);font-size:12.5pt;margin-top:6mm}}
/* === TEK TİP: tek yazı ailesi (Playfair Display), sabit puntolar, beyaz zemin === */
@font-face{{font-family:PFR;src:url({F}/playfair-display/files/playfair-display-latin-400-normal.woff2)}}
@font-face{{font-family:PFR;src:url({F}/playfair-display/files/playfair-display-latin-400-italic.woff2);font-style:italic}}
:root{{--bg:#ffffff}}
body,.d,.note,.intro,.sub,.info p,.info li,.box p,.red,.mnote,.pl i,.sp,.lead,.foot .sc{{font-family:PFR,serif!important}}
.title{{font-size:18pt!important}}
.sec h2,.info h4,.box h3,.lbl,.foot .ad{{font-family:PSC!important}}
.sec h2,.info h4,.box h3{{font-size:13pt!important}}
.prices,.pl b{{font-size:13pt!important}}
.n,.ci,.p,.sup,.end,.box p b{{font-size:11pt!important}}
.d,.note,.intro,.sub,.info p,.info li,.box p,.red,.mnote,.pl i,.sp,.lead,.foot .sc{{font-size:10pt!important}}
.tag,.lbl,.foot .ad{{font-size:7.5pt!important}}
.box{{background:#fff!important}}
.s1 .it{{padding:5.9mm 0!important}} .s3 .it{{padding:5.6mm 0!important}} .s3 .sec{{margin:11mm 0 4mm!important}} .s2 .it{{padding:4.3mm 0!important}} .pg2 .it{{padding:2mm 0!important}}
.info:not(.ginfo) h4{{margin-top:9.5mm!important}} .ginfo h4{{margin-top:7.5mm!important}} .ginfo p{{margin-bottom:3.4mm!important}}
.tag{{font-family:PFR,serif!important;font-style:normal;letter-spacing:.8pt}}
.sec h2:before,.sec h2:after{{content:""!important;display:inline-block;width:1.5mm;height:1.5mm;background:var(--gold);transform:rotate(45deg);top:-1.4pt!important}}
.prices span{{display:inline-block;width:2mm;height:2mm;background:var(--gold);transform:rotate(45deg);font-size:0!important}}
.logo{{width:58mm!important}} .logo.sm{{width:44mm!important}}
"""

ADDR = '5 Bristol Road · Keynsham · BS31 2BA · 0117 986 3107'

def item(name, desc='', right='', tag='', sup=False):
    t = f'<span class="tag">{H(tag)}</span>' if tag else ''
    d = f'<div class="d">{H(desc)}</div>' if desc else ''
    r = f'<div class="{"sup" if sup else "p"}">{H(right)}</div>' if right else ''
    return f'<div class="it"><div class="t"><div class="n">{H(name)}{t}</div>{d}</div>{r}</div>'

def sec(title):
    return f'<div class="sec"><h2>{H(title)}</h2></div>'

def page(inner, foot, cls=''):
    return f'<section class="page {cls}"><div class="frame"></div><div class="in">{inner}</div><div class="foot">{foot}</div></section>'

def doc(title, pages):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{H(title)}</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

# ---------------- EVENING A LA CARTE ----------------
SC = f'<div class="sc">A 10% discretionary service charge is added to all bills.</div><div class="ad">{ADDR}</div>'

p1 = [f'<img class="logo" src="{LOGO}">',
      '<div class="title">Evening A La Carte Menu</div>',
      '<div class="sub">Served <b>Monday to Saturday</b> between <b>6:30pm</b> and <b>9pm</b></div>',
      '<div class="note">Please advise your server if you have any allergies or dietary requirements. Dishes marked (GFA) can be made gluten free (please state if you would like the gluten free alternative).</div>',
      sec('Starters'),
      item("Goat's Cheese Mixed Leaf Salad", 'Served with Sun Blushed Tomatoes and Pitted Olives', '£8.50'),
      item('Soup of the Day', 'Served with Sourdough Bread', '£7.50', 'GFA'),
      item('Beer-Battered Tiger Prawns', 'Served with Sweet Chilli and Lime', '£9.00'),
      item('Cheese Spring Roll', 'Served with Sun Blushed Tomatoes, Rocket and Sweet Chilli', '£8.50'),
      item('Nocellara Olives', 'Served with Crusty Bread, Rapeseed Oil and Balsamic Vinegar', '£7.00', 'GFA'),
      sec('Vegetarian & Vegan'),
      item('Vegan Butternut Squash and Sweet Potato Pie', 'Served with Garlic Pomme Purée, Market Vegetables and Gravy', '£19.00'),
      item('Wild Mushroom and Spinach Risotto', 'Served with Truffle Oil', '£16.00'),
      sec('Fish'),
      item('Beer-Battered Fish of the Day', 'Served with Hand Cut Chips, Peas and Tartare Sauce', '£19.50'),
      sec('Mains'),
      item('Old Manor Cheese Burger', 'Topped with Dorset Red Cheddar, served in a Seeded Milk Bun with Baby Gem, Tomato and Burger Sauce, served with Hand Cut Chips and House Slaw', '£18.00'),
      item('Pie of the Day', 'Served with Garlic Pomme Purée, Market Vegetables and Gravy', '£19.00'),
      item('Pan-Fried Chicken', 'With Peppers and Onions in a Rich Tomato and Garlic Sauce, served with Crispy Shoestring Potatoes and Garlic Pomme Purée', '£20.00'),
      item('Beef Shin and Wild Mushroom Lasagne', 'Topped with Celeriac and Horseradish Remoulade and Pickled Shallot, served with Garlic Bread and Dressed Mixed Salad', '£19.00'),
      item('Pan-Fried Lamb Rump', 'Served with Ratatouille, Grilled Hispi Cabbage and Garlic Salsa Verde', '£24.00'),
      ]
p2 = [f'<img class="logo sm" src="{LOGO}">',
      sec('Our Steaks'),
      '<div class="intro">All steaks are 28-day aged British steak served with Grilled Vine Tomatoes, Field Mushroom &amp; Hand Cut Koffman Chips. All (GFA).</div>',
      item('8oz Rump Steak', '', '£22.00'),
      item('8oz Sirloin Steak', '', '£24.00'),
      item('8oz Ribeye Steak', '', '£27.00'),
      item('Extra: Peppercorn and Brandy Sauce', '', '£2.50'),
      sec('Sides'),
      item('Mixed Leaf Salad', '', '£4.00'),
      item('Hand Cut Koffman Chips', '', '£4.00'),
      item('Garlic Mushrooms', '', '£4.00'),
      sec('Desserts'),
      item('Dark Chocolate and Walnut Brownie', 'Served with Vanilla Ice Cream', '£9.00'),
      item('Sticky Toffee Pudding', 'Served with Butterscotch Sauce, Toffee Popcorn & Vanilla Ice Cream', '£9.00'),
      item('Vanilla Crème Brûlée', 'Served with Amaretti Biscuits', '£9.00'),
      item('Selection of Ice Creams or Sorbets', '3 scoops', '£7.00'),
      item('Selection of English & French Cheeses', 'Served with Grapes, Quince Jelly and Crackers', '£12.00'),
      item('Option to add Taylors Port', '', '£2.50'),
      '<div class="boxes"><div class="box"><h3>Thursday Steak Deal</h3><p><b>2 x 8oz Rump Steaks and a bottle of wine for £44.00</b><br>every Thursday between 6:30pm and 9pm (alongside our A La Carte menu) with the option to upgrade to a different steak for an additional charge.</p></div>',
      '<div class="box"><h3>Old Manor Sunday Lunches</h3><p>Our delicious homemade Sunday Roasts are served every Sunday from 12pm.</p></div></div>',
      ]
EVE_PAGES = [p1, p2]

# ---------------- SET MENU 2026 ----------------
SF = f'<div class="ad" style="margin-top:0">{ADDR}</div>'
s1 = [f'<img class="logo" src="{LOGO}">',
      '<div class="title">Set Menu 2026</div>',
      '<div class="prices">2 Course £34.00 <span>◆</span> 3 Course £42.50</div>',
      '<div class="red">Please note all supplement prices are per person and will be charged accordingly as per the amount of that dish stated on your pre-order.</div>',
      sec('Starters'),
      item('Tomato & Roasted Red Pepper Soup', 'Served with Basil Oil & a Mini Roll', '', 'VG'),
      item('Ham Hock & Chicken Terrine', 'Served with a Pickled Walnut & Pea Shoot Salad & Toast'),
      item('Cornish Fishcake', 'Served with Capers, Pickled Fennel & Rocket'),
      item('Cheese Spring Roll', 'Served with Sun Blushed Tomatoes, Watercress and Sweet Chilli'),
      item('King Cornish Scallops & Cider & Apple Purée', 'Served with Black Pudding & Parma Ham Crisp', '£3.00 supplement', sup=True),
      item('White Bean & Chive Hummus', 'Served with Roasted Mediterranean Vegetables, Spring Onion & Hazelnut Pesto', '', 'VG'),
      item('Confit Duck Leg Spring Roll', 'Served with a BBQ Sauce & Dressed Leaves', '£1.50 supplement', sup=True),
      item('Smooth Chicken Liver & Bacon Parfait', 'Served with Apple & Ale Chutney, Pickled Vegetables & Crostini', '£1.00 supplement', sup=True),
      ]
s2 = [f'<img class="logo sm" src="{LOGO}">',
      sec('Mains'),
      item('Roast Pork Belly', 'Served with Duck Fat Potatoes, Cider & Apple Purée & Thyme Yorkshire Pudding'),
      item('20oz Braised Beef Short Rib', 'Served with Duck Fat Potatoes & Thyme Yorkshire Pudding', '£3.50 supplement', sup=True),
      item('Nut & Field Mushroom Roast', 'Served with Roast Potatoes & Thyme Yorkshire Pudding'),
      item('Pan Roasted 3 Bone Rack of Lamb (served medium rare)', 'Butternut Squash & Cumin Purée, Crushed New Potatoes & Charred Chicory', '£4.00 supplement', sup=True),
      item('Salmon Papillote with Dill, Fennel & Confit Lemon', 'Served with Buttered Potatoes & Crushed Hazelnuts'),
      item('Lemon & Thyme Corn-fed Chicken Supreme', 'Served with White Onion & Thyme Rösti, Chicken Crackling & Café au Lait Sauce'),
      item('Fillet of Sea Bream on a Bed of Roasted Mediterranean Vegetables', 'Served with Hasselback Potatoes, Prawn, Dill & Caper Sauce'),
      '<div class="mnote">All the above dishes are served with fresh market vegetables.</div>',
      '<div class="orn" style="margin:1mm auto 1.5mm;width:30%"><i></i></div>',
      item('8oz Rib Eye Steak', 'Served with Confit Tomato, Field Mushroom, Garlic and Herb Roast Potatoes & Green Peppercorn & Brandy Sauce (please include in your pre-order how you would like your steak cooked)', '£3.00 supplement', sup=True),
      item('Aubergine & Chickpea Curry', 'Served with Fragrant Basmati Rice', '', 'VG'),
      item('Pan Fried Duck Breast', 'Served with Pommes Fondant, Date Purée, Fennel, Watercress & Rich Port Jus', '£3.00 supplement', sup=True),
      item('Wild Mushroom, Spinach & Tarragon Risotto', 'Served with Truffle Oil & Root Vegetable Crisps', '', 'VG'),
      ]
s3 = [f'<img class="logo sm" src="{LOGO}">',
      sec('Desserts'),
      item('Mulled Poached Pear', 'Served with Vegan Ice Cream & Red Wine Syrup', '', 'VG'),
      item('Vanilla Crème Brûlée', 'Served with Sablé Biscuit'),
      item('Selection of English & French Cheeses', 'Served with Grapes, Quince Jelly, Crackers & Taylors Port', '£3.50 supplement', sup=True),
      item('Chocolate Brownie', 'Served with a Bitter Chocolate Sauce & Clotted Cream'),
      item('Vanilla Panna Cotta', 'Served with Strawberry Sauce and Vanilla Ice Cream'),
      item('Apple, Cider & Stem Ginger Crumble', 'Served with Vanilla Ice Cream'),
      item('Sticky Toffee Pudding', 'Served with a Butterscotch Sauce, Toffee Popcorn & Vanilla Ice Cream'),
      item('Baked White Chocolate & Strawberry Cheesecake', 'Served with Popping Candy & Strawberry Ice Cream'),
      item('Tiramisu'),
      item('Vegan Ice Cream and Sorbets', '', '', 'VG'),
      '<div class="grow"></div>',
      '<div class="note" style="margin-bottom:1mm">(VG) Vegan. Please contact the hotel for allergen and dietary information.</div>',
      ]
info = [f'<img class="logo sm" src="{LOGO}">',
        '<div class="title" style="font-size:16pt">Important Information</div>',
        '<div class="orn"><i></i></div>',
        '<div class="info">',
        '<p class="lead">Thank you for choosing us as a venue to host your event.</p>',
        '<h4>Menu Choices</h4>',
        '<p>Please pick 3 starters, 3 mains and 3 desserts to create your own menu. For allergen and dietary information, please contact the hotel.</p>',
        '<h4>Deposit &amp; Payment</h4>',
        '<ul><li>A non-refundable deposit of £10 per head is required to secure the date.</li>'
        '<li>A deadline for the deposit will be given after your provisional booking; if it is not received by then, the booking will be cancelled.</li>'
        '<li>Final payment is due roughly a week before your event, with the deposit deducted.</li>'
        '<li>If guests cancel, food will only be refunded providing no preparation has taken place.</li></ul>',
        '<h4>Pre Order Deadlines</h4>',
        '<ul><li>Your 9 chosen dishes must be with us 4 weeks before the booking.</li>'
        '<li>The final pre-order is due 2 weeks before the booking, including any allergies or dietary requirements.</li></ul>',
        '<h4>Name Cards</h4>',
        '<p>Tables of 15 and over need name cards showing each guest\'s meal choice. We can supply them for £10.00 in total, or you can supply them free of charge.</p>',
        '<h4>Exclusivity</h4>',
        '<ul><li>Function room exclusivity is available for tables of 25 and over (for fewer guests, the remaining charges will be added to the bill).</li>'
        '<li>Restaurant exclusivity is available for tables of 20 and over.</li></ul>',
        '<h4>Decorations</h4>',
        '<ul><li>Only bio-degradable confetti may be used.</li>'
        '<li>No loose balloons, and nothing may be stuck to the walls.</li>'
        '<li>Photos and tied balloons may be hung from window frames and mantelpieces.</li>'
        '<li>Failure to comply may lead to charges for any damage.</li></ul>',
        '<p class="end">We look forward to hosting your event.</p>',
        '</div>']
SET_PAGES = [s1, s2, s3, info]

pathlib.Path('evening.html').write_text(doc('Evening A La Carte Menu', [page(''.join(p), SC, 'tight'+(' pg2' if i else '')) for i,p in enumerate(EVE_PAGES)]))
pathlib.Path('setmenu.html').write_text(doc('Set Menu 2026', [page(''.join(p), SF, ['loose s1','loose s2','s3',''][i]) for i,p in enumerate(SET_PAGES)]))
print('ok')

# ---------------- COLD BUFFET MENU 2026 ----------------
CB_CSS = """<style>
.cb .ci{text-align:center;font-family:PF;font-weight:600;font-size:12pt;color:var(--ink);padding:1.3mm 0;letter-spacing:.2pt}
.cb .ci .tag{font-size:9pt}
.cb .cd{display:block;width:1.6mm;height:1.6mm;background:var(--gold);transform:rotate(45deg);margin:0 auto;opacity:.75}
.cb .pl{text-align:center;margin:0 0 2.5mm}
.cb .pl b{font-family:PF;font-weight:700;color:var(--bur);font-size:17pt;display:block}
.cb .pl i{font-size:11.8pt;color:var(--mute)}
.cb .lbl{text-align:center;font-family:PSC;font-weight:700;font-size:9.6pt;letter-spacing:2.4pt;color:var(--gold);margin:1mm 0 1mm}
.cb .sp{display:block;font-family:CG;font-style:italic;font-weight:600;font-size:10.8pt;color:var(--bur);margin-top:.6mm;letter-spacing:0}
.cb .logo{width:74mm} .cb .title{font-size:21pt;margin-top:6mm}
.cb .sec{margin:6.5mm 0 2.5mm}
.ginfo p{font-size:11.7pt;line-height:1.36;margin-bottom:1.6mm}
.ginfo h4{margin-top:4.6mm}
</style>"""
def ci(name, tag='', note=''):
    t = f'<span class="tag">{H(tag)}</span>' if tag else ''
    n = f'<span class="sp">{H(note)}</span>' if note else ''
    return f'<div class="ci">{H(name)}{t}{n}</div>'
def dots(items):
    return '<i class="cd"></i>'.join(items)
cb1 = [CB_CSS, f'<img class="logo" src="{LOGO}">',
       '<div class="title">Cold Buffet Menu 2026</div>',
       '<div class="orn"><i></i></div>',
       sec('One Course'),
       '<div class="pl"><b>£28.00 per head</b><i>including the selection listed below</i></div>',
       '<div class="lbl">Menu Selection</div>',
       dots([ci('Platter of Smoked Salmon with Capers and Lemons'),
             ci('Selection of Home-Made Breads', 'V'),
             ci('Olives with Balsamic and Oils', 'V'),
             ci('Pastry Savouries with Meat & Vegetable Fillings', 'V'),
             ci('New Potatoes with Rosemary & Garlic', 'V'),
             ci('Cold Meat Platter'),
             ci("Selection of Chef's Homemade Salad", 'V'),
             ci('Homemade Red Onion and Sage Sausage Rolls'),
             ci('Barbecue Chicken Drumsticks')]),
       sec('Two Course'),
       '<div class="pl"><b>£31.50 per head</b><i>please select two choices from the dessert menu</i></div>',
       dots([ci('Profiteroles with Chocolate Fondant'),
             ci('Chocolate Brownie'),
             ci('Fresh Fruit'),
             ci('Scones, Jam & Clotted Cream'),
             ci('A Selection of Local Cheeses, Biscuits, Celery, Grapes & Apple Platter', '',
                'There is a supplement of £3.25 per head if the cheese platter is one of your chosen desserts')]),
       '<div class="grow"></div>',
       '<div class="note" style="margin-bottom:1mm">(V) Vegetarian</div>']
cb2 = [CB_CSS, f'<img class="logo sm" src="{LOGO}">',
       '<div class="title" style="font-size:16pt">General Information</div>',
       '<div class="orn"><i></i></div>',
       '<div class="info ginfo">',
       '<p class="lead">Thank you for choosing us as a venue to host your event. Please read the information below that applies to this menu. If you have any questions, please do not hesitate to contact us.</p>',
       '<h4>Menu</h4>',
       '<p>We require the final number that we are catering for, along with any allergies or dietary requirements, 7 days prior to the booking.</p>',
       '<p>Should you require any allergen or dietary information, please contact the hotel directly and we can assist with your menu choices.</p>',
       '<h4>Drinks</h4>',
       '<p>Please make us aware if you will be running a bar tab for your guests. We will require a card to be held behind the bar to run a tab.</p>',
       '<p>Wine lists/bottle prices can be provided on request. Please note drinks prices can fluctuate.</p>',
       '<h4>Deposit &amp; Payment</h4>',
       '<p>This menu requires a non-refundable deposit of £10 per head to secure the date. Once a provisional booking has been made, we will give you a deadline for a date that a deposit must be paid by, or the booking will be cancelled and offered to another group.</p>',
       '<p>Once we know the final number that we are catering for, we will contact you to make the final payment. Should any of your guests cancel the food can only be refunded providing no preparation has already taken place.</p>',
       '<h4>Exclusivity</h4>',
       '<p>Please note exclusivity of the function room can only be offered to groups of 25 and over. If you would like exclusivity of the function room with less than this number, the remaining charges would be added to your bill. Exclusivity of the restaurant can be offered to groups of 20 and over.</p>',
       '<h4>Decorations</h4>',
       '<p>Only bio-degradable confetti is permitted on-site. We DO NOT allow any loose balloons because this is a trip hazard to staff, or anything stuck to the walls because it ruins the paint. Photos/tied balloons can be hung from the window frames and mantelpieces. Failure to comply may lead to damage charges. Thank you for your cooperation.</p>',
       '<p class="end">We look forward to hosting your event.</p>',
       '</div>']
pathlib.Path('coldbuffet.html').write_text(doc('Cold Buffet Menu 2026', [page(''.join(cb1), SF, 'cb'), page(''.join(cb2), SF, 'cb')]))
print('cb ok')
