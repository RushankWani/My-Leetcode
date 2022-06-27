# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA=headA
        currB=headB
        def length(currA,currB):
            countA,countB=0,0
            while currA:
                countA+=1
                currA=currA.next
            while currB:
                countB+=1
                currB=currB.next
            return countA , countB
        A,B=length(currA,currB)
        print(A)
        print(B)
        if A>B:
            diff=A-B
            while currA!=None and diff>0:
                currA=currA.next
                diff-=1
        else:
            diff=B-A
            while currB!=None and diff>0:
                currB=currB.next
                diff-=1
        # print(currA)
        # print(currB)
        while currA and currB:
            if currA==currB:
                return currA
            else:
                currA,currB=currA.next,currB.next
            
            
            