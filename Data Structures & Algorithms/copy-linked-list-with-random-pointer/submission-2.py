"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        list_nodes = []
        current = head
        while (current):
            list_nodes.append(current)
            current = current.next
        
        list_nodes2 = []
        for i in range (len(list_nodes)):
            node_val = list_nodes[i].val
            new_node = Node(node_val)
            list_nodes2.append(new_node)

        i = 0
        while (i <= len(list_nodes2) -2):
            list_nodes2[i].next = list_nodes2[i+1]
            i += 1

        list_nodes2[-1].next = None

        for i in range (len(list_nodes)):
            random = list_nodes[i].random
            for j in range (len(list_nodes)):
                if random == list_nodes[j]:
                    list_nodes2[i].random = list_nodes2[j]
        
        return list_nodes2[0]
