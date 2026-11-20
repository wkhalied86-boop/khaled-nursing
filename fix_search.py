import pathlib
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
if "id=\"searchInput\"" not in t:
    search_html = '''<div style="max-width:700px;margin:14px auto;padding:0 12px"><input id="searchInput" type="text" placeholder="ابحث في الأقسام... 🔍" style="width:100%;padding:14px 16px;font-size:17px;border-radius:14px;border:2px solid #ddd;outline:none;text-align:right;direction:rtl"></div>'''
    t = t.replace('<div class="grid"', search_html + '\n<div class="grid"', 1)
    js = '''<script>
document.getElementById("searchInput").addEventListener("input", function(){
  var q = this.value.trim().toLowerCase();
  document.querySelectorAll(".card").forEach(function(c){
    var txt = (c.textContent + " " + (c.getAttribute("data-key")"") + " " + (c.getAttribute("data-cat")"")).toLowerCase();
    c.style.display = (!q || txt.includes(q)) ? "" : "none";
  });
  document.querySelectorAll(".cat-btn").forEach(function(b){
    var txt = b.textContent.toLowerCase();
    b.style.display = (!q || txt.includes(q)) ? "" : "none";
  });
});
</script>'''
    t = t.replace("</body>", js + "\n</body>")
    p.write_text(t, encoding="utf-8")
    print("DONE - search added")
else:
    print("already exists")
