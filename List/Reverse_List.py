# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 92. 反转链表 II
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        prev, cur = None, head
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        first, secend = prev, cur
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        if first:
            first.next = prev
        else:
            head = prev
        secend.next = cur
        return head
