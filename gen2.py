cats=[
("Pregnancy","الحمل","p1"),
("Nursing","التمريض","p2"),
("Heart","القلب","p3"),
]
import json
h=open("index.html","w")
h.write("<html><head>")
h.write("<meta charset=utf-8>")
h.write("<meta name=viewport ")
h.write("content='width=device-width'>")
h.write("<style>body{margin:0}")
h.write("header{background:#0b3d91;")
h.write("color:#fff;padding:14px}")
h.write(".card{background:#fff;")
h.write("border-radius:12px}</style>")
h.write("</head><body>")
h.write("<header><h2>Khaled</h2>")
h.write("<select id=lang>")
h.write("<option value=EN>English</option>")
h.write("<option value=AR>العربية</option>")
h.write("<option value=FR>Francais</option>")
h.write("<option value=ES>Espanol</option>")
h.write("<option value=DE>Deutsch</option>")
h.write("<option value=TR>Turkce</option>")
h.write("<option value=HI>Hindi</option>")
h.write("<option value=UR>Urdu</option>")
h.write("<option value=RU>Russian</option>")
h.write("<option value=PT>Portugues</option>")
h.write("</select></header>")
h.write("<div id=home></div>")
h.write("<div id=detail></div>")
L=[]
for c in cats:
 for n in range(1,11):
  img="https://picsum.photos/seed/"
  img+=c[0]+str(n)+"/600/400"
  L.append([c[0],c[1],n,img])
for c in cats:
 h.write("<h2>"+c[0]+" - "+c[1]+"</h2>")
 for x in L:
  if x[0]==c[0]:
   h.write("<div class=card>")
   h.write("<img src="+x[3]+">")
   h.write("<details><summary>")
   h.write(x[0]+" "+str(x[2]))
   h.write("</summary><p>Lesson ")
   h.write(str(x[2])+" about "+x[0])
   h.write(". Check vitals, safety.")
   h.write("</p><p>Source: WHO 2024")
   h.write("</p></details></div>")
h.write("</body></html>")
h.close()
print("done")
