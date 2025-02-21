import matplotlib.pyplot as plt
import numpy as np
import timeit
import random

def insertion_sort(array):
    for i in range(1, len(array)):
        target = array[i]
        j = i - 1
        while j >= 0 and target < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = target


def binary_search(array, target, low, high):
    if high <= low:
        if target > array[low]:
            return low + 1
        else:
            return low
    
    mid = (low + high) // 2

    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, high)
    else:
        return binary_search(array, target, low, mid - 1)


# Made to modify the array rather than return a sorted copy to match insertion sort
def binary_insertion_sort(array):
    for i in range(1, len(array)):
        target = array[i]
        j = i - 1
        pos = binary_search(array, target, 0, j)
        while j >= pos:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = target

def plot(x, y1, y2):
    # Interpolation for both graphs
    a1, b1, c1 = np.polyfit(x, y1, 2)
    x1_pred = np.linspace(min(x), max(x), 100)
    y1_pred = a1 * x1_pred ** 2 + b1 * x1_pred + c1

    a2, b2, c2 = np.polyfit(x, y2, 2)
    x2_pred = np.linspace(min(x), max(x), 100)
    y2_pred = a2 * x2_pred ** 2 + b2 * x2_pred + c2

    plt.scatter(x, y1, color='blue', label='Insertion sort')
    plt.plot(x1_pred, y1_pred, color='green', label="Insertion sort(Interpolated)")
    plt.scatter(x, y2, color='red', label='Binary insertion sort')
    plt.plot(x2_pred, y2_pred, color='purple', label="Binary insertion sort(Interpolated)")
    plt.title("Execution time of insertion and binary insertions sorts on arrays of varying sizes")
    plt.xlabel("Input size")
    plt.ylabel("Execution time (seconds)")
    plt.legend()
    plt.savefig("ex5.png")



def test():
    unsorted = [random.randint(1, 100) for x in range(1, 20)]
    x_values = [x for x in range(1, len(unsorted) + 1)]
    is_times = []
    bis_times = []
    for i in range(0, len(unsorted)):
        is_time = timeit.timeit(lambda: insertion_sort(unsorted[0:i]))
        #print(f"is: {is_time}")
        is_times.append(is_time)
        bis_time = timeit.timeit(lambda: binary_insertion_sort(unsorted[0:i]))
        #print(f"bis: {bis_time}")
        bis_times.append(bis_time)
    plot(x_values, is_times, bis_times)

test()

# 4. Which algorithm is faster? Why?
# In this case, insertion sort was faster than binary insertion sort.
# The reason for this is because there is a lot more setup involved in binary insertion sort
# than insertion sort, which is not worth the runtime cost for smaller arrays. The binary search
# does not justify its existance when the array is sufficiently small that linear search
# still works very well.
