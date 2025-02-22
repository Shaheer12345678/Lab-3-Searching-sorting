import random
import timeit
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(15000)

def partition(array, low, high):
    pivot = array[low]
    i = low
    j = high

    while i < j:
        while array[i] <= pivot and i <= high - 1:
            i += 1

        while array[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[low]
    array[low] = array[j]
    array[j] = temp
    return j


def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)


def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


def binary_search(array, target, low, high):
    if high < low:
        return -1
    mid = (low + high) // 2
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, high)
    else:
        return binary_search(array, target, low, mid - 1)

def linear_search_task(array, target):
    linear_search(array, target)

def binary_search_task(array, target, low, high):
    # array is already sorted, resulting in worst case time complexity
    quicksort(array, low, high)
    binary_search(array, target, low, high)


def plot(x, y1, y2):
    plt.scatter(x, y1, color='blue', label='Linear search')
    plt.scatter(x, y2, color='red', label='Binary search (after quicksort)')
    plt.title("Execution time of linear and binary search on arrays of varying sizes")
    plt.xlabel("Input size")
    plt.ylabel("Execution time (seconds)")
    plt.legend()
    plt.savefig("ex6_worst.png")


def task():
    tasks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    times_linear = []
    times_binary = []
    for i in range(len(tasks)):
        # print(i)
        task_array = [x for x in range(tasks[i])]
        target = task_array[len(task_array) // 2]
        total_time_linear = timeit.timeit(lambda: linear_search_task(random.sample(task_array, len(task_array)), target), number=100)
        total_time_binary = timeit.timeit(lambda: binary_search_task(task_array[:], target, 0, len(task_array) - 1), number=100)
        times_linear.append(total_time_linear / 100)
        times_binary.append(total_time_binary / 100)
    plot(tasks, times_linear, times_binary)

task()

# 4. Discuss which algorithm is faster
# Linear search is still faster than the quick sort into binary search sequence, with the difference now being several orders of magnitude.
# As well, instead of linear time complexity, the combination of worst-case quick sort and binary search now has a quadratic complexity.
