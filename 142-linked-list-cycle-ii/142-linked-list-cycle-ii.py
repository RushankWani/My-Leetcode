# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        dict1={}
        count=0
        while curr:
            if curr in dict1:
                return curr
            count+=1
            dict1[curr]=count
            # dict1.append(curr)
            curr=curr.next
        