# Revision: Nov 3, 2025

import math

def min_eating_speed(piles: list[int], h: int) -> int:
    # At most, Koko can eat as many bananas in an hour as is available
    # in the pile with most bananas.
    
    # Binary Search to determine the minimum possible rate
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

print(min_eating_speed(piles, h))
