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
    def addTwoNumbers(self, X: Optional[ListNode], Y: Optional[ListNode]) -> Optional[ListNode]:

        # алгоритм на основе ограничения длины чисел и разложения числа по разрядам

        # вычисляем первое число
        x = 0
        i = 0
        while X:
            x += X.val*(10**i)
            i += 1
            X = X.next

        # вычисляем второе число
        y = 0
        i = 0
        while Y:
            y += Y.val*(10**i)
            i += 1
            Y = Y.next

        # складываем
        z = x + y
        Z = z

        # считаем сколько разрядов (не более 100 по условию)
        for s in range(101):
            if z // (10**(100-s)) != 0:
                break
        r = 100 - s

        # строим список для суммы
        l = ListNode(z//10**r)
        z -= (10**r)*(z//10**r)
        for k in range(r):
            l = ListNode(z//10**(r-1-k), l)
            z -= (10**(r-1-k))*(z // 10 ** (r-1-k))

        return l

X = ListNode(2, ListNode(4, ListNode(3)))
Y = ListNode(9, ListNode(6, ListNode(6, ListNode(8, ListNode(4)))))
print('X=', str(X)[::-1], ', Y=', str(Y)[::-1], ', ans =', str(Solution().addTwoNumbers(X, Y))[::-1])

X = ListNode(7, ListNode(1))
Y = ListNode(3, ListNode(2))
print('X=', str(X)[::-1], ', Y=', str(Y)[::-1], ', ans =', str(Solution().addTwoNumbers(X, Y))[::-1])
