# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getlength(head):
            curr,length=head,0
            while curr!=None:
                curr=curr.next
                length=length+1
            return length
        counter=getlength(head)
        curr=head
        for i in range(counter//2):
            curr=curr.next
        return curr