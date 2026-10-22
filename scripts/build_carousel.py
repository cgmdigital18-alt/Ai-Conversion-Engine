"""Build an offline HTML carousel and exact, reusable layer specifications.

Evolves PR #1's ten-slide sequence, .preview-row/.slide-wrapper/.slide shells,
brand label, progress counter, large headline, list and CTA components.
The historic source stays intact on its original branch.
"""
from pathlib import Path
import base64
import html
import json

ROOT = Path(__file__).resolve().parents[1]
N = '#00306C'
T = '#D2F2FB'
C = '#FFF0CD'
G = '#FFE7AF'
W = '#FFFFFF'
slides = []

def slide(name, bg, fg=N):
    s = {'name': name, 'background': bg, 'foreground': fg, 'layers': []}
    slides.append(s)
    return s

def text(s, value, x, y, width, size, font='DM Sans', color=None,
         weight=500, line=1.2, style='normal', role='body'):
    s['layers'].append(dict(type='text', text=value, x=x, y=y, width=width,
        size=size, font=font, color=color or s['foreground'], weight=weight,
        line_height=line, style=style, role=role))

def box(s, x, y, width, height, fill, stroke=None):
    s['layers'].append(dict(type='rect', x=x, y=y, width=width, height=height,
        fill=fill, stroke=stroke))

def rule(s, x, y, width, color=None):
    box(s,x,y,width,2,color or s['foreground'])

def head(s, value, y=244, size=112, width=888):
    text(s,value,96,y,width,size,'Barlow Condensed',weight=700,line=.99,role='headline')

def serif(s, value, y, size=66, color=None):
    text(s,value,96,y,888,size,'Libre Baskerville',color=color,line=1.14,style='italic',role='emphasis')

def label(s, value, x, y, width=800, color=None):
    text(s,value,x,y,width,24,color=color,weight=700,line=1.15,role='label')

# 01. Retains the hook role. Replaces status claims with a specific process issue.
s=slide('Before you add AI',N,C)
box(s,0,0,24,1440,G)
head(s,'BEFORE YOU\nADD AI,',248,148)
serif(s,'fix your\nfollow-up.',578,100,G)
rule(s,96,902,96,G)
text(s,'A workflow check for service\nbusinesses handling new inquiries.',96,954,840,42,color=C)
label(s,'START WITH THE PROCESS',96,1162,color=T)

# 02. Retains the problem slide, replaces the unsupported 90% statistic.
s=slide('Who owns the reply?',C)
head(s,'An inquiry\nis waiting.',244,126)
serif(s,'Who owns the reply?',532,61)
box(s,96,676,888,394,N)
label(s,'EXAMPLE INQUIRY',132,716,color=T)
text(s,'Request for a quote',132,778,800,58,'Barlow Condensed',G,700,1.05)
rule(s,132,866,816,T)
text(s,'Assigned to',132,901,350,28,color=C)
text(s,'Unassigned',132,944,800,52,color=G,weight=700)
text(s,'A reply template still needs someone\nresponsible for sending the reply.',96,1136,888,36)

# 03. Retains systems over isolated tool use, with a defined operational sequence.
s=slide('Build the process',T)
head(s,'Build the process\nbefore the prompt.',244,108)
rows=[('01','Capture','Record the inquiry in one place.'),
      ('02','Assign','Name the person responsible.'),
      ('03','Schedule','Set the next action and due date.'),
      ('04','Track','Record the outcome.')]
for i,(n,a,b) in enumerate(rows):
    y=574+i*146
    rule(s,96,y,888)
    label(s,n,96,y+31,80)
    text(s,a,194,y+24,780,48,'Barlow Condensed',weight=700,line=1.05)
    text(s,b,194,y+82,780,30)

# 04. Retains content reuse, replaces the 30 pieces / 20 minutes claim.
s=slide('Reuse real questions',W)
head(s,'Turn real questions\ninto useful content.',244,108)
label(s,'START WITH A BUYER QUESTION',96,530)
box(s,96,585,888,202,T)
text(s,'Why do these two\nservice quotes differ?',128,620,820,52,'Libre Baskerville',style='italic',line=1.16)
rule(s,96,850,888)
label(s,'PUBLIC POST',96,888,350)
text(s,'Explain the scope differences.',96,938,888,40)
label(s,'FOLLOW-UP REPLY',96,1041,500)
text(s,'Point to the relevant scope details.',96,1091,888,40)

# 05. Retains sales follow-up, removes claims about knowing exactly what to say.
s=slide('Schedule quote follow-up',N,C)
head(s,'Put quote follow-up\non the calendar.',244,108)
box(s,96,570,888,560,C)
fields=[('STAGE','Quote sent'),('OWNER','Assigned team member'),
        ('NEXT ACTION','Ask about open questions'),('DUE','Agreed follow-up date')]
