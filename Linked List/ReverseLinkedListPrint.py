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
  #head is null return None
  if head is None:
    return None
  #create prev node
  prev = None
  #while loop through the llist from head
  while head:
    curr = head #assign curr becomes head
    head = head.next #move head forward
    curr.next = prev #curr node points to prev node
    prev = curr #prev node becomes curr node
  return prev
 
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

