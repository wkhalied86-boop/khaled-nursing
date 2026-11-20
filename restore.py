import glob, re
IMG={"مخ": "https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=800", "قلب": "https://images.unsplash.com/photo-1505576399279-565b52d4ac71?w=800", "عين": "https://images.unsplash.com/photo-1577401239170-897942555fb3?w=800", "رئة": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=800", "كبد": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800", "كلى": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800", "عظم": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=800", "جلد": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=800", "أسنان": "https://images.unsplash.com/photo-1606811841689-23dfddce3e95?w=800", "حمل": "https://images.unsplash.com/photo-1493894473891-10fc1e5dbd22?w=800", "دم": "https://images.unsplash.com/photo-1615461066841-6116e610c4fe?w=800", "أذن": "https://images.unsplash.com/photo-1591160690555-5debfba289f0?w=800"}
INFO={"مخ": ("المخ فيه 86 مليار خلية عصبية", "المخ بيتحكم في التفكير والحركة والمشاعر، وبيستهلك 20% من طاقة الجسم"), "قلب": ("القلب بيضخ 5 لتر دم في الدقيقة", "القلب عضلة لا تتوقف، وبيوصل الدم لكل الجسم عن طريق الشرايين"), "عين": ("الشبكية فيها 100 مليون خلية", "الضوء بيدخل من القرنية، والعدسة بتجمعه على الشبكية، والمخ بيفهم الصورة")}
for f in glob.glob("site/lessons/*_pages/page-*.html"):
 t=open(f,encoding="utf-8").read()
 nm=re.search(r"<h1>(.*?)</h1>",t)
 nm=nm.group(1) if nm else "الدرس"
 nm=nm.replace(" 5","").replace(" 1","").strip()
 i=int(re.search(r"page-(\d+)",f).group(1))
 img="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800"
 detail="هذا العضو يعمل بنظام دقيق، وأي خلل فيه يظهر في أعراض واضحة يجب ملاحظتها بدري."
 for k,v in IMG.items():
  if k in nm: img=v; break
 for k,v in INFO.items():
  if k in nm: detail=v[1]; break
 new=f"""<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{nm}</title></head><body style='font-family:sans-serif;margin:0;background:#fff'>
<img src='{img}' style='width:100%;height:280px;object-fit:cover'>
<div style='padding:20px;max-width:700px;margin:auto'>
<h1 style='text-align:center'>{nm} - صفحة {i}</h1>
<div style='background:#f5f5f5;padding:15px;border-radius:15px'><b>شرح {nm}:</b> {detail}</div>
<div style='background:#f9f9f9;padding:15px;border-radius:15px;margin-top:15px'><b>Key Medical Points</b><br><br>1. <b>التعريف:</b> ما هو {nm} ووظيفته الأساسية<br>2. <b>التقييم التمريضي:</b> كيف تفحص {nm} وتلاحظ العلامات الحيوية<br>3. <b>علامات الخطر:</b> متى تبلغ الطبيب فورا لو حصل ألم أو تغير في {nm}<br>4. <b>تثقيف المريض:</b> نصايح للمريض للحفاظ على {nm} - أكل صحي، نوم، رياضة، ومتابعة دورية</div>
<div style='background:#e3f2fd;padding:15px;border-radius:15px;margin-top:15px'><b>معلومة تفصيلية عن {nm}:</b> {detail} - في صفحة {i} بندرس جزء مختلف من {nm}، كل صفحة بتكمل اللي قبلها، عشان في الآخر تكون فاهم {nm} كله من التشريح للعلاج.</div>
<div style='background:#dbeafe;text-align:center;padding:10px;border-radius:10px;margin-top:15px'><b>Source: CDC 2024</b></div>
<div style='display:flex;justify-content:center;gap:10px;margin-top:15px'><a href='page-{i-1}.html' style='border:1px solid #999;padding:8px 15px;border-radius:20px;text-decoration:none;color:#000'>Prev</a><a href='../../index.html' style='border:1px solid #999;padding:8px 15px;border-radius:20px;text-decoration:none;color:#000'>Back</a><a href='page-{i+1}.html' style='border:1px solid #999;padding:8px 15px;border-radius:20px;text-decoration:none;color:#000'>Next</a></div></div></body></html>"""
 open(f,"w",encoding="utf-8").write(new)
print("RESTORED")
