import pathlib
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
onclick = '''onclick="var txt=this.textContent.trim();var q=txt.toLowerCase();document.querySelectorAll('.cat-btn').forEach(function(x){x.classList.remove('active')});this.classList.add('active');if(txt.includes('الكل')q.includes('all')){document.querySelectorAll('.card').forEach(function(c){c.style.setProperty('display','','important')});return}document.querySelectorAll('.card').forEach(function(c){var cat=(c.getAttribute('data-cat')'').toLowerCase();var tc=c.textContent.toLowerCase();var show=cat.includes(q)q.includes(cat)tc.includes(q);c.style.setProperty('display',show?'':'none','important')})"'''
if t.count('class="cat-btn"') > 0 and 'cat-btn\' onclick' not in t:
    t = t.replace('class="cat-btn"', 'class="cat-btn" ' + onclick)
    # اللي فيه active
    t = t.replace('class="cat-btn active"', 'class="cat-btn active" ' + onclick)
p.write_text(t, encoding="utf-8")
print("DONE CAT", t.count("cat-btn"))
