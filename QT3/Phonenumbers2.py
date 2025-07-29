class WrongNumber(Exception):
    pass
 
 
open = ["[", "{", "("]
close = ["]", "}", ")"]
 
 
def check(mystr):
    st = []
    for i in mystr:
        if len(st) > 1:
            return False
        if i in open:
            st.append(i)
        elif i in close:
            pos = close.index(i)
            if ((len(st) > 0) and
                    (open[pos] == st[len(st) - 1])):
                st.pop()
            else:
                return False
    if len(st) == 0:
        return True
 
 
s = ['1', '0', '2', "3", "4", "5", "6", "7", "8", '9']
 
aa = input()
try:
    aa = aa.strip()
    aa = aa.replace(' ', "")
    aa = aa.replace("\t", '')
    if not (aa.startswith("+7") or aa.startswith("8")):
        raise WrongNumber
    if aa.startswith("-") or aa[-1] == ("-"):
        raise WrongNumber
    if "--" in aa:
        raise WrongNumber
    if aa[0] == "8":
        u = aa[1:]
        aa = '+7' + u
    if "-" in aa:
        aa = aa.replace('-', "")
    if not check(aa):
        raise WrongNumber
    aa = aa.replace('(', "")
    aa = aa.replace(')', "")
    for el in aa[1:]:
        if el not in s:
            raise WrongNumber
    if len(aa) != 12:
        raise WrongNumber
    print(aa)
except WrongNumber:
    print("error")