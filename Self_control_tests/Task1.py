'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на
стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:

Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:

Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
'''
i = 0
n = 3
with open('in.txt', encoding='utf-8') as inf:
     while i < n:
         s = inf.readline().strip().split(';')
         i += 1
         print(s)

