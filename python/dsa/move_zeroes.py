def move0s(nums: list[int]) -> None:
    # Traverse the array.
    # Track the position of the least recently encountered zero. Place the next non-zero element there.
    # After a swap, increment the tracker by one. This maintains the order of non-zero elements.
    zero_pos = 0

    for i in range(len(nums)):
        if nums[i]:
            nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
            zero_pos += 1


nums = [2, 0, 4, 0, 9]
move0s(nums)
print(nums)
