import pathlib, re
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
# شيل الكود اللي فات
t = re.sub(r'<script>.*?LINKED CARD 1.*?</script>', '', t, flags=re.DOTALL)

code = """
<script>
document.addEventListener('click', function(e){
  var card = e.target.closest ? e.target.closest('[data-key="مقدمة في التمريض"]') : null;
  if(card){
    e.preventDefault();
    e.stopPropagation();
    window.location.href = 'lesson1.html';
  }
}, true);
</script>
"""
if 'closest' not in t or 'مقدمة في التمريض' not in t.split('closest')[-1][:500]:
    if '</body>' in t:
        t = t.replace('</body>', code + '\n</body>')
    else:
        t = t + code
    p.write_text(t, encoding='utf-8')
    print("DONE FIX FINAL2")
else:
    print("ALREADY")
