def ss(k):
    if k < 10:
        return k
    else:
        return k % 10 + ss(k // 10)
        

h = list(map(int, input().split(" ")))
m = list(map(int, input().split(" ")))
r = []
for a in h:
    sa = ss(a)
    for b in m:
        if sa != ss(b):
            r.append((a, b))
for (x, y) in sorted(r):
    print('%02d:%02d' % (x, y))
