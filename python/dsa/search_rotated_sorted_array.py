# Input is a sorted array of unique values, rotated multiple times

def target_pos(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    end_val = nums[-1]    
    min_pos = 0

    # O (log n)
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > end_val:
            left = mid + 1
        else:
            min_pos = mid
            right = mid - 1

    if nums[min_pos] == target:
        return min_pos
    
    # Target is either on the left or right of the min element
    # O (log n)
    if target > nums[min_pos] and target <= end_val:
        left = min_pos + 1
        right = len(nums) - 1
    else:
        left = 0
        right = min_pos - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    
    return -1


print(target_pos([3, 4, 5, 6, 1, 2], 1))
print(target_pos([1, 3], 3))
print(target_pos([1, 3, 5], 5))

