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
  
  def peek(self): # create a function that return the value of the top but do not remove it
    return self._stack[len(self._stack)-1]
  
  def size(self): # create a function that return the length of the stack
    return len(self._stack)
  
