class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.height(root.left) 
        r = self.height(root.right)
        return 1 + max(l, r)    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh - rh) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)