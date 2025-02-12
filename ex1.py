def merge(arr, low, mid, high):
    temp_array = []
    low_index = low
    high_index = mid + 1

    while low_index != mid + 1 or high_index != high + 1:
        if low_index == mid + 1:
            temp_array.append(arr[high_index])
            high_index += 1
        elif high_index == high + 1:
            temp_array.append(arr[low_index])
            low_index += 1
        else:
            low_element = arr[low_index]
            high_element = arr[high_index]
            if low_element < high_element:
                temp_array.append(low_element)
                low_index += 1
            else:
                temp_array.append(high_element)
                high_index += 1
    for i in range(low, high + 1):
        arr[i] = temp_array[i - low]


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

array = [8, 42, 25, 3, 3, 2, 27, 3]
print(f'Unsorted array: {array}')
merge_sort(array, 0, len(array) - 1)
print(f'Sorted array: {array}')