for i,(a,b) in enumerate(fields):
    y=608+i*126
    label(s,a,132,y,color=N)
    text(s,b,132,y+40,810,40,color=N)
    if i<3:rule(s,132,y+102,816,N)
text(s,'Agree on timing. Log the outcome.',96,1180,888,34,color=T)

# 06. Retains measurement and decisions without instantaneous-answer claims.
s=slide('Measure the handoff',C)
head(s,'Measure where\ninquiries stop.',244,122)
label(s,'FOLLOW THE SAME COHORT OF INQUIRIES',96,549)
stages=['Inquiry','Contacted','Consult','Sale']
for i,a in enumerate(stages):
    x=96+i*225
    box(s,x,611,213,96,N)
    text(s,a,x+15,642,183,34,'Barlow Condensed',C,700,1)
rule(s,96,787,888)
label(s,'FIRST RESPONSE TIME',96,831)
text(s,'Track the median time from inquiry\nto first human reply.',96,884,888,38)
label(s,'INQUIRY-TO-CONSULT RATE',96,1025)
text(s,'Booked consults ÷ inquiries × 100',96,1078,888,38)
text(s,'Use one date range and clear stage definitions.',96,1180,888,28)

# 07. Replaces the unsupported 10x result with a bounded AI task.
s=slide('Give AI a defined job',T)
head(s,'Give AI\none defined job.',244,130)
serif(s,'A draft needs a review.',564,59)
rule(s,96,723,888)
label(s,'AI ASSISTS',96,769)
text(s,'Draft a reply using your approved\nservice details and next step.',96,822,888,41)
rule(s,96,961,888)
label(s,'YOUR TEAM CHECKS',96,1007)
text(s,'Verify scope, price and promises\nbefore a customer receives the reply.',96,1060,888,41)

# 08. Replaces generic results with a practical diagnostic.
s=slide('Check five inquiries',W)
head(s,'Check your last\nfive inquiries.',244,128)
label(s,'MARK EACH FIELD PRESENT OR MISSING',96,548)
items=['Named owner','First response time','Next action + due date','Recorded outcome']
for i,a in enumerate(items):
    y=621+i*116
    box(s,96,y,42,42,W,N)
    text(s,a,169,y-4,815,43)
    rule(s,169,y+76,815,T)
box(s,96,1132,888,96,G)
text(s,'Fix the first missing handoff this week.',120,1162,840,33,weight=700)

# 09. Retains the brand slide while aligning the actual services and audience.
s=slide('The work behind marketing',C)
head(s,'The work behind\nyour marketing.',244,120)
cards=[('MESSAGE','Explain the service and next step.'),
       ('FOLLOW-UP','Keep inquiries moving.'),
       ('PROOF','Show relevant\ncompleted work.'),
       ('TRACKING','See where the process needs work.')]
for i,(a,b) in enumerate(cards):
    x=96+(i%2)*456; y=579+(i//2)*205
    rule(s,x,y,432)
    label(s,a,x,y+29,432)
    text(s,b,x,y+80,416,34,line=1.25)
text(s,'Edge21 pairs marketing infrastructure\nwith content execution for established\nservice businesses.',96,1072,888,37)

# 10. Retains a CTA but removes the unverified weekly AI-playbook promise.
s=slide('Start with your process',N,C)
box(s,0,0,24,1440,T)
head(s,'YOUR NEXT\nMARKETING FIX',244,138)
serif(s,'starts with\nyour process.',569,88,G)
rule(s,96,839,888,T)
text(s,'Explore Edge21’s marketing\ninfrastructure and content services.',96,894,888,41)
box(s,96,1055,888,116,G)
text(s,'edge21marketing.com',128,1091,824,52,'Barlow Condensed',N,700,1.0,role='cta')

font_defs=[]
for family,weight,style,filename in [
    ('Barlow Condensed',700,'normal','BarlowCondensed-700.ttf'),
    ('DM Sans',500,'normal','DMSans-500.ttf'),
    ('DM Sans',700,'normal','DMSans-700.ttf'),
    ('Libre Baskerville',400,'italic','LibreBaskerville-400-Italic.ttf')]:
    data=base64.b64encode((ROOT/'assets/fonts'/filename).read_bytes()).decode()
    font_defs.append(f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:{style};src:url(data:font/ttf;base64,{data}) format('truetype');font-display:block}}")

