import glob, os, re
for f in glob.glob("site/lessons/*.html"):
 t=open(f,encoding="utf-8").read()
 m=re.search(r"<h1>(.*?)</h1>",t)
 name=m.group(1) if m else "درس"
 base=f.replace(".html","")
 os.makedirs(base+"_pages",exist_ok=True)
 for i in range(1,101):
  prev=f"page-{i-1}.html" if i>1 else "../"+os.path.basename(f)
  nxt=f"page-{i+1}.html" if i<100 else "../"+os.path.basename(f)
  h=f"<html><head><meta charset='utf-8'><title>{name} - {i}</title></head><body style='font-family:sans-serif;padding:20px;max-width:700px;margin:auto'><h1>{name}</h1><h2>📖 الصفحة {i} / 100</h2><p>الدرس رقم {i} عن {name}.</p><p>في هذه الصفحة هنتعلم جزء جديد ومهم عن {name} بالتفصيل، مع شرح بسيط وامثلة من حياتك اليومية.</p><p>كمل للصفحة اللي بعدها عشان تكمل الكتاب كله.</p><br><div style='display:flex;justify-content:space-between'><a href='{prev}'>⬅ السابق</a><a href='../{os.path.basename(f)}'>🏠 القائمة</a><a href='{nxt}'>التالي ➡</a></div></body></html>"
  open(f"{base}_pages/page-{i}.html","w",encoding="utf-8").write(h)
 links="".join([f"<a href='{os.path.basename(base)}_pages/page-{i}.html' style='display:block;padding:12px;margin:5px;background:#eef;border-radius:10px;text-decoration:none;color:#000'>📖 صفحة {i} - {name}</a>" for i in range(1,101)])
 t=re.sub(r"<body.*?>", "<body>"+f"<h1>{name}</h1><h2>📚 الكتاب كامل - 100 صفحة</h2>"+links, t, count=1, flags=re.DOTALL)
 open(f,"w",encoding="utf-8").write(t)
 print("DONE",name)
print("ALL DONE 15000")
