a = input()
b = input()
if a == b:
    print('ничья')
elif a == 'камень' and b == 'ножницы':
    print('первый')
elif a == 'ножницы' and b == 'бумага':
    print('первый')
elif a == 'бумага' and b == 'камень':
    print('первый')
elif a == 'камень' and b == 'бумага':
    print('второй')
elif a == 'бумага' and b == 'ножницы':
    print('второй')
elif a == 'ножницы' and b == 'камень':
    print('второй')
