import re
l1 = open("lessons/lesson-1.html", encoding="utf-8").read()
l10 = open("lessons/lesson-10.html", encoding="utf-8").read()

# خد الستايل من درس 1
m1 = re.search(r'<style>.*?</style>', l1, flags=re.S)
style1 = m1.group(0)
# حطه في درس 10 بدل الستايل القديم
l10_new = re.sub(r'<style>.*?</style>', style1, l10, flags=re.S, count=1)

# لو درس 10 فيه h2 خليه h3 زي درس 1
l10_new = l10_new.replace('<h2>', '<h3>').replace('</h2>', '</h3>')

open("lessons/lesson-10.html", "w", encoding="utf-8").write(l10_new)
print("done - style copied from lesson 1")
