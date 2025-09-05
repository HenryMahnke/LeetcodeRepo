# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head,head
        #here we advance slow 1 and fast 2
        #and if where slow = fast then we exit
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast: 
                return True
        return False
