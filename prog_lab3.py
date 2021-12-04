#Вариант 8
import random

"""st=input('Введите строку')
a=len(st)
strN=st.split(' ')
b=len(strN)
def findSmth(st):
    maxS=0
    minS=100000000000000000000000000000000
    for i in st:
        if len(i)>maxS:
            maxS=len(i)
        if len(i)<minS:
            minS=len(i)
    return maxS, minS
st=st.replace('*','')
print(a,b,findSmth(strN),st)"""

A=[]
for i in range(random.randint(10,20)):
    A.append(random.randint(-100,100))
print(A)
def sort2(A):
    B=[]
    C=[]
    for i in range(1,len(A)):
        if A[i]>0 and i%2==1:
            B.append(A[i])
        else:
            C.append(A[i])
    B.extend(C)
    return B
print(sort2(A))

P=[]
for i in range(random.randint(10,20)):
    P.append(random.randint(1,5))
print(P)
def sort3(P):
    K=[]
    for i in P:
        if K.count(i)==0:
            K.append(i)
    return K
print(sort3(P))

n=int(input('Введите число n'))
simpArr=[]
Arr7=[]
for i in range(2,n+1):
    simpArr.append(i)
    if i%7==0:
        Arr7.append(i)
def findSimp(simpArr,i):
    p = simpArr[i]
    for j in simpArr[i+1::]:
        if j%p==0:
            simpArr.remove(j)
    return simpArr
i=0
while i<len(simpArr)-1:
    findSimp(simpArr,i)
    i+=1
ArrS=[1]
ArrS.extend(simpArr)
print(Arr7)
print(ArrS)

a1,a2=map(int,input("Введите кол-во строк и столбоцов матрицы через пробел").split())
sr=[]
for j in range(a1):
    st=[]
    for i in range(a2):
        st.append(random.randint(-100,100))
    sr.append(sum(st)/len(st))
    print(st)
print('Средние значения для каждой строки',sr)
print('==================================')
elMax=0
b1=0
b2=0
b3=0
for i in range(3):
    sl=[]
    for j in range(5):
        st=[]
        for k in range(7):
            a=random.randint(-100,100)
            st.append(a)
            if a>elMax:
                elMax=a
                b1=i
                b2=j
                b3=k
        print(st)
    print('-----------------------------')
print(elMax, [b1,b2,b3])