a= input('введите первое число: ')
b= input('введите второе число: ')
c= input('введите третье число: ')

if a==b==c:
    print(3)
elif a==b or b==c or c==a:
    print(2)
else:
    print(0)