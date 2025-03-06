"""
Given a fixed-length integer array arr, duplicate each
occurrence of zero, shifting the remaining elements to
the right.

Note that elements beyond the length of the original
array are not written. Do the above modifications to
the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is
modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is
modified to: [1,2,3]


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""


def duplicateZeros(arr: list[int]) -> None:
    if 0 in arr:
        exclude_index:set = set()

        for index, num in enumerate(arr):
            if num == 0 and index not in exclude_index:
                arr.insert(index + 1, 0)
                exclude_index.add(index + 1)
                arr.pop()

    print(arr)


duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
duplicateZeros([1, 2, 3])
