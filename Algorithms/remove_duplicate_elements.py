def delete_duplicates(arr: list):
    write_index = 1

    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, len(arr)):
        arr[i] = 0
    print(arr)
    return write_index


test_list = [2, 5, 5, 6, 7, 7, 7, 9, 10]
test_result = delete_duplicates(test_list)

print(test_result)
