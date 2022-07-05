#creating Node class
class ListNode:
  def __init__(self, val:int):
    self.next = None
    self.val = val
  def __repr__(self):
    if not self.next:
      return str(self.val)
    return f'{self.val} -> {self.next.__repr__()}'

#start coding here
def solution(head, position: int):
  node = ListNode(3)
  if head is None:
    head = node
    return head
  
  curr = head
  counter = 1
  
  while curr.next:
    counter += 1
    curr = curr.next
    if counter == position:
      node.next = curr.next
      curr.next = node
  return head
  
  

#test case
#list 1
head = ListNode(11)
temp = head
for value in [9,2,9]:
  temp.next = ListNode(value)
  temp = temp.next

#list 2
head2 = ListNode(20)
temp = head2
for value in [6,2,19,7,4,15,9]:
  temp.next = ListNode(value)
  temp = temp.next
print(solution(head,2))
print(solution(head2,3))

