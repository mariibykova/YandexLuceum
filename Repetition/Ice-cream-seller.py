menu = {}

for _ in range(int(input())):
    ice, pr = input().rsplit(maxsplit=1)
    menu[ice] = int(pr)
 
input()

order = [0]
for i in iter(input, "."):
    if i:
        ice, cnt = i.rsplit(maxsplit=1)
        order[-1] += menu[ice] * int(cnt)
    elif order[-1] != 0:
        order.append(0)
 
sum = 0
cnt = 1
for i, j in enumerate(order):
    if j != 0:
        sum += j
        print(cnt, ") ", j, sep="")
        cnt += 1
    
print("Итого:", sum)
