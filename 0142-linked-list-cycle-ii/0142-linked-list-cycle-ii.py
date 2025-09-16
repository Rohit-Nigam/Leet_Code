# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        map={}
        temp=head
        timer=0
        while temp:
            if temp in map:
                return temp
            map[temp]=timer
            timer+=1
            temp=temp.next
        return None