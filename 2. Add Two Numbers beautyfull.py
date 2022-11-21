# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ''
        l = self
        while l:
            s += str(l.val)
            l = l.next
        return s

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # третий вариант алгоритма с сайта
        root = ListNode(0)
        result = root
        excess = 0
        while l1 or l2 or excess:
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next

            result.next = ListNode(excess % 10)
            result = result.next
            excess = excess // 10

        return root.next

X = ListNode(2, ListNode(4, ListNode(3)))
Y = ListNode(5, ListNode(6, ListNode(4)))
print('X=', str(X)[::-1], ', Y=', str(Y)[::-1], ', ans =', str(Solution().addTwoNumbers(X, Y))[::-1])

X = ListNode(0)
Y = ListNode(0)
print('X=', str(X)[::-1], ', Y=', str(Y)[::-1], ', ans =', str(Solution().addTwoNumbers(X, Y))[::-1])

X = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
Y = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
print('X=', str(X)[::-1], ', Y=', str(Y)[::-1], ', ans =', str(Solution().addTwoNumbers(X, Y))[::-1])

Y = ListNode(1)
print('X=', str(X)[::-1], ', Y=', str(Y)[::-1], ', ans =', str(Solution().addTwoNumbers(X, Y))[::-1])
