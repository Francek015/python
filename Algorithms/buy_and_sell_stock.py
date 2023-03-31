def buy_and_sell_stock(price: list):
    max_sum = 0
    curr_sum = 0

    for i in range(len(price) - 1):
        curr_sum = curr_sum + price[i + 1] - price[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


test = [7, 1, 5, 3, 6, 4]
test_result = buy_and_sell_stock(test)

print(test_result)