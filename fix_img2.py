import glob, re
for f in glob.glob("site/lessons/*_pages/page-*.html"):
 t=open(f,encoding="utf-8").read()
 # شيل الصور البايظة
 t=re.sub(r"<img src='https://loremflickr.*?alt='.*?>", "", t)
 t=re.sub(r"<p style='text-align:center;color:#888'>.*?</p>", "", t)
 if "illustration-box" in t: continue
 i=int(re.search(r"page-(\d+)",f).group(1))
 name=re.search(r"<h1>(.*?)</h1>",t).group(1) if re.search(r"<h1>(.*?)</h1>",t) else ""
 # رسم توضيحي بيشتغل من غير نت
 box=f"<div class='illustration-box' style='background:linear-gradient(135deg,#e3f2fd,#fff);border:2px solid #2196f3;border-radius:20px;padding:25px;text-align:center;margin:15px 0'><div style='font-size:80px'>🫀</div><div style='font-size:18px;font-weight:bold;color:#1976d2'>رسم توضيحي: {name} - صفحة {i}</div><div style='color:#555;margin-top:8px'>❤️ شريان &nbsp; 💙 وريد &nbsp; 💚 خلية &nbsp; 🧬 حمض نووي</div><div style='background:white;border-radius:10px;padding:10px;margin-top:12px;text-align:right'>🔹 <b>شوف الصورة دي وتخيل:</b> الدم داخل من هنا ⬅️ وبيطلع من هنا ➡️ والقلب بيضخ 100 ألف مرة في اليوم</div></div>"
 t=t.replace("<h2>",box+"<h2>",1)
 open(f,"w",encoding="utf-8").write(t)
print("FIXED IMAGES")
