qs=[
("يعني ايه طوارئ؟","اي موقف خطر بيهدد حياة الشخص ولازم نتصرف بسرعة قبل الاسعاف."),
("اول حاجة اعملها ايه؟","اهدى، أمن المكان، اتصل بالاسعاف 123، ساعد المصاب."),
("ايه هي الدقائق الذهبية؟","اول دقايق بعد الحادث، تصرفك الصح فيها ينقذ حياة المصاب."),
("اقول ايه للاسعاف؟","مكانك، ايه اللي حصل، كام مصاب، بيتنفس ولا لا."),
("ايه قاعدة ABC؟","A: مجرى الهواء - B: التنفس - C: النبض والنزيف."),
("النزيف اعمل ايه؟","اضغط على الجرح بقماش نضيف، وارفع العضو لفوق."),
("الحروق اعمل ايه؟","ميه جارية باردة 10 دقايق، متحطش معجون ولا زيت."),
("حد اتخنق اعمل ايه؟","خليه يكح، لو مش قادر يتنفس اعمل هيمليك."),
("حد اغمى عليه اعمل ايه؟","نيمه وارفع رجليه، ولو مفاقش اتصل بالاسعاف."),
("الكسر اعمل ايه؟","متحركش العضو، ثبته، وحط تلج بقماش."),
("انخفاض السكر اعمل ايه؟","لو واعي اديله عصير، لو مش واعي متحطش حاجة في بقه."),
("ضربة الشمس اعمل ايه؟","انقله لمكان بارد، كمادات باردة، واتصل بالاسعاف."),
]
a="<html dir=rtl><head><meta charset=utf-8>"
b="<style>body{font-family:system-ui;max-width:700px;margin:auto;padding:15px}"
c=".card{border:1px solid #333;border-radius:12px;padding:14px;margin:12px 0;break-inside:avoid}"
d=".no-print{display:block;margin:15px auto;padding:12px 25px;font-size:18px;background:#111;color:#fff;border:none;border-radius:10px}"
e="@media print{.no-print{display:none!important}.card{border:1px solid #000!important}}</style></head><body>"
f="<button class=no-print onclick='window.print()'>اطبع الدرس</button>"
g="<a class=no-print href='../index.html'>رجوع</a><h1>درس 6 - الطوارئ</h1>"
h=a+b+c+d+e+f+g
for i,(q,ans) in enumerate(qs,1):
 h+=f"<div class=card><h3>{i}- {q}</h3><p>{ans}</p></div>"
h+="</body></html>"
open('lessons/lesson-6.html','w',encoding='utf-8').write(h)
print('DONE PRINTABLE')
