# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1 
        l2 = list2 
        head = None 
        cur = None 
        if not l1: 
            return l2 
        if not l2: 
            return l1
        while l1 and l2:
            nx = None
            if l1.val < l2.val: 
                nx = l1 
                l1 = l1.next
            else: 
                nx = l2 
                l2 = l2.next 
            if not head: 
                head = nx 
                head.next = None
                cur = head 
            else: 
                cur.next = nx 
                cur = cur.next 
        #cleanup 
        while l1:
            cur.next = l1 
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2 
            l2 = l2.next
            cur = cur.next
        return head

