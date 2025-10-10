# Input is a sorted array, rotated multiple times

def min_element(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    end_val = nums[-1]
    ans = nums[0]

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > end_val:
            left = mid + 1
        else:
            ans = nums[mid]
            right = mid - 1

    return ans


print(min_element([3, 4, 5, 6, 1, 2]))
print(min_element([4, 5, 0, 1, 2, 3]))
print(min_element([4, 5, 6, 7]))
print(min_element([2, 1]))
