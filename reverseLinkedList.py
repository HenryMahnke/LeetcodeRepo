import Node
from linkedListBuilder import LinkedList


def reverse(head):
    cur = head
    next = cur.next
    cur.next = None
    while next:
        print("cur", cur.val)
        print("next", next.val)
        nextNext = next.next
        next.next = cur
        cur = next
        next = nextNext
    print(cur.val)
    print("reversed: ")
    LinkedList.printLinkedList(cur)

def reverse_canonical(head): 
    prev = None 
    cur = head 
    while cur: 
        print("cur", cur.val) 
        nxt = cur.next 
        print("nxt",nxt)
        cur.next = prev
        prev = cur 
        cur = nxt 
    LinkedList.printLinkedList(prev)
    return prev



newLinkedList = LinkedList([1, 2, 3, 4, 5])
head = newLinkedList.head
cur = head
# LinkedList.printLinkedList(head)
reversedList = reverse_canonical(head)
LinkedList.printLinkedList(reversedList)
