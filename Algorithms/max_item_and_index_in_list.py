def max_element(arr):
    max_index = 0
    max_num = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i

    print(f"Max number: {max_num}")
    print(f"Max index: {max_index}")

test_list = [5, 6, 3, 6, 10, 3, 6, 9]
test_result = max_element(test_list)

print(test_result)