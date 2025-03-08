def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    list nums1
    m representa el numero de elementos en nums1
    list nums2
    n representa el numero de elemento en nums2
    """
    if m == 0 or n == 0:
        nums1 = nums1 if n == 0 else nums2
    else:
        flag = float()

        while len(nums2) != 0:
            for x in range(0, m + n):
                if flag:
                    x = flag

                if nums1[x] == 0:
                    nums1[x] = nums2[0]
                    flag = x + 1
                    nums2.pop(0)

                elif nums2[0] == nums1[x] + 1:
                    nums1.insert(x + 1, nums2[x])
                    nums2.pop(x)

        if 0 in nums1:
            for index, num in enumerate(nums1):
                if num == 0:
                    nums1.pop(index)

    print(nums1)


merge_sorted_array(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
merge_sorted_array(nums1=[1], m=1, nums2=[], n=0)
merge_sorted_array(nums1=[0], m=0, nums2=[1], n=1)
