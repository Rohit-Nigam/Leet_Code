# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if (headA==None or headB==None):
            return None
        h1=headA
        h2=headB
        while(h1 != h2):
            h1=h1.next
            h2=h2.next
            if h1==h2:
                return h1
            if h1==None:
                h1=headB                
            if h2==None:
                h2=headA
        return h1