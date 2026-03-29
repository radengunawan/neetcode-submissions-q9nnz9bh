class Node:
    def __init__ (self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None       # None <- Node (key,value) -> None


class LRUCache:

    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {} # e.g. {key1:value1, key2:value2, key3:value3}

        #Dummy head and tail
        self.head = Node(0,0)   # None <- head (0,0) -> None
        self.tail = Node(0,0)   # None <- tail (0,0) -> None

        #Connect head and tail
        self.head.next = self.tail # head -> tail,
        self.tail.prev = self.head # head <- tail, 
                                   # final: head <-> tail

    #Helper: remove node from DLL
    def _remove(self, currentNode: Node):
        # 1. Identify the node on the left and right side of current node
        leftNode = currentNode.prev   # leftNode <-> currentNode <-> rightNode
        rightNode = currentNode.next  

        # 2. connect leftNode to rightNode, leave the currentNode has no connection
        leftNode.next = rightNode   # Connect : leftNode -> rightNode
        rightNode.prev = leftNode   #         : leftNode <- rightNode 
                                    # final   : leftNode <-> rightNode 

    def _add_to_front(self, currentNode: Node): 
        currentNode.prev = self.head
        currentNode.next = self.head.next
        self.head.next.prev = currentNode
        self.head.next = currentNode
     
    def get (self, key:int) -> int:
        if key in self.cache: #1. assign node based on key (if exist), 2. move node to front
            extractedNode = self.cache[key]
            self._remove(extractedNode)
            self._add_to_front(extractedNode)
            return extractedNode.value
        return -1

    def put(self, key:int, value:int) -> None:
        if key in self.cache: #if modify
            extractedNode = self.cache[key]
            extractedNode.value = value
            self._remove(extractedNode)
            self._add_to_front(extractedNode)
        else:
            #if insert new -> 1. create, 2. update cache, 3. add to front
            new_node = Node (key,value)
            self.cache[key] = new_node  
            self._add_to_front(new_node)

            if len (self.cache) > self.capacity: #1. check capacity, 2. find LRU (node at tail), 3. remove LRU, 4. remove cache
                #evict least: node attached to tail
                lru = self.tail.prev
                self._remove(lru)
                #del self.cache[lru.key]
                self.cache.pop(lru.key, None)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # ➜ 1
lru.put(3, 3)      # ➜ evicts key 2
print(lru.get(2))  # ➜ -1
lru.put(4, 4)      # ➜ evicts key 1
print(lru.get(1))  # ➜ -1
print(lru.get(3))  # ➜ 3
print(lru.get(4))  # ➜ 4
'''
