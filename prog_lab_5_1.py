'''Задание 1. Создайте текстовый файл in.txt, в который поместите текст
(объёмом примерно 0,5 страницы). Затем ваша программа должна считать
данные из файла, выполнить операции в соответствии с вариантом. Результат
нужно записать в текстовый файл out.txt
1)Посчитать сколько раз в тексте встречается заданное слово
2)Заменить заданное слово на другое по всему тексту
3)Подсчёт целых чисел в тексте
4)Удалить из текста лишние пробелы
5)Удалить все вхождения заданного слова из текста
6)Кол-во слов начинающихся с А
7)Кол-во слов начинающихся с и
8)Кол-во слов содержащих слог ло
9)Подсчитать кол-во открывающих и закрывающих скобок
10)Удалить последовательности символов заключённые в фигурные скобки
11)Определить наибольшее число подряд идущих одинаковых символов
12)Определить, каких символо больше: цифр или латинских букв'''
import re
with open('in.txt','r',encoding='utf-8') as s:
    s=s.read()

text=re.sub(r'[^\w\s]','', s)
word_mas=text.split(' ')
def count_word():
    word = input('введите слово чтобы узнать сколько раз оно встречается')
    return word_mas.count(word)
text_mas=s.split(' ')
def change_inword():
    outword, inword = map(str, input('введите два слова через пробел, чтобы заменить первое на второе ').split())
    for i in range(len(text_mas)):
        o=text_mas[i]
        if outword in text_mas[i]:
            if  len(word_mas[i])-len(outword)>0:
                pass
            else:
                text_mas[i]=o.replace(outword,inword)
    s=''
    for i in text_mas:
        s+=i+' '
    s=s[:-1]
    return s
def count_integer(word_mas):
    count=0
    for i in range(len(word_mas)):
        o=word_mas[i]
        if len(o)>0:
            if o[0].isdigit():
                if int(word_mas[i])==float(word_mas[i]):
                    count+=1
                else:
                    pass
    return count
def delete_spaces(s):
    s=s.split(' ')
    ss=''
    for i in range(len(s)):
        ss+=s[i]+' '
    return ss


def delete_inword():
    inword=input('Введите слово которое нужно удалить')
    for i in range(len(text_mas)):
        o=text_mas[i]
        if inword in o:
            if len(o)-len(inword)>1:
                pass
            else:
                text_mas[i]=o.replace(inword,'')
    s=''
    for i in text_mas:
        s+=i+' '
    s=s[:-1]
    return s
def count_stfA(word_mas):
    count=0
    for i in word_mas:
        if len(i)>0:
            if i[0]=='А':
                count+=1
            else:
                pass
    return count
def count_stfI(word_mas):
    count = 0
    for i in word_mas:
        if len(i) > 0:
            if i[0] == 'и':
                count += 1
            else:
                pass
    return count
def countlo(word_mas):
    count=0
    for i in word_mas:
        count+=(i.count('ло')+i.count('Ло'))
    return count
def count_skb(s):
    return s.count(')')+s.count('(')
def delete_psl(s):
    while s.count('{')>0:
        s=s[:s.index('{')]+s[s.index('}')+1::]
    return s
def count_maxi(s):
    max_count=0
    for i in range(1,len(s)):
        count=1
        if s[i-1]==s[i]:
            count+=1
        else:
            if count>max_count:
                max_count=count
            else:
                pass
    return max_count
def opr_wicthOne(s):
    bukvi='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    countC=0
    countB=0
    for i in s:
        if i.isdigit():
            countC+=1
        if i in bukvi:
            countB+=1
    if countC>countB:
        return 'Цифр больше'
    if countB<countC:
        return 'Латинских букв больше'
    if countB==countC:
        return 'Поровну'
otv={
    '1':count_word(),
    '2':change_inword(),
    '3':count_integer(word_mas),
    '4':delete_spaces(s),
    '5':delete_inword(),
    '6':count_stfA(word_mas),
    '7':count_stfI(word_mas),
    '8':countlo(word_mas),
    '9':count_skb(s),
    '10':delete_psl(s),
    '11':count_maxi(s),
    '12':opr_wicthOne(s)
}
with open('out.txt','w',encoding='utf-8') as f:
    for key in otv:
        f.write(f'{key}: {otv[key]}\n')