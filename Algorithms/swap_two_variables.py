def swap_variables(a: int, b: int):
    print(f'before swap: a = {a}, b = {b}')
    temp = a
    a = b
    b = temp
    print(f'after swap: a = {a}, b = {b}')


test_a = 5
test_b = 10
swap_variables(test_a, test_b)

def swap_variables(a: int, b: int):
    print(f'before swap: a = {a}, b = {b}')
    a, b = b, a
    print(f'after swap: a = {a}, b = {b}')


test_a = 5
test_b = 10
swap_variables(test_a, test_b)