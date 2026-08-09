class DoublyLinkedList:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next 
        self.prev = prev
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedList(tokens[0])
        curr = head 
    
        for i in range(1, len(tokens)):
            curr.next = DoublyLinkedList(tokens[i], prev=curr)
            curr = curr.next 
        
        while head is not None:
            if head.data in "+-*/":
                l = int(head.prev.prev.data)
                r = int(head.prev.data)
                if head.data == "+":
                    res = l + r
                elif head.data == "-":
                    res = l - r
                elif head.data == "*":
                    res = l * r
                elif head.data == "/":
                    res = int(l / r)
                
                head.data = str(res)
                head.prev = head.prev.prev.prev
                if head.prev is not None:
                    head.prev.next
                    ext = head 

            ans = int(head.data)
            head = head.next 
        return ans 