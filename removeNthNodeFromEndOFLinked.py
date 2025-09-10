# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head 
        length = 1
        while cur.next:
            cur = cur.next
            length +=1
        #then iterate through to remove the nth from the end 
        print(length)
        nodeToRem = length -n + 1
        print(nodeToRem)
        curCount = 1 
        cur = head 
        prev = None
        if nodeToRem <= 0: 
            return None
        while curCount < nodeToRem:
            prev = cur 
            cur = cur.next 
            curCount +=1
        if prev:
            if cur:
                prev.next = cur.next
            else: 
                prev.next = None
        else: 
            head = cur.next
        return head
            