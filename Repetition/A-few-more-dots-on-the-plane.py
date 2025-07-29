c = [input().split() for i in range(int(input()))]
for i in c:
    if abs(int(i[0])) != abs(int(i[1])) and abs(int(i[0])) > abs(int(i[1])):
        print(f'({i[0]}, {i[1]})')

min_x = min(c, key=lambda x: int(x[0]))
max_x = max(c, key=lambda x: int(x[0]))
max_y = max(c, key=lambda x: int(x[1]))
min_y = min(c, key=lambda x: int(x[1]))


print(f'left: ({min_x[0]}, {min_x[-1]})')
print(f'right: ({max_x[0]}, {max_x[-1]})')
print(f'top: ({max_y[0]}, {max_y[-1]})')
print(f'bottom: ({min_y[0]}, {min_y[-1]})')