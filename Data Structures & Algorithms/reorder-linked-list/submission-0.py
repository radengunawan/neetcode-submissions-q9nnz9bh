# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # go to middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # start with the second part and handle it
        current_node = slow.next

        # we will reverse link and traversing, so initiate head
        reverse_head = None

        #cut ties with first part:
        slow.next = None

        # while current_node not point to None:
        while current_node:
            # always put next node on separate var in link change
            next_node = current_node.next

            # reverse next node of current node to reverse_head
            current_node.next = reverse_head

            # move reverse_head pointer to place referenced by current_node
            reverse_head = current_node

            # move current_node to the place referenced by next_node 
            current_node = next_node

        # loop finished with final conditions:
        # current_node = None, reverse_head = last node

        # last part: merge first part and second part:
        L, R = head, reverse_head

        # using S&F pointer, second part will never be greater than first part
        while (R):
            # because we will break link, always safe next_node reference
            next_node1, next_node2 = L.next, R.next

            #link next pointer of current L to R
            L.next = R

            #link next pointer of current R to previous existing next of L
            R.next =  next_node1

            # now R has move and become part 1
            # now next_node2 is unreferenced but exist
            # it's time to update L and R
            # L to right, R to left
            L = next_node1
            R = next_node2

