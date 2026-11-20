import glob
s='<select id=L onchange=T()><option value=ar>عربي<option value=en>English<option value=de>Deutsch<option value=fr>Francais<option value=es>Espanol<option value=it>Italiano<option value=tr>Turkce<option value=ru>Russian<option value=zh-CN>Chinese<option value=hi>Hindi</select><script>let O=null;async function T(){let l=document.getElementById("L").value,e=[...document.querySelectorAll("h1,.icon span,p")];if(!O)O=e.map(x=>x.innerText);if(l=="ar"){e.forEach((x,i)=>x.innerText=O[i]);return}let j=O.join(" | ");let r=await fetch("https://api.mymemory.translated.net/get?q="+encodeURIComponent(j)+"&langpair=ar|"+l);let d=await r.json();let t=d.responseData.translatedText.split(" | ");e.forEach((x,i)=>{if(t[i])x.innerText=t[i]})}</script>'
for f in ["site/index.html"]+glob.glob("site/lessons/*.html"):
 t=open(f,encoding="utf-8").read()
 if "id=L" not in t:
  t=t.replace("<body>","<body><div style='position:fixed;top:10px;left:10px;z-index:9999;background:#fff;padding:5px;border-radius:20px'>🌐"+s+"</div>",1)
  open(f,"w",encoding="utf-8").write(t)
print("OK")
