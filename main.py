# # Общее задание
# # 1
# # линейный способ
# from sympy import *

# k, T, C, L = symbols("k C T L")
# C_ost = 100000
# Am_lst = []
# C_ost_lst = []
# for i in range(5):
#     Am = (C - L) / T
#     C_ost -= Am.subs({C: 100000, T: 5, L: 0})
#     Am_lst.append(round(Am.subs({C: 100000, T: 5, L: 0}), 2))
#     C_ost_lst.append(round(C_ost, 2))
# print("Am_lst:", Am_lst)
# print("C_ost_lst:", C_ost_lst)

# # 2
# # способ уменьшаемого остатка
# Aj = 0
# C_ost = 100000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(5):
#     Am = k * 1 / T * (C - Aj)
#     C_ost -= Am.subs({C: 100000, T: 5, k: 2})
#     Am_lst_2.append(round(Am.subs({C: 100000, T: 5, k: 2}), 2))
#     Aj += Am
#     C_ost_lst_2.append(round(C_ost, 2))
# print("Am_lst_2:", Am_lst_2)
# print("C_ost_lst_2", C_ost_lst_2)

# # Контейнер табличного вывода
# import pandas as pd

# Y = range(1, 6)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=["Y", "C_ost_lst", "Am_lst"])
# tfame2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_2", "Am_lst_2"])
# print(tfame)
# print(tfame2)

# # 3
# # линейный способ
# from sympy import *

# k, T, C, L = symbols("k T C L")
# C_ost = 30000
# Am_lst = []
# C_ost_lst = []
# for i in range(8):
#     Am = (C - L) / T
#     C_ost -= Am.subs({C: 30000, T: 8, L: 0})
#     Am_lst.append(round(Am.subs({C: 30000, T: 8, L: 0}), 2))
#     C_ost_lst.append(round(C_ost, 2))
# print("Am_lst:", Am_lst)
# print("C_ost_lst:", C_ost_lst)

# # способ уменьшаемого остатка
# Aj = 0
# C_ost = 30000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(8):
#     Am = k * 1 / T * (C - Aj)
#     C_ost -= Am.subs({C: 30000, T: 8, k: 2})
#     Am_lst_2.append(round(Am.subs({C: 30000, T: 8, k: 2}), 2))
#     Aj += Am
#     C_ost_lst_2.append(round(C_ost, 2))
# print("Am_lst_2:", Am_lst_2)
# print("C_ost_lst_2:", C_ost_lst_2)

# # Контейнер табличного вывода
# import pandas as pd

# Y = range(1, 9)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=["Y", "C_ost_lst", "Am_lst"])
# tfame2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_2", "Am_lst_2"])
# print(tfame)
# print(tfame2)

# # визуализация
# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot(tfame["Y"], tfame["C_ost_lst"], label="Am")
# plt.savefig("chart1.png")
# plt.plot(tfame2["Y"], tfame2["C_ost_lst_2"], label="Am2")
# plt.savefig("chart2.png")

