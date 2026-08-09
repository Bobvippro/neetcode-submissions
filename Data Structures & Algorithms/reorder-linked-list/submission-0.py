# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 
        #find middle
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        #split linklist
        second = slow.next
        slow.next = None
        #reverse second half
        prev_node = None
        current_node = second 
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        second = prev_node
        #merge ziczac
        first = head

        while second is not None:
            temp1 = first.next 
            temp2 = second.next

            first.next = second
            second.next = temp1 

            first = temp1
            second = temp2 





