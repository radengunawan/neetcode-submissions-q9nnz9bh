class MyStack:

    def __init__(self):
        self.myQueue = None
        
    def push(self, x: int) -> None:
        self.myQueue = deque([x, self.myQueue])      

    def pop(self) -> int:
        top = self.myQueue.popleft()
        self.myQueue = self.myQueue.popleft()
        return top

    def top(self) -> int:
        return self.myQueue[0]
        
    def empty(self) -> bool:
        return not self.myQueue
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()