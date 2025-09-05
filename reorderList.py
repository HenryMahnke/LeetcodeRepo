# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printList(head):
            cur = head 
            while cur: 
                print(cur.val, end = " ") 
                cur = cur.next
            print()
        l = head
        r = head
        if not head.next:
            return 
        while r and r.next: 
            print(l.val,r.val)
            l = l.next 
            if not r.next.next: 
                r = r.next 
            else:
                r = r.next.next
        #now l should be at the middle and r at the end 
        print("rval and next", r.val, r.next)
        print(head) 
        print("l val and next", l.val, l.next.val)
        #starting from l.next we want to reverse 
        start = l.next
        print("start", start.val)
        cur = start 
        prev = None 
        while cur: 
            next_node= cur.next 
            cur.next = prev 
            prev = cur 
            cur = next_node
            print("prev", prev.val)
        print("printing prev")
        print(prev.val)
        printList(prev) 
        print(head, head.next.val, head.next.next.val, head.next.next.next)
        #now the start of the reversed list is at prev 
        #now we just need to merge the two lists 
        # and we want to unlink l from the end 
        l.next = None 
        #so head is now from head to l 
        # and prev is from end of list to l+1 of the original 
        l1 = head 
        l2 = prev
        print("printing head")
        printList(head)
        # printList(prev)
        while l1 and l2:
            print("l1", l1.val)
            print("l2", l2.val)
            l1Next = l1.next 
            l2Next = l2.next
            l1.next = l2
            l1.next.next = l1Next
            l1 = l1Next 
            l2 = l2Next
            # printList(head)