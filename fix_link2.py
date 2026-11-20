import pathlib, re
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
# شيل الكود القديم الغلط
t = re.sub(r'<script>\s*document\.addEventListener\(\'click\'.*?lesson1\.html.*?</script>', '', t, flags=re.DOTALL)
code = """
<script>
// fix_link2 - كارت 1 بس
document.addEventListener('DOMContentLoaded', function(){
  var all = document.querySelectorAll('*');
  all.forEach(function(el){
    if(el.children.length === 0 && el.textContent.trim() === 'مقدمة في التمريض'){
      var card = el;
      // اطلع 3 مستويات لفوق عشان نمسك الكارت كله
      for(var i=0;i<3;i++){ if(card.parentElement) card = card.parentElement; }
      card.style.cursor = 'pointer';
      card.onclick = function(e){ e.stopPropagation(); window.location.href = 'lesson1.html'; };
      el.onclick = function(e){ e.stopPropagation(); window.location.href = 'lesson1.html'; };
    }
  });
});
</script>
"""
if 'fix_link2' not in t:
    if '</body>' in t:
        t = t.replace('</body>', code + '\n</body>')
    else:
        t = t + code
    p.write_text(t, encoding='utf-8')
    print("DONE FIX LINK2")
else:
    print("ALREADY")
