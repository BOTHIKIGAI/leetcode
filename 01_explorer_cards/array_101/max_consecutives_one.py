"""
Given a binary array nums, return the maximum number
of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits
are consecutive 1s. The maximum number of consecutive

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    count: int = 0
    max_count: int = 0

    for value in nums:
        if value == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count


print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
