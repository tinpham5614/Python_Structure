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
def solution(head1, head2: ListNode):

  while head1 is not None and head2 is not None:
      if head1.val != head2.val:
          return False
      head1 = head1.next
      head2 = head2.next
      
  if head1 is not None or head2 is not None:
      return False
  return True
#test case
#list 1
head1 = ListNode(1)
temp = head1
for value in [2,3,7]:
  temp.next = ListNode(value)
  temp = temp.next
  

#list 2
head2 = ListNode(1)
temp = head2
for value in [2,3,3,1,6]:
  temp.next = ListNode(value)
  temp = temp.next

print(solution(head1, head2))

# return: False
