class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        size = n1 + n2
        median_idx = size // 2
        i, j, k = 0, 0, 0
        k = 0
        prev, median = None, None
        while i < n1 and j < n2 and k <= median_idx:
            prev = median
            if nums1[i] <= nums2[j]:
                median = nums1[i]
                i += 1
            else:
                median = nums2[j]
                j += 1
            k += 1

        while i < n1 and k <= median_idx:
            prev = median
            median = nums1[i]
            i += 1
            k += 1
        

        while j < n2 and k <= median_idx:
            prev = median
            median = nums2[j]
            j += 1
            k += 1

        if size % 2 != 0:
            return median
        else:
            return (median+prev)/2