def sum_between_min_and_max(arr):
    if len(arr) <= 2:
        return 0

    min_item = max_item = arr[0]
    min_index = max_index = 0
    i = 1
    while i < len(arr):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i
        if arr[i] < min_item:
            min_item = arr[i]
            min_index = i
        i += 1

    return sum(arr[min(min_index, max_index) + 1: max(min_index, max_index)])

test_list = [2, 5, 8, 3, 9, 5, 4]
test_result = sum_between_min_and_max(test_list)

test_list2 = [1,2]
test_result2 = sum_between_min_and_max(test_list2)


print(test_result)
print(test_result2)
