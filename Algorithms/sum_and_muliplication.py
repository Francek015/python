def print_sum_and_mult(arr):
    sum_of_list = 0
    mult_of_list = 1
    for e in arr:
        sum_of_list += e
        mult_of_list *= e

    print(arr)
    print(sum_of_list)
    print(mult_of_list)


test_list = [1, 3, 5]
test_result = print_sum_and_mult(test_list)

print(test_result)