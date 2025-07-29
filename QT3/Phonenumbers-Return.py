try:
    s = input().replace(" ", "").replace("\t", "")
    if "(" in s and ")" in s:
        ind = s.index("(")
        end = s.index(")")
        s = s[:ind] + s[ind + 1:end] + s[end + 1:]
 
    if "--" not in s and "-" in s:
        s = s[0] + s[1:-1].replace("-", "") + s[-1]
 
    if s.startswith("+7"):
        s = "+7" + s[2:]
    elif s.startswith("8"):
        s = "+7" + s[1:]
    else:
        raise TypeError()
 
    if not s[1:].isdigit():
        raise TypeError()
    if len(s[1:]) != 11:
        raise ValueError()
    print(s)
except ValueError:
    print("неверное количество цифр")
except TypeError:
    print("неверный формат")