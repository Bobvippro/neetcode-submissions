"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#way1: using hashing (hash map)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        curr = head

        while curr is not None:
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        #loop again 
        while curr is not None:
            newnode = hashmap[curr]

            newnode.next = hashmap.get(curr.next)
            newnode.random = hashmap.get(curr.random)

            curr = curr.next
            
        return hashmap.get(head)



