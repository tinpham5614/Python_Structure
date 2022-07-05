#Stack a bunch of stuff, LAST IN - FIRST OUT (LIFO)
#two basic operations - PUSH and POP
# push == add, pop == delete
class MinStack:
  def __init__(self):
    self._stack = []
  def push(self, x):
    self._stack.append(x)
  def pop(self):
    return self._stack.pop()
  def peek(self):
    return self._stack.peek()
  
