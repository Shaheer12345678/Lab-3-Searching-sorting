import numpy as np
import timeit
import matplotlib.pyplot as plt

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

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

def worst_case(x_values):
    bubble_times = []
    quick_times = []
    for i in range(1, 21, 1):
        worst_case_bubble = np.flip(np.arange(i))
        worst_case_quick = np.copy(worst_case_bubble)
        bubble_times.append(timeit.timeit(lambda: bubble_sort(worst_case_bubble)))
        quick_times.append(timeit.timeit(lambda: quicksort(worst_case_quick, 0, len(worst_case_quick) - 1)))
    plt.figure(0)
    plt.title("Worst case quick sort vs bubble sort")
    plt.scatter(x_values, bubble_times, color='blue', label='Bubble sort')
    plt.scatter(x_values, quick_times, color='red', label='Quick sort')
    plt.legend()
    plt.savefig("ex2_worst.png")

def average_case(x_values):
    bubble_times = []
    quick_times = []
    for i in range(1, 21, 1):
        average_case_both = np.random.randint(0, i, size=i)
        copy = np.copy(average_case_both)
        bubble_times.append(timeit.timeit(lambda: bubble_sort(average_case_both)))
        quick_times.append(timeit.timeit(lambda: quicksort(copy, 0, len(copy) - 1)))
    plt.figure(1)
    plt.title("Average case quick sort vs bubble sort")
    plt.scatter(x_values, bubble_times, color='blue', label='Bubble sort')
    plt.scatter(x_values, quick_times, color='red', label='Quick sort')
    plt.legend()
    plt.savefig("ex2_avg.png")

def best_case(x_values):
    bubble_times = []
    quick_times = []
    for i in range(1, 21, 1):
        best_case_bubble = np.arange(i)
        best_case_quick = np.random.randint(0, i, size=i) # Creates roughly equal partitions due to randomness
        bubble_times.append(timeit.timeit(lambda: bubble_sort(best_case_bubble)))
        quick_times.append(timeit.timeit(lambda: quicksort(best_case_quick, 0, len(best_case_quick) - 1)))
    plt.figure(2)
    plt.title("Best case quick sort vs bubble sort")
    plt.scatter(x_values, bubble_times, color='blue', label='Bubble sort')
    plt.scatter(x_values, quick_times, color='red', label='Quick sort')
    plt.legend()
    plt.savefig("ex2_best.png")

def main():
    x_values = np.arange(1, 21, 1)
    worst_case(x_values)
    #average_case(x_values)
    #best_case(x_values)

main()

