def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i +1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index],  arr[i]

    return arr

test_list = [5, 3, 6, 1, 2, 9]
print(test_list)

