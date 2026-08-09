# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#we have 2 ways to solve this problem
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        current = head
        while current:
            length += 1
            current = current.next


        target = (length - n + 1)
        if target == 1:
            return head.next
            # Traverse to the node just before the target node
        current = head
        for _ in range(target - 2):
            current = current.next
            
        current.next = current.next.next
        return head
        

    