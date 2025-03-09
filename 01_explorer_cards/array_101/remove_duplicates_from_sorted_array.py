def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k


removeDuplicates([1, 1])
removeDuplicates([1])
removeDuplicates([])
removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
removeDuplicates([1, 1, 2])
