#Вариант 4
def P(n, x):
    if n == 0: return 1
    if n == 1: return x

    return ( (2*n-1)*P(n-1, x) -(n-1)*P(n-2, x) )/n

n = int(input('n: '))
x = int(input('x: '))

print(P(n, x))

M=[1,x]
for i in range(2,n+10):
    M.append(( (2*i-1)*P(i-1, x) -(i-1)*P(i-2, x) )/i)
print(M[n])