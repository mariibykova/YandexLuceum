a = []
st = {"I": 0, "II": 0, "III": 0, "IV": 0}
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        st["I"] += 1
    elif x < 0 and y > 0:
        st["II"] += 1
    elif x < 0 and y < 0:
        st["III"] += 1
    elif x > 0 and y < 0:
        st["IV"] += 1
    else:
        a.append((x, y))
 
for i in a:
    print(i)
print(*[f"{x}: {y}" for x, y in st.items()], sep=", ", end='.')