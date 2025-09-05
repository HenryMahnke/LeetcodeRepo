from Node import Node


class LinkedList:
    def __init__(self, vals_for_list):
        next = None
        self.head = Node(vals_for_list[0], None)

        cur = self.head
        for i in range(0, len(vals_for_list) - 1):
            cur.next = Node(vals_for_list[i + 1], None)
            cur = cur.next

    @staticmethod
    def printLinkedList(head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