# vals = Am_lst
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(
#     vals,
#     labels=labels,
#     autopct="%1.1f%%",
#     shadow=True,
#     explode=explode,
#     wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
#     rotatelabels=True,
# )
# ax.axis("equal")
# plt.savefig("chart3.png")

# vals = Am_lst_2
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(
#     vals,
#     labels=labels,
#     autopct="%1.1f%%",
#     shadow=True,
#     explode=explode,
#     wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
#     rotatelabels=True,
# )
# ax.axis("equal")
# plt.savefig("chart4.png")
# plt.clf()

# plt.figure()
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tframe = pd.DataFrame(table1, columns=["Y", "Am_lst"])
# tframe2 = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
# plt.bar(tfame["Y"], tfame["Am_lst"])
# plt.savefig("chart5.jpeg")
# plt.figure()
# plt.bar(tfame2["Y"], tfame2["Am_lst_2"])
# plt.savefig("chart6.jpeg")

# # Индивидуальное задание - Вариант 6
# from sympy import *
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# # 1. Контейнер расчета
# # линейный способ
# k, T, C, L = symbols("k C T L")
# C_ost = 15000
# Am_lst = []
# C_ost_lst = []
# for i in range(8):
#     Am = (C - L) / T
#     C_ost -= Am.subs({C: 15000, T: 8, L: 0})
#     Am_lst.append(round(Am.subs({C: 15000, T: 8, L: 0}), 2))
#     C_ost_lst.append(round(C_ost, 2))
# print("Am_lst:", Am_lst)
# print("C_ost_lst:", C_ost_lst)

# # способ уменьшаемого остатка
# Aj = 0
# C_ost = 15000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(8):
#     Am = k * 1 / T * (C - Aj)
#     C_ost -= Am.subs({C: 15000, T: 8, k: 2})
#     Am_lst_2.append(round(Am.subs({C: 15000, T: 8, k: 2}), 2))
#     Aj += Am
#     C_ost_lst_2.append(round(C_ost, 2))
# print("Am_lst_2:", Am_lst_2)
# print("C_ost_lst_2", C_ost_lst_2)
# # 2. Контейнер табличного вывода
# Y = range(1, 9)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=["Y", "C_ost_lst", "Am_lst"])
# tfame2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_2", "Am_lst_2"])
# print(tfame)
# print(tfame2)
# # 3. Контейнер визуализации (графики)
# plt.figure()
# plt.plot(tfame["Y"], tfame["C_ost_lst"], label="Am")
# plt.savefig("chart7.png")
# plt.plot(tfame2["Y"], tfame2["C_ost_lst_2"], label="Am2")
# plt.savefig("chart8.png")
# # круговые диаграммы
# vals = Am_lst
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(
#     vals,
#     labels=labels,
#     autopct="%1.1f%%",
#     shadow=True,
#     explode=explode,
#     wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
#     rotatelabels=True,
# )
# ax.axis("equal")
# plt.savefig("chart9.png")

# vals = Am_lst_2
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(
#     vals,
#     labels=labels,
#     autopct="%1.1f%%",
#     shadow=True,
#     explode=explode,
#     wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
#     rotatelabels=True,
# )
# ax.axis("equal")
# plt.savefig("chart10.png")
# plt.clf()

# plt.figure()
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tframe = pd.DataFrame(table1, columns=["Y", "Am_lst"])
# tframe2 = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
# plt.bar(tfame["Y"], tfame["Am_lst"])
# plt.savefig("chart11.jpeg")
# plt.figure()
# plt.bar(tfame2["Y"], tfame2["Am_lst_2"])
# plt.savefig("chart12.jpeg")
import os
vlada=os.environ['vlada']
print(vlada)

import os
VLADA=os.environ['VLADA']
print(VLADA)

import os
Vlada=os.environ['Vlada']
print(Vlada)

import os
KAMA=os.environ['KAMA']
print(KAMA)


import os
Sec_Korneev_1=os.environ['Sec_Korneev_1']
print(Sec_Korneev_1)


import os
Sec_Korneev_2=os.environ['Sec_Korneev_2']
print(Sec_Korneev_2)

#Задание 2 (вариант 6)
from sympy import *

k, T, C, L = symbols('k C T L')

C_ost_4 = 15000
Am_lst_4 = []
C_ost_lst_4 = []
for i in range(8):
    Am = (C - L) / T
    C_ost_4 -= Am.subs({C: 15000, T: 8, L: 0})
    Am_lst_4.append(round(Am.subs({C: 15000, T: 8, L: 0}), 2))
    C_ost_lst_4.append(round(C_ost_4, 2))
print('Am_lst_4:', Am_lst_4)
print('C_ost_lst_4:', C_ost_lst_4)

#2-ой способ 
Aj = 0
C_ost_4 = 15000
Am_lst_2_4 = []
C_ost_lst_2_4 = []
for i in range(8):
    Am = k * 1 / T * (C - Aj)
    C_ost_4 -= Am.subs({C: 15000, T: 8, k: 2})
    Am_lst_2_4.append(round(Am.subs({C: 15000, T: 8, k: 2}), 2))
    Aj += Am
    C_ost_lst_2_4.append(round(C_ost_4, 2))
print('Am_lst_2_4:', Am_lst_2_4)
print('C_ost_lst_2_4:', C_ost_lst_2_4)

#Таблица 
import pandas as pd

Y = range(1, 9)
table1 = list(zip(Y, C_ost_lst_4, Am_lst_4))
table2 = list(zip(Y, C_ost_lst_2_4, Am_lst_2_4))
tframe = pd.DataFrame(table1, columns=['Y', 'C_ost_lst_4', 'Am_lst_4'])
tframe2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2_4', 'Am_lst_2_4'])
print(tframe)#Что делает? Выводит содержимое переменной - ответила Вагизова
print(tframe2)

#Визуализация 
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
plt.plot(tframe['Y'], tframe['C_ost_lst_4'], label='Am')
plt.savefig('chart7.png')
plt.figure()
plt.plot(tframe2['Y'], tframe2['C_ost_lst_2_4'], label='Am_2')
plt.savefig('chart8.png')#Что делает? Сохраняет текущий график - ответила Вагизова

#Круговая диаграмма 
vals = Am_lst_4
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       shadow=True,
       explode=explode,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': "k"
       },
       rotatelabels=True)
ax.axis("equal")
plt.savefig('chart9.png') 

#Круговая диаграмма (данные от 2-го способа)
vals = Am_lst_2_4
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       shadow=True,
       explode=explode,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': "k"
       },
       rotatelabels=True)
ax.axis("equal")
plt.savefig('chart10.png')

#Гистограмма (индивидуальное задание)
table1 = list(zip(Y, Am_lst_4))
table2 = list(zip(Y, Am_lst_2_4))
tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst_4'])#Что это? использование библиотеки pandas - ответила Вагизова
tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2_4'])

plt.figure()
plt.bar(tframe['Y'], tframe['Am_lst_4'])
plt.savefig('chart11.png')

plt.figure()
plt.bar(tframe2['Y'], tframe2['Am_lst_2_4'])
plt.savefig('chart12.png')
#Проверила Вагизова К.Х. 
# 5 из 5
#Индивидуальное задание лаба 3
# cloud_failure_detector.py
# Микросервис для обнаружения отказов в облачной инфраструктуре
# Лабораторная работа 1 - индивидуальное задание 