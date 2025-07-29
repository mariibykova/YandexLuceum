s = input().split(" -> ")
a = int(input())
 
for _ in range(a):
    p = input()
    i = s.index(p)
    otv = s[i - 1 if i > 0 else i:i + 2]
    print(*otv, sep=' -> ')
