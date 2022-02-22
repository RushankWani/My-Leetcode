#leetcode 88
#We used 3 pointers in this code. 
#we traversed backwards instead of forward approache bacause we cannot create #a temporary variable to store the list.


#most optimum solution {O(n),O(1)}

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #last index nums1
        last=m+n-1
        
        #merging in reverse order
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1
            
            #fill nums1 withover of nums2 
        while n>0:
            nums1[last]=num2[n-1]
            n-=1
            last-=1

#2 line solution
class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) ->None:
		nums1[m:] = nums2[:n]
		nums1.sort()