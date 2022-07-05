class ListNode:
  def __init__(self, val:int):
    self.next = None
    self.val = val
  def __repr__(self):
    if not self.next:
      return str(self.val)
    return f'{self.val} -> {self.next.__repr__()}'

def remove_elements(head):
  #Scan the linked list
  #while we scan, we need to see if current.val = val 
  #if we need to remove current node, we need to keep track of previous

  seen = set()
  prev = None
  curr = head
  
  while curr:
    if curr.val in seen:
        prev.next = curr.next
    else:
        seen.add(curr.val)
        prev = curr
    curr = curr.next   
  return head

  
head = ListNode(1)
temp = head

for value in [2,6,3,4,6,5,6]:
  temp.next = ListNode(value)
  temp = temp.next

print(remove_elements(head))
