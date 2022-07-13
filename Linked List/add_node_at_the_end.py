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
def solution(head: ListNode):
  new_node = ListNode(5)
  if head is None: # if empty list, new node is head
    head = new_node
    return head
  #otherwise, find the last node and add the new node
    #traversal through the list
  curr = head #assign curr node is head
  while curr.next: # if the next node is not null, continue traversing
    curr = curr.next # travesal
  curr.next = new_node #the last node before null is new node
  return head
  
#test case
#list 1
head = ListNode(1)
temp = head
for value in [2,3,7]:
  temp.next = ListNode(value)
  temp = temp.next
  

#list 2
head2 = ListNode(1)
temp = head2
for value in [2,4,3,1,6]:
  temp.next = ListNode(value)
  temp = temp.next

print(solution(head))
print(solution(head2))
