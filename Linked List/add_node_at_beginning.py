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
  # create a new node with val
  n = ListNode(5)
  # pointing to the head
  n.next = head
  # update the new node as head
  head = n
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
