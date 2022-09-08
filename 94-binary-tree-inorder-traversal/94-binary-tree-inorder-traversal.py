# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # output=[]
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     output.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return output
        op=[]
        stack=[]
        curr=root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr = stack.pop()
            op.append(curr.val)
            curr=curr.right
        return op
        # op=[]
        # def lefty(root):
        #     if not root:
        #         return
        #     op.append(root.val)
        #     lefty(root.left)
        # lefty(root)
        # return op
        