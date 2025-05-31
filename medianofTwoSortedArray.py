class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numSol = []
        len_mix = len(nums1)+len(nums2)
        p1=0
        p2=0
        output = 0
        for _ in range((len_mix//2)+1):
            if p1 > len(nums1)-1:
                numSol.append(nums2[p2])
                p2+=1
                continue
            elif p2 > len(nums2)-1:
                numSol.append(nums1[p1])
                p1+=1
                continue
            if nums1[p1] < nums2[p2]:
                numSol.append(nums1[p1])
                p1+=1
            else:
                numSol.append(nums2[p2])
                p2+=1
        if len_mix % 2 == 0:
            return((numSol[-1]+numSol[-2])/2)
        else:
            return numSol[-1]    