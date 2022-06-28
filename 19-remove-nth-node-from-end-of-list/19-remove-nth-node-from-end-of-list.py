# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        diff=count-n-1
        prev=head
        nxt=head.next
        if count==n:
            prev=nxt
            return head.next
        while diff!=0:
            prev=nxt
            nxt=nxt.next
            diff-=1
        prev.next=nxt.next
        return head

#         count2=1
#         curr1=ListNode()
#         curr2=curr1
#         curr=head
#         # if diff==0:
#         #     return curr1.next
#         while curr!=None:
#             if count2==diff:
#                 nxt=curr.next
#                 curr=nxt
#                 count2+=1
#             else:
#                 nxt=curr.next
#                 curr2.next=curr
#                 curr,curr2=nxt,curr
#                 count2+=1         
#         return curr1.next

                
        