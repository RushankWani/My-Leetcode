class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(),nums2.sort()
        set1=[]
        if len(nums1)>len(nums2):
            for i in range(0,len(nums2)):
                if nums2[i] in nums1:
                    set1.append(nums2[i])
                    nums1.remove(nums2[i])
        else:
            for i in range(0,len(nums1)):
                if nums1[i] in nums2:
                    set1.append(nums1[i])
                    nums2.remove(nums1[i])
        return set1        