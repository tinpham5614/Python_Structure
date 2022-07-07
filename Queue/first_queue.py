class LinkedListNode:

  def __init__(self, val):
    self.val = val
    self.next = None

class Queue:

  def __init__(self):
    self._head = None
    self._tail = None
    self._len = 0

  def enqueue(self, val):
    new_lln = LinkedListNode(val)
    if not self._len:
      self._len += 1
      self._head = new_lln
      self._tail = new_lln
      return
    self._len += 1
    self._tail.next = new_lln
    self._tail = new_lln

  def dequeue(self):
    if not self._len:
      raise ValueError('Cannot dequeue from empty queue!')
    self._len -= 1
    val = self._head.val
    self._head = self._head.next
    return val

  def __repr__(self):
    if not self._len:
      return 'Empty queue!'
    vals = []
    temp = self._head
    while temp is not None:
      vals.append(str(temp.val))
      temp = temp.next
    return ' -> '.join(vals)

k = 3
running_total = 0
q = Queue()
for user_input_num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
  running_total += user_input_num
  q.enqueue(user_input_num)
  if q._len > k:
    running_total -= q.dequeue()
  print('Current Queue: ' + str(q))
  print('Running Average: ' + running_total / q._len)
