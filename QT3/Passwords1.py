lang = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
        'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
sla = set(''.join(lang))
sua = set(''.join(lang).upper())
na = set('1234567890')
 
 
def pass_is_valid(psw):
    spsw = set(psw)
    if not (spsw & sla and spsw & sua and spsw & na and len(psw) > 8):
        return 'error'
    for c in range(len(psw) - 2):
        psw_ = psw[c:c + 3].lower()
        for i in lang:
            if psw_ in i:
                return 'error'
    return 'ok'
 
 
print(pass_is_valid(input()))