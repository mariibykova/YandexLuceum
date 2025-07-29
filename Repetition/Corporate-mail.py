n = int(input())
a = [input() for _ in range(n)]
 
m = int(input())
names = [input() for _ in range(m)]
 
for el in names:
    i = ""
    while True:
        em = f"{el}{i}@untitled.py"
        if em not in a:
            a.append(em)
            print(em)
            break
        i = i + 1 if i else 1

