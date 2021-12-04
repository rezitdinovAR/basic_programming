#Вариант 4
'''
 4. Задан граф в виде количества вершин n<=7,
 количества ребер k<=28 и матрицы инцидентности.
 а) Для каждой вершины напечатать список инцидентных ей ребер.
б) Определить степень каждой вершины графа.
в) Проверить, есть ли вершины со степенью 0.
г) Определить число вершин, инцидентных только одному ребру.
д) Определить наибольшее число смежных между собой ребер,
инцидентных одной и той же вершине.
е) Проверить, есть ли в графе петли.
'''

n = int(input('Введите колво вершин: '))
k = int(input('Введите колво ребер: '))
I = [[0] * k for _ in range(n)]
friends = {}
peak_degree = {}
nul_degree = False
oneLove = []
loopCheck = False
max_degree = 0
for i in range(n):
    I[i] = [int(x) for x in input().split()]
    friends[i] = set()
    peak_degree[i] = 0
for i in range(n):
    for j in range(k):
        if I[i][j]:
            for i_1 in range(i, n):
                if I[i_1][j]:
                    friends[i].add(j)
    if sum(I[i]) > max_degree:
        max_degree = sum(I[i])
for friend in friends:
    peak_degree[friend] = len(friends[friend])
    if not friends[friend]:
        nul_degree = True
    if len(friends[friend]) == 1:
        oneLove.append(friend)
for i in range(k):
    summa=0
    for j in range(n):
        summa+=I[j][i]
    if summa==1:
        loopCheck=True
print(f'а) Для каждой вершины напечатать список инцидентных ей ребер: {friends}')
print(f'б) Определить степень каждой вершины графа: {peak_degree}')
print(f'в) Проверить, есть ли вершины со степенью 0: {nul_degree}')
print(f'г) Определить число вершин, инцидентных только одному ребру: {len(oneLove)}')
print(f'д) Определить наибольшее число смежных между собой ребер, инцидентных одной и той же вершине: {max_degree}')
print(f'е) Проверить, есть ли в графе петли: {loopCheck}')