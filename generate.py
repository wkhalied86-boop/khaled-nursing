import re, html
def nkey(s):
    return s.lower().strip()
EMOJI_LIST=['1fa7a','1f321','1f489','1f5a5','1f48a','1f6a8','1f3e5','1f9ec','1fac0','1f9a0','1f52c','1fa7b','1f476','1f52a','1f957','1f9e0','1f4cb','1f4da']
def emo(idx):
    code=EMOJI_LIST[idx] if idx < len(EMOJI_LIST) else '1f4da'
    return '<img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/' + code + '.png" style="width:26px;height:26px;vertical-align:middle" alt="">'
topics=[]
cur='X'
cats=[]
with open('topics.txt', encoding='utf-8') as f:
    for line in f:
        line=line.strip()
        if not line:
            continue
        if line.startswith('='):
            cur=re.sub(r'^\d+\.\s*','',line.replace('=','').strip())
            if cur not in cats:
                cats.append(cur)
            continue
        m=re.match(r'^(\d+)\.\s*(.*)',line)
        if m:
            topics.append((int(m.group(1)),m.group(2),cur))
cats_btn=''
for i,c in enumerate(cats):
    cats_btn=cats_btn + '<button class="cat-btn" data-ci="' + str(i) + '">' + emo(i) + ' ' + c + '</button>'
cards=''
for num,title,cat in topics:
    t=html.escape(title, quote=True)
    cc=html.escape(cat, quote=True)
    key=nkey(title + ' ' + cat)
    cards=cards + '<div class="card" data-key="' + key + '" data-cat="' + cc + '"><span class="num">' + str(num) + '</span><h3>' + t + '</h3><p>' + cc + '</p></div>\n'
lang_opts='<option value="ar">Arabic</option><option value="en">English</option>'
a1='<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Khaled</title><style>'
a2='body{font-family:system-ui;background:#0f172a;color:#fff;margin:0}.topbar{display:flex;justify-content:space-between;padding:10px;background:#020617}.banner img{width:100%;display:block}.wrap{padding:20px}.cats{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}.cat-btn{background:#1e293b;color:#fff;border:1px solid #334155;padding:10px;border-radius:20px;display:flex;align-items:center;gap:6px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}.card{background:#1e293b;padding:16px;border-radius:14px}.num{background:#06b6d4;padding:4px 10px;border-radius:20px}'
a3='</style></head><body><div class="topbar"><span>Khaled Academy</span><select id="langSelect">' + lang_opts + '</select></div><div class="banner"><img src="banner.jpg"></div><div class="wrap"><div class="cats"><button class="cat-btn active">All</button>' + cats_btn + '</div><div class="grid">' + cards + '</div></div></body></html>'
open('index.html','w',encoding='utf-8').write(a1 + a2 + a3)
print('Done STEP1 FIXED')
print(len(topics))
