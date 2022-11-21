# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        l3 = ListNode()
        root = l3

        while l3:
            if list1.val <= list2.val:
                l3.next = list1
                l3 = list1
                list1 = list1.next
            else:
                l3.next = list2
                l3 = list2
                list2 = list2.next

        return l3

x = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = x.mergeTwoLists(l1, l2)

while l1:
    print(l1.val, sep=' ', end=' ')
    l1 = l1.next
print('')
while l2:
    print(l2.val, sep=' ', end=' ')
    l2 = l2.next
print('')
while l3:
    print(l3.val, sep=' ', end=' ')
    l3 = l3.next

