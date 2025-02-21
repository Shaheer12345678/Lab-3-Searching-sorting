import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(arr):
    comparisons = 0
    swaps = 0

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return comparisons, swaps

def plot(x, comp, swap):
    # Interpolation for comparisons and swaps
    a1, b1, c1 = np.polyfit(x, comp, 2)
    x1_pred = np.linspace(min(x), max(x), 100)
    y1_pred = a1 * x1_pred ** 2 + b1 * x1_pred + c1

    a2, b2, c2 = np.polyfit(x, swap, 2)
    x2_pred = np.linspace(min(x), max(x), 100)
    y2_pred = a2 * x2_pred ** 2 + b2 * x2_pred + c2

    plt.figure(0)
    plt.scatter(x, comp, color='blue', label='Comparisons')
    plt.plot(x1_pred, y1_pred, color='green', label="Comparisons(Interpolated)")
    plt.title("Bubble sort comparison count for a given input size")
    plt.xlabel("Input size")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("ex3_comp.png")

    plt.figure(1)
    plt.scatter(x, swap, color='red', label='Swaps')
    plt.plot(x2_pred, y2_pred, color='purple', label="Swaps(Interpolated)")
    plt.title("Bubble sort swap count for a given input size")
    plt.xlabel("Input size")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("ex3_swap.png")


    plt.figure(2)
    plt.scatter(x, comp, color='blue', label='Comparisons')
    plt.plot(x1_pred, y1_pred, color='green', label="Comparisons(Interpolated)")
    plt.scatter(x, swap, color='red', label='Swaps')
    plt.plot(x2_pred, y2_pred, color='purple', label="Swaps(Interpolated)")
    plt.title("Comparison and swap count of bubble sort for a given input size")
    plt.xlabel("Input size")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("ex3_both.png")

def results():
    x_values = [x for x in range(4, 15, 1)]
    comparison_counts = []
    swap_counts = []
    for i in range(4, 15, 1):
        random_array = np.random.randint(0, i, size=i) # Creates an unsorted array of random numbers
        comparisons, swaps = bubble_sort(random_array)
        comparison_counts.append(comparisons)
        swap_counts.append(swaps)
    #plot(x_values, comparison_counts, swap_counts)

results()
