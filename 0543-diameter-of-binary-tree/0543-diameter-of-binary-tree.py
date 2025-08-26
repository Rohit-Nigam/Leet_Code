# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def check(self, root: Optional[TreeNode],ans:int) -> int:
        if root==None:
            return 0
        lh=self.check(root.left,self.ans)
        rh=self.check(root.right,self.ans)
        self.ans=max(self.ans,lh+rh)
        return 1+max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.check(root,self.ans)
        return self.ans