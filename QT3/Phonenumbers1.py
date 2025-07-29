def check(s: str):
    s = ''.join(s.split())
    f1 = s.startswith('+7') or s.startswith('8')
    f2 = all(s.split('-'))
    f3 = (s.count('(') == 1 and s.count(')') == 1 and
          s.find('(') < s.find(')'))
    f4 = s.count('(') == 0 and s.count(')') == 0
    if f1 and f2 and (f3 or f4):
        for c in '()-':
            s = s.replace(c, '')
        if s.startswith('8'):
            s = '+7' + s[1:]
        if s[1:].isdigit() and len(s) == 12:
            return s
        else:
            return 'error'
    else:
        return 'error'
 
 
if __name__ == '__main__':
    print(check(input()))