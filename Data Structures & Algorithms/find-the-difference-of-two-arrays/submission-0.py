class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set()
        s2=set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                continue
            else:
                s1.add(nums1[i])    
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                continue
            else:
                s2.add(nums2[i])   
        return [list(s1),list(s2)]         
        