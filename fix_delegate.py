import pathlib, re
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
# امسح سكربت applyFilter القديم
t = re.sub(r'<script>\s*var inp = document\.getElementById\("searchInput"\).*?</script>', '', t, flags=re.S)
js = '''<script>
document.addEventListener("click", function(e){
  var b = e.target.closest(".cat-btn");
  if(!b) return;
  var txt = b.textContent.trim();
  document.querySelectorAll(".cat-btn").forEach(function(x){ x.classList.remove("active"); });
  b.classList.add("active");
  var inp = document.getElementById("searchInput");
  if(inp) inp.value = "";
  if(txt.includes("الكل") || txt.toLowerCase().includes("all")){
    document.querySelectorAll(".card").forEach(function(c){ c.style.setProperty("display","","important"); });
    return;
  }
  var q = txt.toLowerCase();
  document.querySelectorAll(".card").forEach(function(c){
    var cat = (c.getAttribute("data-cat")||"").toLowerCase();
    var txtc = c.textContent.toLowerCase();
    var show = cat.includes(q)  q.includes(cat)  txtc.includes(q);
    c.style.setProperty("display", show ? "" : "none", "important");
  });
});
document.addEventListener("input", function(e){
  if(e.target.id !== "searchInput") return;
  var q = e.target.value.trim().toLowerCase();
  document.querySelectorAll(".card").forEach(function(c){
    var txt = (c.textContent+" "+(c.getAttribute("data-key")"")+" "+(c.getAttribute("data-cat")"")).toLowerCase();
    c.style.setProperty("display", (!q || txt.includes(q)) ? "" : "none", "important");
  });
});
console.log("DELEGATE READY");
</script>'''
t = t.replace("</body>", js + "\n</body>")
p.write_text(t, encoding="utf-8")
print("DONE DELEGATE")
