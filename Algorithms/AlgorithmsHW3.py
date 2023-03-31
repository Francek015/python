def ar_mean(n):
    ari_mean = sum(n) / len(n)
    total = []
    for element in n:
        if element < ari_mean:
            total.append(element)
    return total


test_list = [1, 2, 3, 4, 5, 6]
test_result = ar_mean(test_list)
print(test_result)


def find_two_lowest(arr):
    arr.sort()
    return arr[:2]


test_numbers = [3, 56, 23, 34, 1, 35, 3]
test_result = find_two_lowest(test_numbers)
print(test_result)

