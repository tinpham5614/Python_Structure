#Stack a bunch of stuff, LAST IN - FIRST OUT (LIFO)
#two basic operations - PUSH and POP
# push == add, pop == delete
class Stack:
  def __init__(self): # create an empty stack
    self._stack = []
    
  def push(self, x): # create adding function
    return self._stack.append(x)
    
  def pop(self): # create remove function
    return self._stack.pop()
  
  def peek(self): # create checking the last item but do not remove that item
    return self._stack[len(self._stack)-1]
  
  def size(self): # create the length function of the stack
    return len(self._stack)
  
