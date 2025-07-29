import sys
 
count = 0
data = sys.stdin.readlines()
for i in data:
    words = i.lower()
    if 'алек' in words:
        count += 1
    else:
        continue
print(count)