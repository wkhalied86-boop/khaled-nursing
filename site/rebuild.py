import re
t = open('make4.py', encoding='utf-8', errors='ignore').read()
# هات كل النصوص اللي جوة علامات تنصيص وفيها رقم ونقطة
items = re.findall(r'"(\d+\.\s[^"]+)"', t)
# شيل المكرر وحافظ على الترتيب
seen=set(); clean=[]
for x in items:
    x=x.strip()
    if x not in seen:
        seen.add(x); clean.append(x)
print("found", len(clean))
html = """<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>الدرس الرابع</title><style>body{font-family:system-ui;background:#f1f5f9;margin:0}header{background:#1e3a5f;color:#fff;padding:24px 16px;text-align:center}.wrap{max-width:800px;margin:0 auto;padding:16px}.card{background:#fff;border-radius:14px;padding:16px;margin:14px 0}li{background:#f8fafc;border-right:4px solid #1e3a5f;padding:10px 12px;border-radius:8px;margin:8px 0;line-height:1.7;list-style:none}a{color:#fff;text-decoration:none}</style></head><body><header><h1>الدرس الرابع</h1><p>الأجهزة والمعدات الطبية</p><a href="../index.html">⬅ العودة للرئيسية</a></header><div class="wrap"><div class="card"><ul>"""
for it in clean:
    it2 = it.replace("<","").replace(">","")
    html += f'<li>{it2}</li>'
html += '</ul></div></div></body></html>'
open('lessons/lesson-4.html','w',encoding='utf-8').write(html)
print("done4 -", len(clean))
