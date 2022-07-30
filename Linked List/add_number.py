class ListNode:
  def __init__(self, val:int):
    self.next = None
    self.val = val
  def __repr__(self):
    if not self.next:
      return str(self.val)
    return f'{self.val} -> {self.next.__repr__()}'

def add(l1,l2):
  #go through l1, l2
  carry = 0
  new_head = ListNode(0)
  new_curr = new_head
  while l1 is not None or l2 is not None:
    l1_val = 0
    if l1 is not None:
      l1_val = l1.val
    l2_val = 0
    if l2 is not None:
      l2_val = l2.val
    new_val = l1_val + l2_val + carry
    if new_val > 9:
      carry = 1
      new_val -= 10
    else:
      carry = 0
      new_col = ListNode(new_val)
      new_curr.next = new_col
      new_curr = new_col
    if l1:
      l1 = l1.next
    if l2:
      l2 = l2.next
  return new_head.next

l1 = ListNode(1)
temp = l1
for value in [2]:
  temp.next = ListNode(value)
  temp = temp.next
l2 = ListNode(3)
temp = l2
for value in [4]:
  temp.next = ListNode(value)
  temp = temp.next
print(add(l1,l2))
