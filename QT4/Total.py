f = open('prices.txt', mode='r')
a = f.readlines()

otv = 0 
for el in a:
    aa = el.split()
    otv += (float(aa[1]) * float(aa[2]))
print(otv)
