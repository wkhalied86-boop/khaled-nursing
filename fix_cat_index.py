import pathlib, re
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
# امسح onclick القديم بتاع الأيقونات
t = re.sub(r' onclick="var txt=this\.textContent.*?"', '', t)
onclick = '''onclick="var cats=[...new Set([...document.querySelectorAll('.card')].map(function(c){return c.getAttribute('data-cat')}))];var idx=parseInt(this.getAttribute('data-ci')||'0');var target=cats[idx];document.querySelectorAll('.cat-btn').forEach(function(x){x.classList.remove('active')});this.classList.add('active');document.querySelectorAll('.card').forEach(function(c){c.style.setProperty('display',c.getAttribute('data-cat')===target?'':'none','important')});window.scrollTo({top:document.querySelector('.grid').offsetTop-20,behavior:'smooth'})"'''
t = t.replace('class="cat-btn"', 'class="cat-btn" ' + onclick)
t = t.replace('class="cat-btn active"', 'class="cat-btn active" ' + onclick)
p.write_text(t, encoding="utf-8")
print("DONE INDEX", t.count("data-ci"))
