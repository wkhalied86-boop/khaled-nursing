import pathlib, re
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
t = re.sub(r'<div style="max-width:700px.*?</div>', '', t, flags=re.S)
t = t.replace('id="searchInput"', 'id="searchInputOLD"')
search_html = '''<div style="max-width:700px;margin:14px auto;padding:0 12px"><input id="searchInput" type="text" placeholder="ابحث في الأقسام... 🔍" style="width:100%;padding:14px 16px;font-size:17px;border-radius:14px;border:2px solid #ddd;outline:none;text-align:right;direction:rtl"></div>'''
idx = t.find('class="cat-btn"')
if idx != -1:
    start = t.rfind('<div', 0, idx)
    if start == -1: start = idx
    t = t[:start] + search_html + '\n' + t[start:]
js = '''<script>
var inp = document.getElementById("searchInput");
inp.addEventListener("input", function(){
  var q = this.value.trim().toLowerCase();
  document.querySelectorAll(".card").forEach(function(c){
    var txt = (c.textContent + " " + (c.getAttribute("data-key")"") + " " + (c.getAttribute("data-cat")"")).toLowerCase();
    c.style.setProperty("display", (!q || txt.includes(q)) ? "" : "none", "important");
  });
  document.querySelectorAll(".cat-btn").forEach(function(b){
    var txt = b.textContent.toLowerCase();
    b.style.setProperty("display", (!q || txt.includes(q)) ? "" : "none", "important");
  });
});
</script>'''
t = re.sub(r'<script>\s*var inp.*?</script>', '', t, flags=re.S)
t = t.replace("</body>", js + "\n</body>")
p.write_text(t, encoding="utf-8")
print("DONE - search moved up")
