import numpy as np

def sorting_algorithm(data):
    return sorted(data)

def search_algorithm(data, target):
    return target in data

def count_unique_elements(data):
    return len(set(data))

def linear_search(data, target):
    for element in data:
        if element == target:
            return True
    return False

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]