import sys
 
a, k = [i.lower().replace('.', '').split() for i in list(map(str.strip, sys.stdin))], 0
a1 = ['далек', 'далека', 'далеку', 'далеком', 'далеке', 
      'далеки', 'далеков', 'далекам', 'далеками', 'далеках']
for i in a:
    for g in i:
        if 'далек' in g and g.index('далек') == 0:
            if g in a1:
                k += 1
                break
print(k)