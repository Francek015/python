# Even First

# list = [1, 2, 3, 4, 5, 6, 7]
# list.sort(key=(2).__rmod__)
# print(list)


# def even_first(arr: list):
#     next_even = 0
#     next_odd = len(arr) - 1
#     while next_even < next_odd:
#         if arr[next_even] % 2 == 0:
#             next_even += 1
#         else:
#             arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
#             next_odd -= 1
#
#     return arr
#
# test_numbers = [3, 5, 4, 6, 7, 8, 9, 11]
# print(even_first(test_numbers))

# Increment a Number
def increment_number(arr: list):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr


test_list = [9, 4, 9]

print(increment_number(test_list))