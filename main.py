import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from algorithms import sorting_algorithm, search_algorithm, count_unique_elements, linear_search, bubble_sort
from time_execution import time_execution
from data_generation import best_case_data, average_case_data, worst_case_data

# Анализ сложности алгоритмов
N_values = [1, 2, 5, 10, 20, 50, 100, 150]
sorting_times = []
searching_times = []
counting_times = []

for N in N_values:
    data = np.random.randint(0, 100, N)  # Генерация случайных данных

    # Замер времени для сортировки
    sorting_time = time_execution(sorting_algorithm, data)
    sorting_times.append(sorting_time)

    # Замер времени для поиска (например, ищем элемент 50)
    searching_time = time_execution(search_algorithm, data, 50)
    searching_times.append(searching_time)

    # Замер времени для подсчета уникальных элементов
    counting_time = time_execution(count_unique_elements, data)
    counting_times.append(counting_time)

# Построение графиков
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(N_values, sorting_times, marker='o')
plt.title('Sorting Algorithm Time Complexity')
plt.xlabel('N')
plt.ylabel('Time (s)')

plt.subplot(1, 3, 2)
plt.plot(N_values, searching_times, marker='o')
plt.title('Search Algorithm Time Complexity')
plt.xlabel('N')
plt.ylabel('Time (s)')

plt.subplot(1, 3, 3)
plt.plot(N_values, counting_times, marker='o')
plt.title('Count Unique Elements Time Complexity')
plt.xlabel('N')
plt.ylabel('Time (s)')

plt.tight_layout()
plt.show()

# Сравнение времени работы алгоритмов
cases = ['best', 'average', 'worst']
algorithms = {
    'library_sort': sorted,
    'my_sort': bubble_sort,
    'library_search': search_algorithm,
    'my_search': linear_search,
}

results = {alg: {case: [] for case in cases} for alg in algorithms}

N_values = [10, 100, 1000]  # Маленький, средний и большой N

for N in N_values:
    for case in cases:
        if case == 'best':
            data = best_case_data(N)
        elif case == 'average':
            data = average_case_data(N)
        else:
            data = worst_case_data(N)

        # Замеры для сортировки
        for alg_name, alg in algorithms.items():
            if 'sort' in alg_name:
                exec_time = time_execution(alg, data.copy())
                results[alg_name][case].append(exec_time)

        # Замеры для поиска
        for alg_name, alg in algorithms.items():
            if 'search' in alg_name:
                exec_time = time_execution(alg, data.copy(), 50)  # Ищем элемент 50
                results[alg_name][case].append(exec_time)

# Вывод результатов в таблицу с использованием tabulate
table_data = {
    'Algorithm': [],
    'Case': [],
    'N': [],
    'Time (s)': []
}

for alg_name in results:
    for case in results[alg_name]:
        for idx, time in enumerate(results[alg_name][case]):
            table_data['Algorithm'].append(alg_name)
            table_data['Case'].append(case)
            table_data['N'].append(N_values[idx])
            table_data['Time (s)'].append(time)

df_results = pd.DataFrame(table_data)

# Использование tabulate для красивого вывода
print(tabulate(df_results, headers='keys', tablefmt='pretty', floatfmt=".6f"))