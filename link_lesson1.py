import pathlib
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
code = """
<script>
document.addEventListener('click', function(e){
  var el = e.target;
  // اطلع لفوق لحد ما نلاقي الكارت
  for(var i=0;i<4;i++){
    if(!el) break;
    if(el.textContent && el.textContent.includes('مقدمة في التمريض')){
      window.location.href = 'lesson1.html';
      return;
    }
    el = el.parentElement;
  }
});
</script>
"""
if 'lesson1.html' not in t or 'link_lesson1' not in t:
    # شيل اي كود قديم بيعمل مشكلة
    if '</body>' in t:
        t = t.replace('</body>', code + '\n</body>')
    else:
        t = t + code
    p.write_text(t, encoding='utf-8')
    print("DONE LINK")
else:
    print("ALREADY LINKED")
