"""
1. Use a set to track seen elements. If a num already exists, return it.

2. Given (n + 1) integers s.t. each num is within the interval [1, n]. Only one of the nums is repeated
two or more times:

    - Every num > 0.
    - Every value can be used as an index to access another value.

Traverse the array. In every iteration, negate the value at the index represented by the current number.
If the index appears more than once, then the corresponding value would be < 0; the sign to return the
current number as the required duplicate.

3. To refine the previous algorithm, pose it as creating a Linked List, where every value represents the
pointer to the next node:

    - The list will always have a cycle.

    - No. of incoming edges = No. of times the index appears in the array => The node with the repeated index
    has > 1 edges, i.e. the duplicate num is the entry point of the cycle.
"""


def duplicate_number(nums: list[int]) -> int:
    for num in nums:
        num = abs(num)  # Avoid IndexError
        if nums[num] < 0:
            return num

        nums[num] *= -1

    return -1


nums = [1, 2, 3, 2, 2]
print(duplicate_number(nums))
