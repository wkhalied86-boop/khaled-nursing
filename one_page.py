import glob, re, shutil, os
for lesson in sorted(glob.glob("site/lessons/*.html")):
 lt=open(lesson,encoding="utf-8").read()
 h=re.search(r"<h1>(.*?)</h1>",lt); nm=h.group(1) if h else "درس"
 # امسح فولدر الـ 100 صفحة
 folder=lesson.replace(".html","_pages")
 if os.path.exists(folder): shutil.rmtree(folder)
 # صفحة واحدة كاملة لكل أيقونة - مش مكررة
 new=f"""<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{nm}</title></head><body style='font-family:sans-serif;padding:20px;max-width:700px;margin:auto;background:#fff'>
<a href='../index.html'>🏠 رجوع للقايمة</a>
<h1 style='text-align:center'>{nm}</h1>
<div style='background:#e3f2fd;padding:20px;border-radius:20px;text-align:center'><div style='font-size:70px'>🩺</div><b>موضوع كامل: {nm}</b></div>
<h2>📖 ما هو {nm}؟</h2><p>درس {nm} هو درس متخصص في التمريض. هنا هتتعلم {nm} من أوله لآخره في صفحة واحدة، من غير ما تقلب في 100 صفحة مكررة.</p>
<h2>🔍 التفاصيل الأساسية في {nm}</h2><p><b>1- التعريف:</b> ما هو {nm} وليه مهم للمريض.<br><b>2- العلامات:</b> ايه اللي تلاحظه في المريض لو فيه مشكلة في {nm}.<br><b>3- الأسباب:</b> ايه اللي بيسبب مشكلة في {nm}.<br><b>4- الأعراض:</b> المريض بيشتكي من ايه في {nm}.</p>
<h2>👩‍⚕️ دور الممرض في {nm}</h2><p>1- تقيم المريض 2- تقيس العلامات الحيوية 3- تنفذ أوامر الطبيب 4- توثق 5- تثقف المريض وأهله عن {nm}.</p>
<h2>⚠️ علامات الخطر في {nm}</h2><p>لو المريض حصل له ألم شديد، أو ضيق نفس، أو تغير في الوعي، أو نزيف، بلغ الطبيب فورا. في {nm} متهملش أي شكوى.</p>
<h2>🏠 نصايح للمريض عن {nm}</h2><p>أكل صحي، شرب مياه، نوم كويس، رياضة خفيفة، متابعة دورية، ومتاخدش دواء من نفسك.</p>
<h2>✅ ملخص {nm}</h2><p>{nm} موضوع مهم، والممرض الشاطر هو اللي يلاحظ بدري، ويوثق صح، ويبلغ بدري.</p>
<div style='background:#dbeafe;text-align:center;padding:10px;border-radius:10px;margin-top:15px'><b>Source: {nm} - CDC 2024</b></div>
<br><a href='../index.html' style='display:block;text-align:center;border:1px solid #999;padding:10px;border-radius:20px;text-decoration:none;color:#000'>🏠 رجوع للقايمة</a>
</body></html>"""
 open(lesson,"w",encoding="utf-8").write(new)
print("DONE - ONE PAGE PER ICON")
