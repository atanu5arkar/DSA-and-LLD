# Floyd's Algorithm for Cycle Detection

def duplicate_number(nums: list[int]) -> int:
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    ptr1 = nums[0]
    ptr2 = slow

    while ptr2 != ptr1:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr2


nums = [1, 4, 3, 4, 2]
print(duplicate_number(nums))
