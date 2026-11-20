import glob, re
for lesson in sorted(glob.glob("site/lessons/*.html")):
 lt=open(lesson,encoding="utf-8").read()
 h=re.search(r"<h1>(.*?)</h1>",lt); nm=h.group(1) if h else "درس"
 body=f"""<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{nm}</title></head><body style='font-family:sans-serif;padding:20px;max-width:700px;margin:auto;background:#fff;text-align:center'>
<a href='../index.html'>🏠 القايمة</a>
<h1>{nm}</h1>
<div style='font-size:80px'>🩺</div>
<div style='background:#fff3cd;padding:20px;border-radius:20px;border:2px dashed #ffc107'>
<h2>📭 الأيقونة دي فاضية دلوقتي</h2>
<p>في انتظار موضوع <b>{nm}</b></p>
<p>ابعت موضوع {nm} وهنحط معلوماته هنا</p>
</div>
<h3 style='text-align:right'>📖 ما هو {nm}؟</h3><p style='text-align:right;color:#999'>... لسه فاضي - في انتظار موضوعك ...</p>
<h3 style='text-align:right'>🔍 أعراض {nm}</h3><p style='text-align:right;color:#999'>... لسه فاضي ...</p>
<h3 style='text-align:right'>👩‍⚕️ علاج ورعاية {nm}</h3><p style='text-align:right;color:#999'>... لسه فاضي ...</p>
<h3 style='text-align:right'>🏠 نصايح {nm}</h3><p style='text-align:right;color:#999'>... لسه فاضي ...</p>
<br><a href='../index.html' style='display:block;border:1px solid #999;padding:10px;border-radius:20px;text-decoration:none'>🏠 رجوع للقايمة</a>
</body></html>"""
 open(lesson,"w",encoding="utf-8").write(body)
 print(f"CLEARED {nm}")
print("ALL CLEARED - EMPTY NOW")
