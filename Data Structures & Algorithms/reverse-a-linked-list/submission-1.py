# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 2nd approach: recursion
        ## edge case
        if not head:
            return None

        #base case part, part 1/2
        newHead = head
        if (head.next):
            # recursive case part
            newHead = self.reverseList(head.next) #recognize new global head
            head.next.next = head #point next node pointer to current node ("head")
            head.next = None # point next pointer of current node to None / Null
        return newHead #base case part, part 1/2

    '''
        # two pointers
        prev, curr = None, head

        #while curr is not null
        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        '''
        