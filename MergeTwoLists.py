from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def getSmallestNode(self, list1, list2):
        if not list1 or not list2:
            if not list1:
                smallest_node = list2
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