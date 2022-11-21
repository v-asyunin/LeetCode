# Definition for singly-linked list.
from typing import Optional

# третий вариант алгоритма с сайта
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

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

l = Solution().addTwoNumbers(X4, Y4)

while l:
     print(l.val)
     l = l.next
