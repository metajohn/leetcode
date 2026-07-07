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

    def remove(value) -> bool
        if self.head is null
            return False
        
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, vals=None):
        self.head = None

        if vals:
            last_node = None
            for v in vals:
                new_node = Node(v)
                if self.head_node is None:
                    self.head = new_node
                    last_node = new_node
                else:
                    last_node.next = new_node
                    last_node = new_node

    def insert_head(self, val):
        self.head = Node(val, self.head)

    def insert_tail(self, val):
        if self.head is None:
            self.head = Node(val, self.head)
            return

        node = self.head
        while node.next is not None:
            node = node.next
            
        new_tail = Node(val)
        node.next = new_tail
        

    def remove(val):
        pass

