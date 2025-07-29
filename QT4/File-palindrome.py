def palindrome():
    with open("input.dat", "rb") as f:
        f1 = f.read()
    return f1 == f1[::-1]