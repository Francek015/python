def total_sum(n):
    total = sum(range(n + 1))
    print(total)


total_sum(9)


def highest_num(x, y, z):
    for i in x, y, z:
        if y < i > z:
            print(i)
        elif x < i > z:
            print(i)
        elif x < i > y:
            print(i)


highest_num(9, 90, 7)


def odds_evens(n):
    evens = 0
    odds = 0
    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1
        n = n // 10
    print(f'Odds: {odds}')
    print(f'Evens: {evens}')


odds_evens(123412341)


