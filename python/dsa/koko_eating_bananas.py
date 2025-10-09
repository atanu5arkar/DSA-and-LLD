import math

# O(n * log m)
def bananas_to_eat_per_hour(piles: list[int], h: int) -> int:
    left = 0
    right = max(piles) - 1
    min_rate = 1

    while left <= right:
        mid = left + (right - left) // 2
        hrs = 0

        for p in piles:
            hrs += math.ceil(p / (mid + 1))

        if hrs > h:
            left = mid + 1
        else:
            min_rate = mid + 1
            right = mid - 1

    return min_rate


piles = [1, 4, 3, 2]
h = 9
print(bananas_to_eat_per_hour(piles, h))
