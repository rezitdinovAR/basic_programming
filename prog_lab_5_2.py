from openpyexcel import load_workbook
import heapq as hq
def read_file():
    wb=load_workbook(filename='map1.xlsx',read_only=True)
    ws=wb['Лист1']
    return ws
def get_graph():
    ws=read_file()
    inf=float('Inf')
    _len=0
    G=[]
    for i in range(16):
        _str=[]
        for i in range(16):
            _str.append(0)
        G.append(_str)
    i, j=0, 0
    for row in ws.rows:
        for cell in row:
            if i!=0 and j!=0:
                if cell.value:
                    G[i-1][j-1]=cell.value
                else:
                    G[i - 1][j - 1]=inf
            j += 1
        i += 1
        j=0
    return G
'''for stroka in G:
        print(stroka)
get_graph()'''
def dijkstra(G,s):
    inf = float('Inf')
    n=len(G)
    Q=[(0,s)]
    d=[inf for i in range(n)]
    d[s]=0
    while len(Q)!=0:
        (cost,u)=hq.heappop(Q)
        for v in range(n):
            if d[v]>d[u]+G[u][v]:
                d[v]=d[u]+G[u][v]
                Q.append((d[v],v))
    return d
slv={
    'Маркарт': 0,
    'Картвастен': 1,
    'Драконий мост': 2,
    'Солитьюд': 3,
    'Морфал': 4,
    'Рорикстед': 5,
    'Вайтран': 6,
    'Данстар': 7,
    'Винтерхолд': 8,
    'Виндхельм': 9,
    'Камень Шора': 10,
    'Рифтен': 11,
    'Айрвастед': 12,
    'Хелген': 13,
    'Фолкрит': 14,
    'Ривервуд': 15
}
slvmas=['Маркарт','Картвастен','Драконий мост','Солитьюд','Морфал','Рорикстед','Вайтран','Данстар','Винтерхолд','Виндхельм','Камень Шора','Рифтен','Айрвастед','Хелген','Фолкрит','Ривервуд']
punkts=[]
for key in slv:
    punkts.append(key)
print('Список всех пунктов:',punkts)
start=slv[input('Введите название пункта для рассчёта кратчайших расстояний')]
G=get_graph()
d=dijkstra(G,start)
new_slv={}
for i in slvmas:
    new_slv[i]=d[slvmas.index(i)]
print(new_slv)
def getPath(f):
    global d
    n=len(get_graph())
    path=[f]
    while f!=start:
        for v in range(n):
            if d[v]==d[f]-G[f][v]:
                path.append(v)
                f=v
    path=path[::-1]
    way=[]
    for i in path:
        way.append(slvmas[i])
    return way
f=input('Введите название пункта для восстановления пути')
print(getPath(slv[f]),'Кратчайшее расстояние:',new_slv[f])