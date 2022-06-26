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
        if counter%2==0:
            mid=counter//2
        else:
            mid=counter//2
        curr=head
        for i in range(mid):
            curr=curr.next
        return curr