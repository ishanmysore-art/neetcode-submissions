# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        while head and head.next:
            firstNode, nextNode, prevNode = head, head.next, None
            while head.next:
                prevNode = head
                head = head.next
            prevNode.next = None
            firstNode.next = head

            if head == nextNode:
                break

            head.next = nextNode
            head = head.next