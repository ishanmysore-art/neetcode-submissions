# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # find the middle of the linkedlist
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the linkedlist
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # merge two lists
        while prev:
            prev_rest = prev.next
            head_rest = head.next
            head.next = prev
            prev.next = head_rest
            head = head_rest
            prev = prev_rest
            
            