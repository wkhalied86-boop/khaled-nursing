import pathlib
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")

fix = """
<script>
document.addEventListener('DOMContentLoaded', function(){
  var box = document.getElementById('lesson-1-content');
  if(!box) return;
  // خلي صندوق الدرس فوق كل حاجة
  box.style.position = 'fixed';
  box.style.top = '0';
  box.style.left = '0';
  box.style.right = '0';
  box.style.bottom = '0';
  box.style.background = 'white';
  box.style.overflowY = 'auto';
  box.style.zIndex = '9999';
  box.style.display = 'none';

  function openLesson(){
    box.style.display = 'block';
    window.scrollTo(0,0);
  }
  // دور على أي عنصر فيه اسم الدرس وخليه زرار
  document.querySelectorAll('*').forEach(function(el){
    if(el.children.length === 0 && el.textContent.trim().startsWith('مقدمة في التمريض')){
      el.style.cursor = 'pointer';
      el.onclick = openLesson;
      if(el.parentElement) el.parentElement.onclick = openLesson;
      if(el.parentElement && el.parentElement.parentElement) el.parentElement.parentElement.onclick = openLesson;
    }
  });
  // زرار الرجوع
  var btn = box.querySelector('button');
  if(btn){ btn.onclick = function(){ box.style.display='none'; }; }
});
</script>
"""
if 'fix_click' not in t and 'lesson-1-content' in t:
    if '</body>' in t:
        t = t.replace('</body>', fix + '\n</body>')
    else:
        t = t + fix
    p.write_text(t, encoding='utf-8')
    print("DONE FIX CLICK")
else:
    print("ALREADY FIXED OR NO LESSON")
