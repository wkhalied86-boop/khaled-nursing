import pathlib, re
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
# شيل اللي حطيناه قبل كده
t = re.sub(r'<!-- درس 1:.*?-->\s*<div id="lesson-1-content".*?</div>\s*<script>.*?مقدمة في التمريض.*?</script>', '', t, flags=re.DOTALL)
t = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\'.*?fix_click.*?/script>', '', t, flags=re.DOTALL)
# شيل اي بقايا ل lesson-1
t = re.sub(r'<div id="lesson-1-content".*?</div>', '', t, flags=re.DOTALL)
p.write_text(t, encoding='utf-8')

# اعمل صفحة الدرس لوحدها
html = """<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>مقدمة في التمريض</title>
<style>body{font-family:sans-serif;padding:18px;background:#f8fbfb;color:#111}h2{color:#0e7c7b}h3{color:#0e7c7b;margin-top:22px}.card{background:white;padding:14px;border-radius:14px;margin:10px 0}a{display:inline-block;background:#0e7c7b;color:white;padding:10px 18px;border-radius:10px;text-decoration:none}</style></head><body>
<a href="index.html">⬅ رجوع</a>
<h2>1. مقدمة في التمريض</h2><p>أساسيات التمريض</p>
<div class="card"><h3>📌 التعريف الشامل</h3><p>التمريض علم وفن يهدف إلى رعاية الأفراد والأسر والمجتمعات لتعزيز الصحة، الوقاية من الأمراض، استعادة العافية، وتخفيف المعاناة.</p></div>
<div class="card"><h3>📜 التطور التاريخي</h3><p><b>العصور القديمة:</b> ارتبط بالمعتقدات الدينية والأساطير، ثم تطور مع الحضارات المصرية واليونانية (أبقراط).</p><p><b>العصر الإسلامي:</b> برزت رائدات مثل رفيدة الأسلمية التي أسست أول خيمة طبية ميدانية لتقديم رعاية تمريضية منظمة.</p><p><b>التمريض الحديث:</b> أسسته فلورنس نايتنجيل في القرن التاسع عشر، ووضعت أسس النظافة والإحصاء الطبي والتدريب الأكاديمي.</p></div>
<div class="card"><h3>📚 النظريات التمريضية الكبرى</h3><p><b>نظرية البيئة (نايتنجيل):</b> التهوية، الإضاءة، النظافة، والتغذية كعوامل أساسية للشفاء.</p><p><b>نظرية الحاجات الأساسية (فرجينيا هندرسون):</b> 14 حاجة أساسية للإنسان يساعده الممرض على تلبيتها حتى يستعيد استقلاليته.</p><p><b>نظرية العناية الذاتية (دوروثيا أوريم):</b> تعليم المريض كيفية العناية بنفسه.</p></div>
<div class="card"><h3>🏥 مستويات الرعاية الصحية</h3><p><b>1. الأولية:</b> التطعيمات، التثقيف الصحي، والفحص المبكر.</p><p><b>2. الثانوية:</b> التشخيص والعلاج في المستشفيات العامة والعيادات التخصصية.</p><p><b>3. الثالثية:</b> الجراحات الدقيقة، علاج الأورام، والعلاج الطبيعي المكثف.</p></div>
<br><a href="index.html">⬅ رجوع للرئيسية</a>
</body></html>"""
pathlib.Path("lesson1.html").write_text(html, encoding="utf-8")
print("DONE CLEAN + LESSON1.HTML")
