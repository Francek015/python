# O(n)
def factorial(number: int):
    result = 1
    for i in range(2, number + 1):
        result = result * i  # result *= i

    print(f'Factorial of {number} is {result}')


test_number = 5


factorial(5)
