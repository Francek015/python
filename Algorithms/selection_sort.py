# list_int = [3, 6, 4, 7, 9, 2, 7, 9, 2]
# print(list_int)
#list_int.sort()
# print(list_int)
# list_int.sort(reverse=True)
# print(list_int)
# works with words to and a key can be used to decide what to sort by ex. key=len


# def recursion(number: int):
#     if number == 0:
#         return
#     print(number)
#     number -= 1
#     recursion(number)
#
#
# recursion(10)

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

