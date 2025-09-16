# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find(self, temp: Optional[ListNode], k: int):
            cnt=0
            while(temp and cnt<k):
                if cnt==k:
                    return temp
                cnt+=1
                temp=temp.next
            return temp
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        l=1
        tail=head
        while(tail.next):
            l+=1
            tail=tail.next
        k=k%l
        if k%l==0:
            return head
        tail.next=head
        newnode=self.find(head,l-k-1)
        head=newnode.next
        newnode.next=None
        return head