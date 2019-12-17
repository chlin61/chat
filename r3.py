lines=[]
with open('3.txt',encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
for line in lines:
    s = line.split()
    time = s[0][0:5]
    name = s[0][5:]
    message =''
    for m in s[1:]:
        message += m
    print(time, name, message)


