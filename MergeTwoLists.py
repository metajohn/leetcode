from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # gets the smallest node, the next node from that list, updating both nodes for the sake of consistency
    # the alternative would involve an extra variable like boolean, List1Smaller, or smallerNodeIndex (assuming 0 for list1 and 1 for list 2)
    # because only this function knows which node was smaller we must assume that MAIN is dumb, but, given that this is for a linked list, the memory cost seems acceptable
    def getSmallestNode(self, list1, list2):
        if not list1 or not list2:
            if not list1:
                smallest_node = list2 #repeat movement and assigment to avoid passing ptrs to a small function
                list2 = list2.next
            else:
                smallest_node = list1
                list1 = list1.next
            return list1, list2, smallest_node
        if list1.val <= list2.val:
            smallest_node = list1
            list1 = list1.next
        else:
            smallest_node = list2
            list2 = list2.next
        return list1, list2, smallest_node
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        list1, list2, mergelist_head = self.getSmallestNode(list1, list2)
        last_node = mergelist_head

        while list1 or list2:
            list1, list2, smallest_node = self.getSmallestNode(list1, list2)
            last_node.next = smallest_node
            smallest_node = last_node
        return mergelist_head