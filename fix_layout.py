import pathlib
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
css = """
<style id="fix-layout">
*{box-sizing:border-box!important}
html,body{overflow-x:hidden!important;max-width:100vw!important}
img{max-width:100%!important;height:auto!important}
header,.hero,.banner{max-width:100vw!important;overflow:hidden!important}
/* حاوية الأيقونات - 2 جنب بعض */
.categories,.cats,.cat-filter,.filters,.filter-bar,.cat-buttons{
  display:flex!important;flex-wrap:wrap!important;
  gap:8px!important;justify-content:center!important;
  width:100%!important;max-width:100%!important;
  padding:10px 8px!important;margin:0 auto!important;
}
/* كل زرار ياخد نص العرض - يعني 2 في الصف */
.cat-btn{
  flex:0 0 calc(50% - 6px)!important;
  max-width:calc(50% - 6px)!important;
  display:flex!important;align-items:center!important;justify-content:center!important;
  gap:6px!important;text-align:center!important;
  padding:10px 6px!important;font-size:14px!important;
  line-height:1.3!important;white-space:normal!important;
  word-break:break-word!important;border-radius:20px!important;
  min-height:44px!important;
}
.cat-btn.active{transform:none!important}
.grid,.cards{display:grid!important;grid-template-columns:1fr!important;gap:12px!important;width:100%!important;padding:0 8px!important}
.card{width:100%!important;max-width:100%!important;margin:0!important}
</style>
"""
if 'id="fix-layout"' in t:
    import re
    t = re.sub(r'<style id="fix-layout">.*?</style>', css, t, flags=re.S)
else:
    t = t.replace("</head>", css + "\n</head>")
p.write_text(t, encoding="utf-8")
print("DONE LAYOUT")
