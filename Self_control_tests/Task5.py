'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное
число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.В качестве ответа прикрепите файл с
полученными данными о среднем росте.

Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153

Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
'''

num = 1
clas = {}
#keys = range(1, 12)
values = ['-','-','-','-','-','-','-','-','-','-','-']
#d = dict(zip(keys,values))
# for k, v in d.items():
#     print((k), *v)

with open('in.txt', encoding='utf-8') as tbl:
    for l in tbl:
        s = l.strip().split('\t')
        if s[0] not in clas:
            clas[s[0]] = [int(s[2]), num]
        elif s[0] in clas:
            clas[s[0]][0] += int(s[2])
            clas[s[0]][1] += 1

for k, v in clas.items():
    values[int(k)-1] = v[0]/v[1]
#print(values)