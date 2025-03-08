def remove_element(nums: list[int], val: int) -> int:
    middle_number = []
    nums_lengths: int = len(nums)

    half_nums = int(nums_lengths / 2)

    if nums_lengths % 2 != 0:
        middle_number = [nums.pop(half_nums - 1)]

    start_middle = nums[:half_nums].copy()
    half_end = nums[half_nums:].copy()

    i_one: int = half_nums - 1
    i_two: int = half_nums - 1

    while i_one != -1 and i_two != -1:
        if start_middle[i_one] == val:
            start_middle.pop(i_one)
        if half_end[i_two] == val:
            half_end.pop(i_two)
        i_one -= 1
        i_two -= 1

    nums = start_middle + half_end + middle_number
    print(nums)


remove_element([3, 2, 2, 3, 2], 3)
remove_element([3, 2, 2, 3], 3)
