def calc_max_profit(prices: list[int]) -> int:
    max_profit = 0
    buy = prices[0]
    start = 0
    end = start + 1

    while end < len(prices):
        buy = min(buy, prices[end])
        profit = prices[end] - buy
        max_profit = max(max_profit, profit)

        start += 1
        end += 1

    # Brute Force
    # while start < len(prices) - 1:
    #     profit = prices[end] - prices[start]
    #     max_profit = max(max_profit, profit)
    #
    #     if end == len(prices) - 1:
    #         start += 1
    #         end = start + 1
    #     else:
    #         end += 1

    return max_profit


result = calc_max_profit([10, 1, 5, 6, 7, 1])
print(result)
