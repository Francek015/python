list_int = [3, 6, 4, 7, 9, 2, 7, 9, 2]
print(list_int)



def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    arr.sort(reverse=True)
    return arr


print(selection_sort(list_int))


def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    arr.sort(reverse=True)
    return arr


print(bubble_sort(list_int))


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    arr.sort(reverse=True)
    return arr


print(insertion_sort(list_int))


def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[0:middle]), merge_sort(arr[middle:]))



def merge_arrays(left_arr: list, right_arr: list):
    merged_list = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_list.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_list.append(left_arr[i])
            i += 1
            continue
        if left_arr[i] <= right_arr[j]:
            merged_list.append(left_arr[i])
            i += 1
        else:
            merged_list.append(right_arr[j])
            j += 1
    return merged_list

sorted_list = merge_sort(list_int)
sorted_list.sort(reverse=True)

print(sorted_list)
