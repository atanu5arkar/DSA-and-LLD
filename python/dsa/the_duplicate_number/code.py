
def duplicate_number(nums: list[int]) -> int:
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break

    meetup = slow
    return -1


nums = [1, 2, 3, 2, 2]
print(duplicate_number(nums))
