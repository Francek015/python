def buy_and_sell_stock(prices: list):
    maximum = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            maximum = maximum + prices[i + 1] - prices[i]

    return maximum


test = [7, 1, 5, 3, 6, 8, 4, 6, 1]
test_result = buy_and_sell_stock(test)

print(test_result)