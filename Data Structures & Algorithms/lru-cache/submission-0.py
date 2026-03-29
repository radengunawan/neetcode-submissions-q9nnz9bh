class Node:
    def __init__ (self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node

        #Dummy head and tail
        self.head = Node (0,0)
        self.tail = Node (0,0)

        #Connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    #Helper: remove node from DLL
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: #if modify
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            #if insert new -> 1. create, 2. update link
            new_node = Node(key,value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

            if len (self.cache) > self.capacity:
                #evict least: node attached to tail
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#https://leetcode.com/problems/lru-cache/