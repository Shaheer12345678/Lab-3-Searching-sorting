import matplotlib.pyplot as plt
import timeit
import json

def binary_search(array, target, low, high, mid):
    if high < low:
        return -1
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, high, (mid + 1 + high) // 2) # Successive iterations just split array in half
    else:
        return binary_search(array, target, low, mid - 1, (low + mid - 1) // 2) # Successive iterations just split array in half

def plot(x, y):
    plt.scatter(x, y, color='blue')
    plt.title("Midpoint vs execution time of various tasks")
    plt.xlabel("Midpoint")
    plt.ylabel("Execution time (seconds)")
    plt.savefig("ex7.png")



def timing():
    with open("ex7data.json", "r") as file:
        array = json.load(file)
    with open("ex7tasks.json", "r") as file:
        tasks = json.load(file)

    points = []
    times = []

    for task in tasks:
        # Different midpoints will be at 1/200, 2/200, 3/200, 4/200...
        bestpoint = -1
        besttime = -1
        parts = 200
        for i in range(1, parts):
            midpoint = int(len(array) * i/parts)
            time = timeit.timeit(lambda: binary_search(array, task, 0, len(array) - 1, midpoint), number=1)
            if time < besttime or besttime == -1:
                besttime = time
                bestpoint = midpoint
        points.append(bestpoint)
        times.append(besttime)
    plot(points, times)
                
timing()

# 4. 
# The choice of initial midpoint does not seem to matter too much, seeing as the graph has little to no trend.
# This is most likely caused by how binary search is a recursive function with several layers of recursion.
# Only setting the midpoint on the first call will have little effect on the eventual execution time.
