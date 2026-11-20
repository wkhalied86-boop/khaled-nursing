import glob, re
mp={"قلب":("🫀","القلب بيضخ 100 ألف مرة في اليوم"),"عيون":("👁️","الضوء بيدخل من القرنية للشبكية"),"عين":("👁️","الضوء بيدخل من القرنية للشبكية"),"عقل":("🧠","المخ فيه 86 مليار خلية"),"دماغ":("🧠","المخ فيه 86 مليار خلية"),"رئة":("🫁","الهوا بيدخل للرئة والأكسجين للدم"),"كبد":("🟤","الكبد بينظف الدم"),"كلى":("🫘","الكلى بتفلتر الدم")}
mp.update({"عظم":("🦴","العظم جواه نخاع بيصنع الدم"),"جلد":("🧴","الجلد بيحمي الجسم"),"أسنان":("🦷","السن فيه مينا وعاج وعصب"),"معدة":("🫠","المعدة فيها حمض بيهضم الأكل"),"دم":("🩸","الدم بيشيل الأكسجين"),"أذن":("👂","الصوت بيهز طبلة الأذن"),"أنف":("👃","الأنف بيفلتر الهوا"),"يد":("✋","اليد فيها 27 عظمة"),"قدم":("🦶","القدم بتشيل وزن الجسم"),"عضلة":("💪","العضلة بتنقبض وترتخي")})
for f in glob.glob("site/lessons/*_pages/page-*.html"):
 t=open(f,encoding="utf-8").read()
 t=re.sub(r"<div class='illustration-box'.*?</div></div>","",t,flags=re.S)
 i=int(re.search(r"page-(\d+)",f).group(1))
 name=re.search(r"<h1>(.*?)</h1>",t).group(1) if re.search(r"<h1>(.*?)</h1>",t) else ""
 emoji,desc="🧬","تخيل العضو ده شغال جوه جسمك"
 for k,v in mp.items():
  if k in name: emoji,desc=v; break
 box=f"<div class='illustration-box' style='background:#e3f2fd;border:2px solid #2196f3;border-radius:20px;padding:20px;text-align:center'><div style='font-size:80px'>{emoji}</div><div><b>رسم توضيحي: {name} - صفحة {i}</b></div><div style='background:white;padding:10px;margin-top:10px'>{desc}</div></div>"
 if "illustration-box" not in t: t=t.replace("<h2>",box+"<h2>",1)
 open(f,"w",encoding="utf-8").write(t)
print("DONE")
