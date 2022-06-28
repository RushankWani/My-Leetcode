# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        dict1=[]
        while curr:
            if curr in dict1:
                return True
            # dict1[curr]=True
            dict1.append(curr)
            curr=curr.next
            
        