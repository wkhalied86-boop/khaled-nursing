import pathlib
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")

lesson = """
<!-- درس 1: مقدمة في التمريض -->
<div id="lesson-1-content" style="display:none; padding:16px; text-align:right; direction:rtl;">
  <h2>1. مقدمة في التمريض</h2>
  <p>أساسيات التمريض</p>
  <h3>📌 التعريف الشامل</h3>
  <p>التمريض علم وفن يهدف إلى رعاية الأفراد والأسر والمجتمعات لتعزيز الصحة، الوقاية من الأمراض، استعادة العافية، وتخفيف المعاناة.</p>
  <h3>📜 التطور التاريخي</h3>
  <p><b>العصور القديمة:</b> ارتبط بالمعتقدات الدينية والأساطير، ثم تطور مع الحضارات المصرية واليونانية (أبقراط).</p>
  <p><b>العصر الإسلامي:</b> برزت رائدات مثل رفيدة الأسلمية التي أسست أول خيمة طبية ميدانية لتقديم رعاية تمريضية منظمة.</p>
  <p><b>التمريض الحديث:</b> أسسته فلورنس نايتنجيل في القرن التاسع عشر، ووضعت أسس النظافة والإحصاء الطبي والتدريب الأكاديمي.</p>
  <h3>📚 النظريات التمريضية الكبرى</h3>
  <p><b>نظرية البيئة (نايتنجيل):</b> التركيز على التهوية، الإضاءة، النظافة، والتغذية كعوامل أساسية للشفاء.</p>
  <p><b>نظرية الحاجات الأساسية (فرجينيا هندرسون):</b> تحديد 14 حاجة أساسية للإنسان يساعده الممرض على تلبيتها حتى يستعيد استقلاليته.</p>
  <p><b>نظرية العناية الذاتية (دوروثيا أوريم):</b> تعليم المريض كيفية العناية بنفسه.</p>
  <h3>🏥 مستويات الرعاية الصحية</h3>
  <p><b>1. الرعاية الأولية:</b> التطعيمات، التثقيف الصحي، والفحص المبكر.</p>
  <p><b>2. الرعاية الثانوية:</b> التشخيص والعلاج في المستشفيات العامة والعيادات التخصصية.</p>
  <p><b>3. الرعاية الثالثية:</b> الجراحات الدقيقة، علاج الأورام، والعلاج الطبيعي المكثف.</p>
  <button onclick="document.getElementById('lesson-1-content').style.display='none'">رجوع</button>
</div>
<script>
document.addEventListener('click', function(e){
  var el = e.target.closest('*');
  if(el && el.textContent && el.textContent.includes('مقدمة في التمريض') && el.textContent.length < 100){
    var box = document.getElementById('lesson-1-content');
    if(box) box.style.display='block';
  }
});
</script>
"""

if 'lesson-1-content' not in t:
    if '</body>' in t:
        t = t.replace('</body>', lesson + '\n</body>')
    else:
        t = t + lesson
    p.write_text(t, encoding='utf-8')
    print("DONE LESSON 1")
else:
    print("ALREADY ADDED")
