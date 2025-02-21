import numpy as np
import matplotlib.pyplot as plt
import timeit

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

def plot(x, y):
    # Best fit
    a, b, c = np.polyfit(x, y, 2)
    x_pred = np.linspace(min(x), max(x), 100)
    y_pred = a * x_pred ** 2 + b * x_pred + c

    plt.scatter(x, y, color='blue', label='Quicksort')
    plt.plot(x_pred, y_pred, color='red', label="Quicksort(Interpolated)")
    plt.title("Worst-case time to quicksort an array of size i")
    plt.xlabel("Array size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("ex4.png")


def increasing_worst_case(repetitions):
    x_values = [x for x in range(1, repetitions, 1)]
    times = []

    for i in range(1, 21):
        worst_case_array = [x for x in range(i)]
        #print(worst_case_array)
        times.append(timeit.timeit(lambda: quicksort(worst_case_array, 0, i - 1)))
    plot(x_values, times)

increasing_worst_case(21)
