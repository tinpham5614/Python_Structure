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
def solution(head, x: int):
  beforeHead = before = ListNode(0)
  afterHead = after = ListNode(0)
  while head:
    if head.val < x:
      before.next = head
      before = before.next
    else:
      after.next = head
      after = after.next
      
    head = head.next
    
  before.next = afterHead.next
  after.next = None
  return beforeHead.next
  
  

#test case
#list 1
head = ListNode(1)
temp = head
for value in [4,3,2,5,2]:
  temp.next = ListNode(value)
  temp = temp.next

#list 2
head2 = ListNode(2)
temp = head2
for value in [3,4,3,5,6]:
  temp.next = ListNode(value)
  temp = temp.next
print(solution(head, 3))


