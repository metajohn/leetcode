#Linked List pseudocode 

"""
class Node
    int val
    *Node next

class LL
    *Node head
    *Node tail

    def insert_head(value)
        if head is null
            head = new *Node(value, null)
            tail = head # if the head is empty, so is the tail
            return

        self.head = new *Node(value, self.head) 

    def insert_tail(value)
        if tail is null
        # if the tail is empty, so is the head
            head = new *Node(value, null)
            tail = head 
            return

        *Node old_tail = self.tail # store a reference to the current tail
        self.tail = new *Node(value, null) # create a new tail
        old_tail->next = self.tail
"""