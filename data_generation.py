import numpy as np

def best_case_data(N):
    return np.array(range(N))  # Упорядоченные данные

def average_case_data(N):
    return np.random.randint(0, 100, N)  # Случайные данные

def worst_case_data(N):
    return np.array(range(N-1, -1, -1))  # Обратный порядок