class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        current = None # previous node
        while head:
            nextNode = head.next
            head.next = current
            current = head
            head = nextNode
        return current
