# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=-math.inf
    def check(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        lh = max(0, self.check(root.left))
        rh = max(0, self.check(root.right))
        self.ans=max(self.ans,lh+rh+root.val)
        return root.val+max(lh,rh)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.check(root)
        return self.ans