# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        ans=[]
        if root==None: return ans
        flag=True
        while(q):
            size=len(q)
            level=[]
            for i in range(size):
                root=q.popleft()
                level.append(root.val)
                if root.left!=None:
                    q.append(root.left)
                if root.right!=None:
                    q.append(root.right)

            if not flag:
                level.reverse()
            ans.append(level)
            flag = not flag
        return ans
