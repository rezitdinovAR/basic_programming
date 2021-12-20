#Вариант 9
import math
x,n=map(int,input('Введите x и n через пробел').split())
b=1
Summa_Ryada=b
for i in range(n):
    b=b*(((-1)*(x**2))/(2*i*(2*i-1)))
    Summa_Ryada+=b
print(Summa_Ryada)
def getPhrase():
    a=input("Введите фразу от 10 символов")
    if len(a)<10:
        return getPhrase()
    else:
        return a
a=input("Введите фразу от 10 символов")
if len(a)<10:
    getPhrase()
if len(a)%2!=0:
    print(a[:4],' ',a[len(a)-4::],' ',a[len(a)//2+1],' ',a[2:8])
else:
    print(a[:4],' ',a[len(a)-4::],' ','Длинна ряда чётная',' ',a[2:8:1])
str=input('Введите 6 целых чисел через запятую')
arr=[]
strN=str.split(',')
for i in strN:
    arr.append(int(i))
print(arr[3],' ',arr[::-1],' ',sum(arr)/6)
