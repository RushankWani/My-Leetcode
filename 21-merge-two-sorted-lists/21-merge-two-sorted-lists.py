# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        curr3=ListNode()
        head=curr3
        
        while curr1 and curr2:
            if curr1.val<curr2.val:
                head.next=curr1
                curr1,head=curr1.next,curr1
            else:
                head.next=curr2
                curr2,head=curr2.next,curr2
        
        if curr1 or curr2:
            head.next=curr1 if curr1 else curr2
        
        return curr3.next