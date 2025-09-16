# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #digit 123 is stored as 3->2-1 in a linked list that is "number 1" 
        def getDigit(lnk):
            cur = lnk 
            #all we really want to do is keep a count, and then make teh digit 
            #we can make the digit by doing string appending whcih would be faster than carrying
            #a count and doing powers once we get to big numbers, and becuase this might be a real method used by 
            #massive numbers you wouldn't be able to store them with binary anyways becuase they would be too large 
            digit = ""
            while cur:
                print(cur.val) 
                digit = str(cur.val) + digit
                print(digit) 
                cur = cur.next
            print(digit) 
            return digit
        d1 = getDigit(l1)
        d2 = getDigit(l2)
        d1 = int(d1) 
        d2 = int(d2)
        total = d1 + d2 
        total = str(total)
        total = total[::-1]
        print("the total is", total)
        #then we just need to convert this to a list 
        newList = None
        running = None
        if len(total) == 1:
            return ListNode(int(total[0]),None)
        for i in range(len(total)-1): 
            if not newList: 
                newList = ListNode(int(total[i]),ListNode(int(total[i+1]),None))
                running = newList 
                running = running.next
            else: 
                running.next = ListNode(total[i+1],None)
                running = running.next
        #then we have to reform the list 
        return newList


        # is another way to do this with a carry digit
        #and traversing both at the same time.
