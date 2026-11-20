import glob, re
def cats_for(nm):
 if any(k in nm for k in ["أملاح","سكر","فيتامين","تحليل","دم","كولسترول","ضغط"]):
  return ["القيم الطبيعية","أسباب الارتفاع","أسباب الانخفاض","الأعراض والعلامات","دور الممرض","التغذية العلاجية","الحالات الطارئة","المتابعة","أحدث الأبحاث","مراجعة"]
 if any(k in nm for k in ["دواء","أدوية","حقن","مضاد","مسكن","أنسولين"]):
  return ["تعريف الدواء","الجرعة الصحيحة","طريقة الإعطاء","الأعراض الجانبية","5 حقوق الدواء","التفاعلات","تثقيف المريض","الحالات الطارئة","التخزين","مراجعة"]
 if any(k in nm for k in ["تركيب","قياس","فحص","رعاية","غيار","قسطرة","محلول"]):
  return ["تعريف الإجراء","الأدوات المطلوبة","خطوات الإجراء","مكافحة العدوى","مضاعفات محتملة","توثيق الممرض","تثقيف المريض","الحالات الطارئة","الأخطاء الشائعة","مراجعة"]
 return ["التشريح الدقيق","الوظيفة","الأمراض الشائعة","التشخيص","العلاج","التغذية","التأهيل","الطوارئ","الأبحاث","مراجعة"]
for lesson in sorted(glob.glob("site/lessons/*.html")):
 lt=open(lesson,encoding="utf-8").read()
 h=re.search(r"<h1>(.*?)</h1>",lt); nm=h.group(1) if h else "درس"
 cats=cats_for(nm)
 for f in sorted(glob.glob(lesson.replace(".html","_pages/page-*.html"))):
  i=int(re.search(r"page-(\d+)",f).group(1)); cat=cats[(i-1)//10]
  body=f"""<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{nm}</title></head><body style='font-family:sans-serif;padding:20px;max-width:700px;margin:auto'>
<h1>{nm}</h1><p style='color:#007bff'>🩺 درس: {nm}</p>
<h2>📖 صفحة {i} / 100 - {cat} في {nm}</h2>
<h3>1. {cat} - شرح {nm}</h3><p>في درس {nm}، قسم {cat} هو جزء أساسي. هنا هنتعلم {cat} الخاص بـ {nm} بالتفصيل، وازاي الممرض يتعامل معه في المستشفى، وايه اللي لازم يلاحظه ويسجله.</p>
<h3>2. {cat} في الواقع العملي</h3><p>لما تكون شغال على حالة {nm}، قسم {cat} بيظهر في الشغل اليومي: في التقييم، في الملاحظة، في تنفيذ أوامر الطبيب. أي تغير في {nm} في قسم {cat} لازم تبلغ بيه فورا.</p>
<h3>3. دور الممرض في {cat} - {nm}</h3><p>دورك: 1- تقيم 2- تقيس 3- تنفذ 4- توثق 5- تثقف المريض عن {nm} وخاصة في {cat}.</p>
<h3>💡 معلومة مهمة عن {nm}</h3><p>في {nm}، ركز على {cat}، ومتهملش أي شكوى، ووثق كل حاجة.</p>
<h3>✍️ سؤال للمراجعة</h3><p>اشرح {cat} في {nm}، واذكر 3 نقاط مهمة فيه.</p><br><div style='display:flex;justify-content:space-between'><a href='page-{i-1}.html'>⬅ السابق</a><a href='../../index.html'>🏠 القائمة</a><a href='page-{i+1}.html'>التالي ➡</a></div></body></html>"""
  open(f,"w",encoding="utf-8").write(body)
print("FIXED TYPES FOR ALL 150")
