import math
def triangle(a,b):
    C=math.sqrt(a**2+b**2)
    P=a+b+C
    return C,P
print(triangle(3,4))
def rounds(r1,r2):
    S1=math.pi*(r1)**2
    S2=math.pi*(r2)**2
    S3=S1-S2
    return S1,S2,S3
print(rounds(3,2))
def candy(X,A,Y,B):
    chocolate=A/X
    toffee=B/Y
    difference=chocolate/toffee
    return chocolate,toffee,difference
print(candy(2,24,3,12))
def segments(A,B):
    return A//B
print(segments(10,3))
def number(a):
    sum=0
    mult=1
    while a>0:
        sum+=a%10
        mult*=a%10
        a=a//10
    return sum, mult
print(number(324))
def rev(a):
    a=str(a)
    a=a[::-1]
    return int(a)
print(rev(324))
def f(a):
    a=str(a)
    return int(a[1:]+a[0:1])
print(f(324))

