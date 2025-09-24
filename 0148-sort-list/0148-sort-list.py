# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1: Optional[ListNode],list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr=dummy
        while list1 and list2:
            if list1.val > list2.val:
                curr.next=list2
                list2=list2.next
            else:
                curr.next=list1
                list1=list1.next
            curr=curr.next
        if list1:
            curr.next=list1
        elif list2:
            curr.next=list2
        return dummy.next
    def middle(self,head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head.next
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid=self.middle(head)
        lefthead=head
        righthead=mid.next
        mid.next=None
        lefthead=self.sortList(lefthead)
        righthead=self.sortList(righthead)
        return self.merge(lefthead,righthead)