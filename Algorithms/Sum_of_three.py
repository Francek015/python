

def sum_of_three(n: int):
    original_n = n
    result = 0
    while n != 0:
        result = result + (n % 10)
        n = n // 10

    print(f'sum of all numbers {original_n} is {result}')


test = 125

sum_of_three(test)