css='''
:root{--navy:#00306C;--teal:#D2F2FB;--cream:#FFF0CD;--gold:#FFE7AF;--scale:.34;--height:1440px}
*{box-sizing:border-box}body{margin:0;padding:28px;background:#e8e8e4;color:var(--navy);font-family:'DM Sans',sans-serif}
h1{font-size:20px;margin:0}p{margin:0}.toolbar{max-width:1240px;margin:0 auto 28px;display:flex;flex-wrap:wrap;align-items:center;gap:12px}.toolbar .title{margin-right:auto}.toolbar p{font-size:13px;margin-top:5px}
button,select{font:500 14px 'DM Sans',sans-serif;padding:10px 14px;border:1px solid var(--navy);background:white;color:var(--navy);border-radius:0;cursor:pointer}button[aria-pressed=true]{background:var(--navy);color:white}button:focus-visible,select:focus-visible{outline:3px solid #A15B00;outline-offset:3px}
main{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:30px;max-width:1240px;margin:auto}.preview-row{min-width:0}.slide-label{font-size:12px;margin-bottom:8px;font-weight:700;letter-spacing:.05em}.slide-wrapper{width:calc(1080px * var(--scale));height:calc(var(--height) * var(--scale));overflow:hidden}.slide{position:relative;width:1080px;height:var(--height);overflow:hidden;transform:scale(var(--scale));transform-origin:top left}.slide-canvas{position:relative;width:1080px;height:1440px}body.ratio45{--height:1350px}body.ratio45 .slide-canvas{transform:translateY(-45px)}
.layer{position:absolute;margin:0;white-space:pre-wrap;overflow-wrap:normal;font-kerning:normal;font-optical-sizing:auto}.headline{letter-spacing:-.012em}.emphasis{letter-spacing:-.035em}.label{letter-spacing:.055em}.brand{position:absolute;left:96px;top:100px;font:700 34px 'DM Sans',sans-serif;letter-spacing:-.055em}.brand small{font-weight:500;font-size:19px;letter-spacing:.02em;margin-left:14px}.slide-num{position:absolute;right:96px;top:110px;font-size:23px;font-weight:700}.top-rule{position:absolute;left:96px;top:170px;width:888px;height:2px;background:currentColor}.footer{position:absolute;left:96px;right:96px;top:1312px;display:flex;justify-content:space-between;align-items:center;font-size:22px}.step-counter{display:flex;gap:10px}.step-pip{width:19px;height:3px;background:currentColor;opacity:.27}.step-pip.active{opacity:1}.swipe-hint{font-size:21px;font-weight:700}
.guides .slide-canvas:after{content:'';pointer-events:none;position:absolute;inset:180px 90px;border:3px dashed #C74833}.guides .slide-canvas:before{content:'';pointer-events:none;position:absolute;inset:45px 0;border-top:3px dashed #437750;border-bottom:3px dashed #437750}.editing [contenteditable=true]{outline:2px dashed #A15B00;outline-offset:7px;min-width:30px}.export-note{max-width:1240px;margin:28px auto 0;font-size:13px;line-height:1.6}.slide[hidden]{display:none}
@media(max-width:420px){body{padding:16px}main{display:block}.preview-row{margin-bottom:26px}}
@media print{@page{size:810pt 1080pt;margin:0}body{padding:0;background:white}.toolbar,.slide-label,.export-note{display:none}main{display:block;margin:0;max-width:none}.preview-row{break-after:page;margin:0}.preview-row:last-child{break-after:auto}.slide-wrapper,.slide{width:1080px;height:1440px;transform:none}.slide-canvas{transform:none!important}.guides .slide-canvas:before,.guides .slide-canvas:after{display:none}body{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
'''

out=['<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">',
     '<title>Edge21 | Before you add AI | Editorial carousel</title><style>',*font_defs,css,'</style></head><body>',
     '<header class="toolbar"><div class="title"><h1>Edge21 / Marketing infrastructure</h1><p>Ten editable slides. Portrait master. Offline fonts.</p></div>',
     '<label for="ratio">Format</label><select id="ratio"><option value="34">3:4 · 1080 × 1440</option><option value="45">4:5 · 1080 × 1350</option></select>',
     '<button id="guides" aria-pressed="false">Show guides</button><button id="edit" aria-pressed="false">Edit copy</button><button id="save">Save template</button><button id="print">Print 3:4 PDF</button></header><main>']
for i,s in enumerate(slides,1):
    out.append(f'<section class="preview-row"><div class="slide-label">{i:02} / {html.escape(s["name"])}</div><div class="slide-wrapper"><article class="slide" id="slide-{i:02}" aria-label="Slide {i}: {html.escape(s["name"])}" style="background:{s["background"]};color:{s["foreground"]}"><div class="slide-canvas">')
    out.append(f'<div class="brand">EDGE21<small>MARKETING</small></div><div class="slide-num">{i:02} / 10</div><div class="top-rule"></div>')
    for k,l in enumerate(s['layers']):
        st=f'left:{l["x"]}px;top:{l["y"]}px;width:{l["width"]}px;'
        if l['type']=='rect':
            out.append(f'<div class="layer shape" aria-hidden="true" style="{st}height:{l["height"]}px;background:{l["fill"]};'+(f'border:2px solid {l["stroke"]};' if l.get('stroke') else '')+'"></div>')
        else:
            st+=f'font:{l["style"]} {l["weight"]} {l["size"]}px/{l["line_height"]} \'{l["font"]}\',sans-serif;color:{l["color"]};'
            tag='h2' if l['role']=='headline' else 'p'
            out.append(f'<{tag} class="layer {l["role"]} editable" data-layer="{k}" style="{st}">{html.escape(l["text"])}</{tag}>')
    out.append('<footer class="footer"><div class="step-counter" aria-hidden="true">'+''.join(f'<span class="step-pip'+(' active' if j==i else '')+'"></span>' for j in range(1,11))+'</div><div class="swipe-hint">'+('EXPLORE EDGE21' if i==10 else 'KEEP READING →')+'</div></footer></div></article></div></section>')
