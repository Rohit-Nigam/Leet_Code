class Solution:
    def leftheight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.leftheight(root.left) 
        r = self.leftheight(root.right)
        return 1 + max(l, r)    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        lh = self.leftheight(root.left)
        rh = self.leftheight(root.right)
        if abs(lh - rh) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)