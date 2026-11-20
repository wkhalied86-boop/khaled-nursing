import glob, os, re
cats=["التعريف والتشريح","الوظيفة وكيف يعمل","الأمراض والمشاكل","الوقاية والعلاج","الغذاء الصحي","الرياضة والحياة اليومية","حقائق مدهشة","أسئلة شائعة","قصص وأمثلة","مراجعة وامتحان"]
for f in glob.glob("site/lessons/*_pages/page-*.html"):
 t=open(f,encoding="utf-8").read()
 m=re.search(r"page-(\d+)",f)
 i=int(m.group(1))
 nm=re.search(r"<h1>(.*?)</h1>",t)
 name=nm.group(1) if nm else "الدرس"
 cat=cats[(i-1)//10]
 title=f"{cat} - جزء {(i-1)%10+1}"
 body=f"<h1>{name}</h1><h2>📖 صفحة {i} / 100 - {title}</h2><h3>ما هو {cat} في {name}؟</h3><p>{name} عضو مهم جدا في جسمك، وفي هذه الصفحة هنتكلم بالتفصيل عن {cat}. {name} بيشتغل طول اليوم من غير توقف، ولو فهمت {cat} هتعرف تحافظ عليه.</p><h3>الشرح بالتفصيل</h3><p>أول حاجة لازم تعرفها أن {name} ليه دور أساسي في حياتك. مثلا، لما تاكل، لما تجري، لما تنام، {name} بيكون شغال وبيساعد باقي الجسم. العلماء اكتشفوا أن الاهتمام بـ {cat} بيخلي {name} أقوى وأصح.</p><h3>مثال من حياتك</h3><p>تخيل أنك صحيت الصبح ونشيط، ده معناه أن {name} شغال كويس. لكن لو أهملت أكلك ونومك، {name} هيتعب، وهتحس بالتعب. عشان كده لازم تطبق اللي في الصفحة دي كل يوم.</p><h3>نصيحة مهمة</h3><p>✅ اشرب مياه كتير ✅ كل خضار وفاكهة ✅ نام 8 ساعات ✅ ابعد عن السكريات والتدخين ✅ اتحرك كل يوم 30 دقيقة</p><h3>سؤال تفكر فيه</h3><p>ازاي تقدر تطبق اللي اتعلمته في صفحة {i} عن {name} في يومك النهاردة؟ اكتب 3 حاجات هتعملها.</p><br><div style='display:flex;justify-content:space-between'><a href='page-{i-1}.html'>⬅ السابق</a><a href='../../{os.path.basename(os.path.dirname(f)).replace('_pages','')}.html'>🏠 القائمة</a><a href='page-{i+1}.html'>التالي ➡</a></div>"
 h=f"<html><head><meta charset='utf-8'><title>{name} - {i}</title></head><body style='font-family:sans-serif;padding:20px;max-width:700px;margin:auto'>{body}</body></html>"
 open(f,"w",encoding="utf-8").write(h)
print("FILLED ALL")
