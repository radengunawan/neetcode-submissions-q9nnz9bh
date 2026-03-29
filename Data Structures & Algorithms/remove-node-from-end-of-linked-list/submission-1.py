# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        dumi = ListNode(0,head)

        L, R = dumi, head

        i = 0
        while (i < n):
            R = R.next
            i +=1

        while (R):
            L = L.next
            R = R.next
        
        #if (L.next.next):
        L.next = L.next.next
        #else:
         #   L.next = None

        return dumi.next
        