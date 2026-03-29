# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # two pointers
        prev, curr = None, head

        #while curr is not null
        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        