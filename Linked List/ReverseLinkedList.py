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
def solution(head):
  
  if head is None: # return if head is null
    return None
  
  curr = head # assign current node is head node
  prev = None # assign previous node is None
  temp = None # assign next node is None
  while curr: # while loop to iterate
    temp = curr.next # assign next node to the curr next 
    curr.next = prev # pointing the curr node to previous node
    prev = curr #prev node becomes curr node
    curr = temp #curr node is next node now
  head = prev #refer the previous is head
  return head

#test case
#list 1
head = ListNode(1)
temp = head
for value in [2,3,4]:
  temp.next = ListNode(value)
  temp = temp.next

#list 2
head2 = ListNode(2)
temp = head2
for value in [3,4,3,5,6]:
  temp.next = ListNode(value)
  temp = temp.next
print(solution(head))
print(solution(head2))

