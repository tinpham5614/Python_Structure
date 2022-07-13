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
  if head is None: #if empty list, do nothing
    return None
  prev = head
  curr = head.next
  while curr.next: #scan from head to the tail. 
    curr = curr.next
    prev = prev.next
  prev.next = None #if after the last node is nothing -> point prev node to None (tail). 
  prev = curr #update curr node
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
print(solution(head))
print(solution(head2))
print(solution(head3))
