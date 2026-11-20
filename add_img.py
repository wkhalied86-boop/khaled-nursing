import glob, os, re
mp={"قلب":"heart","عقل":"brain","دماغ":"brain","عين":"eye","رئة":"lungs","تنفسي":"lungs","كبد":"liver","كلى":"kidney","عظم":"bone","جلد":"skin","أسنان":"teeth","معدة":"stomach","دم":"blood","أذن":"ear","أنف":"nose","يد":"hand","قدم":"foot","شعر":"hair","وجه":"face","عضلة":"muscle"}
for f in glob.glob("site/lessons/*_pages/page-*.html"):
 t=open(f,encoding="utf-8").read()
 if "loremflickr" in t: continue
 i=int(re.search(r"page-(\d+)",f).group(1))
 name=re.search(r"<h1>(.*?)</h1>",t).group(1) if re.search(r"<h1>(.*?)</h1>",t) else "anatomy"
 eng="anatomy"
 for k,v in mp.items():
  if k in name: eng=v; break
 img1=f"<img src='https://loremflickr.com/700/400/{eng}' style='width:100%;border-radius:15px;margin:10px 0' alt='{name}'><p style='text-align:center;color:#888'>📸 صورة توضيحية لـ {name}</p>"
 img2=f"<img src='https://loremflickr.com/700/400/{eng},medical' style='width:100%;border-radius:15px;margin:10px 0' alt='تشريح {name}'><p style='text-align:center;color:#888'>🔬 صورة تشريحية لـ {name}</p>"
 t=t.replace(f"<h2>",""+img1+f"<h2>",1)
 t=t.replace("<h3>3.",img2+"<h3>3.",1)
 open(f,"w",encoding="utf-8").write(t)
print("IMAGES DONE")
