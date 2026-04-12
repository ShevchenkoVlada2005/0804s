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

#Задание 2 (вариант 6) (изменения 2 на вариант 3)
from sympy import *

k, T, C, L = symbols('k C T L')

C_ost_4 = 30000
Am_lst_4 = []
C_ost_lst_4 = []
for i in range(7):
    Am = (C - L) / T
    C_ost_4 -= Am.subs({C: 30000, T: 7, L: 0})
    Am_lst_4.append(round(Am.subs({C: 30000, T: 7, L: 0}), 2))
    C_ost_lst_4.append(round(C_ost_4, 2))
print('Am_lst_4:', Am_lst_4)
print('C_ost_lst_4:', C_ost_lst_4)

#2-ой способ 
Aj = 0
C_ost_4 = 30000
Am_lst_2_4 = []
C_ost_lst_2_4 = []
for i in range(7):
    Am = k * 1 / T * (C - Aj)
    C_ost_4 -= Am.subs({C: 30000, T: 7, k: 2})
    Am_lst_2_4.append(round(Am.subs({C: 30000, T: 7, k: 2}), 2))
    Aj += Am
    C_ost_lst_2_4.append(round(C_ost_4, 2))
print('Am_lst_2_4:', Am_lst_2_4)
print('C_ost_lst_2_4:', C_ost_lst_2_4)

#Таблица 
import pandas as pd

Y = range(1, 8)
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
labels = [str(x) for x in range(1, 8)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
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
labels = [str(x) for x in range(1, 8)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,)
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
#Создание секретных ключей(Индивидуальное задание)
#1 Секретные ключи
s1 = os.environ['Shev1']
s2 = os.environ['Shev2']
s3 = os.environ['Shev3']
print("Секретные ключи - обнаружение отказов в облачной инфраструктуре")
print("Shev1 =", s1)
print("Shev2 =", s2)
print("Shev3 =", s3)

# Преобразуем секреты в нужные переменные
FAILURE_THRESHOLD = int(s1)
CPU_THRESHOLD = float(s2)
MEMORY_THRESHOLD = float(s3)
# 2 задание индивидуальное
# cloud_failure_detector.py
# Микросервис для обнаружения отказов в облачной инфраструктуре
# Лабораторная работа 3 - индивидуальное задание вариант 164


import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

# ========== НАСТРОЙКИ ИЗ SECRETS ==========
s1 = os.environ['Shev1']
s2 = os.environ['Shev2']
s3 = os.environ['Shev3']

print("Секретные ключи - обнаружение отказов в облачной инфраструктуре")
print("Shev1 =", s1)
print("Shev2 =", s2)
print("Shev3 =", s3)

FAILURE_THRESHOLD = int(s1)
CPU_THRESHOLD = float(s2)
MEMORY_THRESHOLD = float(s3)

print("-" * 50)

# ========== ИМЕНА ФАЙЛОВ ==========
INPUT_FILE = "cloud_metrics.json"
OUTPUT_JSON = "failed_nodes.json"
OUTPUT_CHART = "failure_report.png"

# ========== 1. ЗАГРУЗКА ДАННЫХ ==========
def load_data():
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)
    print(f"Загружено {len(data)} записей")
    return data

# ========== 2. АНАЛИЗ ОТКАЗОВ ==========
def analyze_failures(data):
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(['node_id', 'timestamp'])

    df['cpu_fail'] = df['cpu_usage'] > CPU_THRESHOLD
    df['memory_fail'] = df['memory_usage'] > MEMORY_THRESHOLD
    df['is_failed'] = df['cpu_fail'] | df['memory_fail']

    def count_fails_in_row(fail_list):
        result = []
        counter = 0
        for is_fail in fail_list:
            if is_fail:
                counter += 1
            else:
                counter = 0
            result.append(counter)
        return result

    df['fails_in_row'] = df.groupby('node_id')['is_failed'].transform(count_fails_in_row)
    df['need_block'] = df['fails_in_row'] >= FAILURE_THRESHOLD

    def get_status(row):
        if row['need_block']:
            return "ЗАБЛОКИРОВАН"
        elif row['is_failed']:
            return "НЕСТАБИЛЕН"
        else:
            return "РАБОТАЕТ"

    df['status'] = df.apply(get_status, axis=1)
    return df

# ========== 3. ВЫВОД ТАБЛИЦЫ ==========
def print_table(df):
    table = df.tail(15).copy()
    table['time'] = table['timestamp'].dt.strftime('%H:%M:%S')
    table['cpu'] = table['cpu_usage'].apply(lambda x: f"{x:.0f}%")
    table['memory'] = table['memory_usage'].apply(lambda x: f"{x:.0f}%")

    result = table[['time', 'node_id', 'node_type', 'cpu', 'memory', 'status', 'fails_in_row']]
    result.columns = ['Время', 'Узел', 'Тип', 'CPU', 'Память', 'Статус', 'Отказов_подряд']

    print("\n" + "=" * 80)
    print("РЕЗУЛЬТАТЫ МОНИТОРИНГА ОБЛАЧНОЙ ИНФРАСТРУКТУРЫ")
    print("=" * 80)
    print(result.to_string(index=False))
    print("=" * 80)

