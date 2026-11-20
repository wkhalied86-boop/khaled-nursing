import glob
code='<div id="google_translate_element" style="position:fixed;top:5px;left:5px;z-index:9999;background:white;padding:5px;border-radius:10px"></div><script>function googleTranslateElementInit(){new google.translate.TranslateElement({pageLanguage:"ar",includedLanguages:"ar,en,de,fr,es,it,tr,ru,hi,zh-CN"},"google_translate_element")}</script><script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>'
for f in glob.glob("site/lessons/**/*.html",recursive=True):
 t=open(f,encoding="utf-8").read()
 if "google_translate" not in t:
  t=t.replace("<body",code+"<body",1)
  open(f,"w",encoding="utf-8").write(t)
print("FIXED")
