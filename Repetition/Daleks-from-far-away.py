import sys
 
a, k = [i.lower().replace('.', '').split() for i in list(map(str.strip, sys.stdin))], 0
for i in a:
    for g in i:
        if 'далек' in g:
            if g.index('далек') == 0:
                k += 1
                break
print(k)