out.append('''</main><p class="export-note">Edit copy, then save the template to preserve your changes. Guide lines are for design review and are hidden in print. The red box marks the shared text area, x 90–990 and y 180–1260. Green lines mark the optional 4:5 crop. The supplied exports contain no guides. See docs/CANVA-SPECIFICATIONS.md for exact Canva coordinates and export steps.</p>
<script>
const body=document.body;
const ratio=document.getElementById('ratio');
ratio.addEventListener('change',()=>{body.classList.toggle('ratio45',ratio.value==='45');fit()});
document.getElementById('guides').addEventListener('click',e=>{const on=body.classList.toggle('guides');e.currentTarget.setAttribute('aria-pressed',on);e.currentTarget.textContent=on?'Hide guides':'Show guides'});
document.getElementById('edit').addEventListener('click',e=>{const on=body.classList.toggle('editing');document.querySelectorAll('.editable').forEach(x=>x.contentEditable=on);e.currentTarget.setAttribute('aria-pressed',on);e.currentTarget.textContent=on?'Finish editing':'Edit copy'});
document.getElementById('save').addEventListener('click',()=>{const clone=document.documentElement.cloneNode(true);clone.querySelector('body').classList.remove('editing','guides','ratio45');clone.querySelectorAll('[contenteditable]').forEach(x=>x.removeAttribute('contenteditable'));clone.querySelectorAll('button[aria-pressed]').forEach(x=>x.setAttribute('aria-pressed','false'));clone.querySelector('#edit').textContent='Edit copy';clone.querySelector('#guides').textContent='Show guides';clone.querySelector('#ratio').value='34';const blob=new Blob(['<!DOCTYPE html>\\n'+clone.outerHTML],{type:'text/html;charset=utf-8'});const a=document.createElement('a');const url=URL.createObjectURL(blob);a.href=url;a.download='carousel-ai-edge21-edited.html';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)});
document.getElementById('print').addEventListener('click',()=>window.print());
function fit(){document.querySelectorAll('.preview-row').forEach(r=>r.style.setProperty('--scale',Math.min(r.clientWidth/1080,.43)))}
window.addEventListener('resize',fit);fit();
</script></body></html>''')
(ROOT/'carousel-ai-edge21.html').write_text('\n'.join(out))
(ROOT/'slide-specifications.json').write_text(json.dumps({'canvas':{'width':1080,'height':1440,'optional_crop':{'width':1080,'height':1350,'top':45}},'palette':{'navy':N,'light_teal':T,'warm_cream':C,'soft_gold':G,'white':W},'slides':slides},indent=2,ensure_ascii=False))
reference=['# Exact Canva layer reference','',
    'Coordinates and font sizes are source pixels on the 1080 x 1440 master. For 4:5 subtract 45 from every Y coordinate. Text heights follow font size, line height and the supplied line breaks. Shape sizes are width x height. See CANVA-SPECIFICATIONS.md for Canva unit calibration.','']
for i,s in enumerate(slides,1):
    reference.extend([f'## {i:02}. {s["name"]}',f'Background {s["background"]}. Foreground {s["foreground"]}.','',
        '| Layer / exact copy | X | Y | W | Size or H | Font / weight / line height / color |','| --- | --- | --- | --- | --- | --- |'])
    for l in s['layers']:
        if l['type']=='text':
            name=l['text'].replace('\n','<br>')
            reference.append(f'| {name} | {l["x"]} | {l["y"]} | {l["width"]} | {l["size"]} | {l["font"]} {l["style"]} / {l["weight"]} / {l["line_height"]} / {l["color"]} |')
        else:
            reference.append(f'| Rectangle | {l["x"]} | {l["y"]} | {l["width"]} | {l["height"]} | Fill {l["fill"]}'+(f', 2 px stroke {l["stroke"]}' if l.get('stroke') else '')+' |')
    reference.append('')
(ROOT/'docs/LAYER-REFERENCE.md').write_text('\n'.join(reference))
print(f'Built {len(slides)} slides and exact layer specifications.')
