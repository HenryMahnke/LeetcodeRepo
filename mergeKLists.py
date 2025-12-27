class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            outputHead = ListNode()
            output = outputHead
            while l1 and l2:
                if l1.val < l2.val:
                    output.next = ListNode(l1.val,None)
                    l1 = l1.next
                    output = output.next
                else:
                    output.next = ListNode(l2.val,None)
                    l2 = l2.next 
                    output = output.next 
                # print(output.val)
            while l1:
                output.next = ListNode(l1.val,None)
                l1 = l1.next 
                output = output.next 
            while l2: 
                output.next = ListNode(l2.val,None)
                l2 = l2.next 
                output = output.next
            # print(outputHead.val)
            return outputHead.next

        def printLinkedList(newVal):
            while newVal: 
                print(newVal.val, end = " ")
                newVal = newVal.next
        def printListofLinkedLists(llist):
            for i in range(len(llist)): 
                printLinkedList(llist[i])
                print()

        # want to merge nearest neighbors
        outputList = lists
        while len(outputList) > 1:
            i = 0
            listLen = len(outputList)
            newList = []
            while i+1 < listLen:
                newList.append(merge2Lists(outputList[i],outputList[i+1]))
                i+=2
            # account for odd case
            if i < listLen:
                newList.append(outputList[i])
            outputList = newList
            printListofLinkedLists(outputList)
            print(outputList)
        if outputList:
            return outputList[0]
        else:
            return None