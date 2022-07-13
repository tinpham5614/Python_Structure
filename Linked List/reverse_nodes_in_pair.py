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
  #create dummy node:
  dummy = ListNode(0)
  #pointing to head
  dummy.next = head
  #assign dummy as a curr
  curr = dummy

  #traversal
  while curr.next and curr.next.next: # next node and next 2 node is not None
    
    first = curr.next
    second = curr.next.next

    first.next = second.next
    
    curr.next = second
    curr.next.next = first

    curr = curr.next.next
  return dummy.next
    

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

