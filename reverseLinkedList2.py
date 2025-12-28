"""
Docstring for reverseLinkedList2
in preparation for doing amuch harder puzzle, i reminded myself of how to do 
reversal of a linked list from first principles, it took me longer than i wish to admit 
but is a good thing to recap to get it back into mind.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        while head: 
            newhead = head.next 
            head.next = prev 
            prev = head 
            head = newhead
        return prev