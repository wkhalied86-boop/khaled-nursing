import pathlib, re
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
# امسح كل السكربتات القديمة اللي فيها lesson1
t = re.sub(r'<script>.*?lesson1\.html.*?</script>', '', t, flags=re.DOTALL)
t = re.sub(r'<script>.*?fix_link2.*?</script>', '', t, flags=re.DOTALL)
t = re.sub(r'<script>.*?مقدمة في التمريض.*?</script>', '', t, flags=re.DOTALL)
# امسح اي بقايا ل lesson-1-content
t = re.sub(r'<div id="lesson-1-content".*?</div>', '', t, flags=re.DOTALL)

code = """
<script>
document.addEventListener('DOMContentLoaded', function(){
  var card = document.querySelector('[data-key="مقدمة في التمريض"]');
  if(card){
    card.style.cursor = 'pointer';
    card.onclick = function(){ window.location.href = 'lesson1.html'; };
    console.log('LINKED CARD 1 OK');
  }
});
</script>
"""
if 'LINKED CARD 1' not in t:
    if '</body>' in t:
        t = t.replace('</body>', code + '\n</body>')
    else:
        t = t + code
    p.write_text(t, encoding='utf-8')
    print("DONE FIX FINAL - CLEANED ALL OLD")
else:
    print("ALREADY")
