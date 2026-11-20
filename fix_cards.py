import pathlib, re
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf-8")
css = """
<style id="fix-cards">
.grid,.cards,.lessons,.lesson-list{display:grid!important;grid-template-columns:1fr 1fr!important;gap:10px!important;padding:0 8px!important}
.card,.lesson-card,.lesson{
  padding:14px 10px!important;border-radius:18px!important;
  min-height:130px!important;display:flex!important;flex-direction:column!important;
  align-items:center!important;justify-content:center!important;text-align:center!important;
  gap:6px!important
}
.card h3,.card h2,.lesson-card h3{font-size:15px!important;line-height:1.4!important;margin:0!important}
.card p,.lesson-card p{font-size:12px!important;line-height:1.4!important;margin:0!important;opacity:.8}
.card .num,.lesson-card .num{width:32px!important;height:32px!important;font-size:15px!important;margin:0!important}
</style>
"""
if 'id="fix-cards"' in t:
    t = re.sub(r'<style id="fix-cards">.*?</style>', css, t, flags=re.S)
else:
    t = t.replace("</head>", css + "\n</head>")
p.write_text(t, encoding="utf-8")
print("DONE CARDS")
