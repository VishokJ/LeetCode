# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dupFound = False
        dummy = ListNode(0, head)
        slow = dummy
        while head:
            while head.next and head.next.val == head.val:
                dupFound = True
                head.next = head.next.next
            if dupFound:
                slow.next = head.next
            else:
                slow = slow.next
            head = head.next
            dupFound = False
        return dummy.next