# ========== 4. ВЫВОД СТАТИСТИКИ ==========
def print_statistics(df):
    print("\n" + "=" * 60)
    print("СТАТИСТИКА ПО УЗЛАМ")
    print("=" * 60)

    blocked = len(df[df['need_block'] == True]['node_id'].unique())
    unstable = len(df[(df['is_failed'] == True) & (df['need_block'] == False)]['node_id'].unique())
    healthy = len(df[df['is_failed'] == False]['node_id'].unique())

    print(f"\nВсего уникальных узлов: {df['node_id'].nunique()}")
    print(f"  - РАБОТАЮТ нормально: {healthy}")
    print(f"  - НЕСТАБИЛЬНЫ (есть отказы): {unstable}")
    print(f"  - ЗАБЛОКИРОВАНЫ (много отказов подряд): {blocked}")

    print(f"\nСредняя загрузка CPU: {df['cpu_usage'].mean():.1f}%")
    print(f"Средняя загрузка памяти: {df['memory_usage'].mean():.1f}%")
    print(f"Максимум отказов подряд: {df['fails_in_row'].max()}")

    blocked_nodes = df[df['need_block'] == True]['node_id'].unique()
    if len(blocked_nodes) > 0:
        print(f"\nЗАБЛОКИРОВАННЫЕ УЗЛЫ:")
        for node in blocked_nodes:
            node_df = df[df['node_id'] == node]
            max_fails = node_df['fails_in_row'].max()
            print(f"  - {node}: {max_fails} отказов подряд")

    return blocked_nodes

# ========== 5. СОХРАНЕНИЕ РЕЗУЛЬТАТОВ ==========
def save_results(df, blocked_nodes):
    failed_list = []
    for node in blocked_nodes:
        node_data = df[df['node_id'] == node].iloc[-1]
        failed_list.append({
            "node_id": node,
            "node_type": node_data['node_type'],
            "fails_count": int(node_data['fails_in_row']),
            "reason": f"Превышен порог в {FAILURE_THRESHOLD} отказа подряд"
        })

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(failed_list, f, ensure_ascii=False, indent=2)

    print(f"\nРезультаты сохранены в файл: {OUTPUT_JSON}")

# ========== 6. ПОСТРОЕНИЕ ГРАФИКА ==========
def create_chart(df, blocked_nodes):
    blocked_count = len(blocked_nodes)
    unstable_count = len(df[(df['is_failed'] == True) & (df['need_block'] == False)]['node_id'].unique())
    healthy_count = df['node_id'].nunique() - blocked_count - unstable_count

    sizes = []
    labels = []
    colors = []

    if healthy_count > 0:
        sizes.append(healthy_count)
        labels.append(f'РАБОТАЕТ ({healthy_count})')
        colors.append('#2ecc71')

    if unstable_count > 0:
        sizes.append(unstable_count)
        labels.append(f'НЕСТАБИЛЕН ({unstable_count})')
        colors.append('#f39c12')

    if blocked_count > 0:
        sizes.append(blocked_count)
        labels.append(f'ЗАБЛОКИРОВАН ({blocked_count})')
        colors.append('#e74c3c')

    if len(sizes) == 0:
        sizes = [1]
        labels = ['НЕТ ДАННЫХ']
        colors.append('#95a5a6')

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90)
    plt.title('Состояние узлов облачной инфраструктуры', fontsize=14, fontweight='bold')

    plt.savefig(OUTPUT_CHART, dpi=120, bbox_inches='tight')
    plt.close()

    print(f"\nГрафик сохранен в файл: {OUTPUT_CHART}")

# ========== 7. ГЛАВНАЯ ФУНКЦИЯ ==========
def main():
    print("\n" + "=" * 70)
    print("КОНТЕЙНЕР БЕЗОПАСНОСТИ ОБЛАЧНОЙ ИНФРАСТРУКТУРЫ")
    print("Обнаружение отказов (вариант 164)")
    print("=" * 70)

    print("\n1. Загрузка метрик...")
    data = load_data()

    print("\n2. Анализ состояния узлов...")
    df = analyze_failures(data)

    print_table(df)
    blocked_nodes = print_statistics(df)

    print("\n3. Сохранение результатов...")
    save_results(df, blocked_nodes)

    create_chart(df, blocked_nodes)

    print("\n" + "=" * 70)
    print("РАБОТА ЗАВЕРШЕНА")
    print("=" * 70)
    print(f"\nСозданные файлы:")
    print(f"  - {OUTPUT_JSON}")
    print(f"  - {OUTPUT_CHART}")

if __name__ == "__main__":
    main()

