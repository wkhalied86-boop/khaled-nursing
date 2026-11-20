import pathlib
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
# بحث inline - يشتغل حتى لو السكربت اللي تحت بايظ
old_inp = 'id="searchInput"'
new_inp = 'id="searchInput" oninput="var q=this.value.trim().toLowerCase();document.querySelectorAll(\'.card\').forEach(function(c){var txt=c.textContent.toLowerCase();c.style.setProperty(\'display\',(!q||txt.includes(q))?\'\':\'none\',\'important\')})"'
if 'oninput=' not in t:
    t = t.replace(old_inp, new_inp, 1)
p.write_text(t, encoding="utf-8")
print("DONE INLINE")
