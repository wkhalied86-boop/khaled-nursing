import re
h=open('site/index.html',encoding='utf-8').read()
# شيل البانر التاني المكرر من أول <div class=head> لحد قبل أول <h2
h=re.sub(r"<div class=head>.*?</div></div>", "<div style='padding:10px 12px;background:#0a1a3a'><div class=search><input id=s placeholder=\"ابحث ... الحمل، القلب، الإسعافات\"><button onclick=doSearch()>بحث 🔍</button></div></div>", h, count=1, flags=re.S)
open('site/index.html','w',encoding='utf-8').write(h)
print('fixed')
