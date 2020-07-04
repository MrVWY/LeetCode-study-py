# 返回倒数第 k 个节点

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        p = head
        while k > 0:
            p = p.next
            k -= 1

        while p:
            p = p.next
            head = head.next
        return head.val
