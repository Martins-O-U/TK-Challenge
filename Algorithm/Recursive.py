def binary_recursive(array, val):
    if val < array[0] or val > array[-1]:
        return print(f"{val} is not in the given array")
    mid = len(array) // 2
    left_side = array[:mid]
    right_side = array[mid:]
    if val == array[mid]:
        return print(f"Found, value = {array[mid]}")
    elif array[mid] > val:
        return binary_recursive(left_side, val)
    else:
        array[mid] < val
        return binary_recursive(right_side, val)


chosen_Range = [n for n in range(20)]
binary_recursive(chosen_Range, 9)

# Qyestion 2
# Base case considered in the function was:==  if val < array[0] or val > array[-1],
# to ensure that the search value is still within the recursive search ability based on the given array.

# Question 3
# It Will converge by splitting the array into 2 and comparing each section with the required value,
# this will be repeated until the searched value is found or it returns a message that the searched is not in the given array.

print("=================== Quick_Sort ====================")


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            print(array)
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [24, 44, 12, 99, 3, 56]
quick_sort(array, 0, len(array) - 1)
print(array)
