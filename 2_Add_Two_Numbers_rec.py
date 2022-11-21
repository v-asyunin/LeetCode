# Definition for singly-linked list.
from typing import Optional

# второй вариант алгоритма через рекурсию
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

X = ListNode(2, ListNode(4, ListNode(3)))
Y = ListNode(5, ListNode(6, ListNode(4)))

# X = ListNode(7, ListNode(1))
# Y = ListNode(3, ListNode(2))
#
X3 = ListNode(0)
Y3 = ListNode(0)

X4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
Y4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

Y5 = ListNode(1)

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

l = f(X4, Y4, 0)[0]
# print(l.val, l.next)

while l:
     print(l.val)
     l = l.next
