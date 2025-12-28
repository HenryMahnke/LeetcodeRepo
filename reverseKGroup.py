# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def printLinkedList(newVal):
            while newVal:
                print(newVal.val, end=" ")
                newVal = newVal.next
            print()

        def findStart(head):
            start = head
            for i in range(k):
                if start:
                    start = start.next
            return start

        def findEnd(start):
            end = start
            for i in range(k - 1):
                if end:
                    end = end.next
            return end

        # start of algorithm
        start = findStart(head)
        end = findEnd(head)
        # the new place the llist will start at/be returned
        NewStartPtr = findEnd(head)
        if not NewStartPtr:
            return None
        print(NewStartPtr.val)
        while end:
            end = findEnd(start)
            # if end is null here
            prev = end
            if start and not end:
                prev = start
            while head != start:
                print("in reversal loop")
                newhead = head.next
                head.next = prev
                prev = head
                head = newhead
                printLinkedList(head)
            print("from NewStartPtr print: ")
            printLinkedList(NewStartPtr)
            start = findStart(head)
        return NewStartPtr


# This problem was not very challenging in the sense of having to use really complicated data strucutres or know certain tricks
# but quite challenging in just the amount of mental resources you ahd to put in to understand the problem and how to get around it. 
# much of it extends from just extending the capability of the normal reverse linked list algorithm, which is why i reviewed that from first 
# principles last night. I was very very proud of coming up with this solution. I used no outside resources, just lots of mental brain power.
# i liked this problem probably the most out of all of the problems I've done so far because it didn't require some stupid trick that relies on you 
# likely having seen the problem before (yes, that's a skill issue, and why I"m pracicitng, but find those problems don't use a lot of fluid intelligence, but rather, knowledge)
