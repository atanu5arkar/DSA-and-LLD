"""
* When all the elements on a stack are either in ascending or descending order, it is called monotonic.
* It is used to find the next greater or smaller number for every number in an array.
"""

def next_greater_elements(nums: list[int]) -> list[int]:
    # Track the elements whose next greater elements are not found yet.
    stack = []
    size = len(nums)
    result = [-1] * size

    for i in range(size):
        # The following element in the stack can also be smaller than the current element, therefore a loop is needed.
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return result

arr = [2, 1, 3, 2, 4, 3]
print(next_greater_elements(arr))