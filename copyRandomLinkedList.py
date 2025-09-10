"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}
        cur = head 
        while cur: 
            m[cur] = Node(cur.val,None,None)
            cur = cur.next 
        print(m)
        cur = head 
        newList = None
        running = None
        while cur: 
            newNode = m[cur]
            newNode.next = m.get(cur.next,None)
            newNode.random = m.get(cur.random,None)
            if not newList: 
                newList = newNode 
                running = newNode
            else: 
                running.next = newNode
                running = running.next
            cur = cur.next 
        # pr = newList 
        # while pr: 
        #     print(pr.val, pr.next,pr.random)
        #     pr = pr.next
        return newList


            
