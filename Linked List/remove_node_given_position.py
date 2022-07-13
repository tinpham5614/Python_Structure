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
  if head is None: #if empty list, do nothing
    return None
  counter = 0 #create counter
  #create 2 pointers
  prev = head 
  curr = head
  while curr: #while loop
    curr = curr.next #move to next node if curr != null
    counter +=1 #counter increase by 1
    if (counter == position): #if counter is the same with position
        prev.next = curr.next #skip a node, point the pointer to the node after
    else:
        prev = curr # otherwise, prev remain as the same curr
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

