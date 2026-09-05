def max_profit(prices):
    buy = prices[0]
    profit = 0

    for price in prices:
        if price < buy:
            buy = price
        elif price - buy > profit:
            profit = price - buy

    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))
