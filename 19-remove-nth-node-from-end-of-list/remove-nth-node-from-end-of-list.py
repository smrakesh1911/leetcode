# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 





class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        if head is None:
            return None

        # Find length
        curr = head
        l = 0

        while curr != None:
            l += 1
            curr = curr.next

        # If removing the first node
        if n == l:
            return head.next

        # Go to node before the target
        curr = head

        for i in range(l - n - 1):
            curr = curr.next

        # Remove node
        curr.next = curr.next.next

        return head


        
         