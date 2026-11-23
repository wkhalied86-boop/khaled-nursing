t = open('make4.py', encoding='utf-8').read().splitlines()
out = []
buf = ""
for line in t:
    buf += line + " "
    # لو عدد علامات التنصيص زوجي يبقى السطر سليم
    if buf.count('"') % 2 == 0:
        out.append(buf.rstrip())
        buf = ""
    # لو فردي يبقى السطر مكسور، كمل جمعه مع اللي بعده
if buf:
    out.append(buf)
open('make4.py','w',encoding='utf-8').write("\n".join(out))
print("fixed", len(out), "lines")
