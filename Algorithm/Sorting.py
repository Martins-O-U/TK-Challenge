

print("==============LinearSearch ============")
chosen_input = input("Enter your search number between 1 - 19: ")
chosen_range = [n for n in range(20)]


def linear_search():
    if int(chosen_input) >= 20:
        print(f"{chosen_input} is greater than expected value")
    else:
        for x in chosen_range:
            if int(chosen_input) != x:
                print(f"Still Searching")
            else:
                print(f"Found!, Your, input was {x}")
                break


linear_search()

print("============ Binary Search ===============")

chosen_input = input("Enter your search number between 1 - 19: ")
chosen_Range = [n for n in range(20)]


def binary_search():
    lower_limit = 0
    upper_limit = len(chosen_Range)-1
    if int(chosen_input) >= 20:
        print(f"{chosen_input} is greater than expected value")
    else:
        while lower_limit <= upper_limit:
            mid = (lower_limit + upper_limit)//2
            if chosen_Range[lower_limit] == int(chosen_input):
                print(f"Your chosen number is {chosen_Range[lower_limit]}")
                break
            elif chosen_Range[mid] == int(chosen_input):
                print(f"Your chosen number is {chosen_Range[mid]}")
                break
            elif chosen_Range[upper_limit] == int(chosen_input):
                print(f"Your chosen number is {chosen_Range[upper_limit]}")
                break
            elif chosen_Range[mid] > int(chosen_input):
                upper_limit = mid - 1
                print("Still Searching")
            else:
                lower_limit = mid + 1
                print("Still Searching")


binary_search()


print("=========== Insertion_Sort ================")

arr = [25, 67, 4, 33, 29, 40]


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        sort_num = 0
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)


insertionSort(arr)


print("============ Selection_Sort =================")

Given_array = [25, 67, 4, 33, 29, 40]
for i in range(len(Given_array)):
    new_idx = i
    for j in range(i+1, len(Given_array)):
        if Given_array[new_idx] > Given_array[j]:
            new_idx = j
    Given_array[i], Given_array[new_idx] = Given_array[new_idx], Given_array[i]
    print(Given_array)
