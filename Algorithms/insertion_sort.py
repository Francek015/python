def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


test_list = [5, 3, 6, 1, 2, 9]
print(insertion_sort(test_list))
