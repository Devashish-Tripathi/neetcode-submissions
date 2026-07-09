class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            n = len(arr)
            if n <= 1:
                return arr

            subA = mergeSort(arr[:n//2])
            subB = mergeSort(arr[n//2:])
            szA, szB = len(subA), len(subB)
            subC = []
            i = j = 0
            while i < szA and j < szB:
                if subA[i] < subB[j]:
                    subC.append(subA[i])
                    i += 1
                else:
                    subC.append(subB[j])
                    j += 1
            while i < szA:
                subC.append(subA[i])
                i += 1
            while j < szB:
                subC.append(subB[j])
                j += 1
            
            return subC
        return mergeSort(nums)