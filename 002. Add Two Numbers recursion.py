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

        # сложный для понимания алгоритм, зато через рекурсию и работает

        def NoneF(a) -> int:
            if a is None:
                return 0
            else:
                return a.val

        def f(l1, l2, k):

            if l1.next is None and l2.next is None:
                if (k + l1.val + l2.val) // 10 == 0:
                    return ListNode(k + l1.val + l2.val), 0
                else:
                    return ListNode( (k + l1.val + l2.val) % 10, ListNode((k + l1.val + l2.val) // 10) ), 0
            else:
                if l1.next is None:
                    l1.next = ListNode()
                if l2.next is None:
                    l2.next = ListNode()

            if (k + l1.val + l2.val) // 10 == 0:
                return ListNode(k + l1.val + l2.val, f(l1.next, l2.next, 0)[0]), 0
            else:
                return ListNode( (k + l1.val + l2.val) % 10, f(l1.next, l2.next, (k + l1.val + l2.val) // 10)[0] ), (k + l1.val + l2.val) // 10

        return f(l1, l2, 0)[0]

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
