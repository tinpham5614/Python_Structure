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
  #create previous node
  prev = None
  # assign current node becomes head
  curr = head
  #create counter
  counter = 0
  if position == 0:
    head = head.next
    return head
  #loop through the llist
  while curr:
    #if the position equal to counter (target position)
    if counter == position:
      prev.next = curr.next #point to the next node
    else: #otherwise
      prev = curr #stay the same position
    counter += 1 #increase to reach the target position
    curr = curr.next #runs the loop
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


head3 = ListNode(11)
temp = head3
for value in [12,8,18,16,5,18]:
  temp.next = ListNode(value)
  temp = temp.next
print(solution(head,1))
print(solution(head2,3))
print(solution(head3,0))

