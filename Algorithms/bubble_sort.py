def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1], = arr[j + 1], arr[j]

    return arr


test_list = [5, 3, 6, 1, 2, 9]
print(bubble_sort(test_list))