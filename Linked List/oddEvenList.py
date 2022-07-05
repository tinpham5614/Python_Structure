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
def oddEvenList(head: ListNode):
  if(head != None):
    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
      odd.next = odd.next.next
      even.next = even.next.next
      odd = odd.next
      even = even.next

    odd.next = evenHead
    return head

#test case
#list 1
head = ListNode(1)
temp = head
for value in [2,3,4]:
  temp.next = ListNode(value)
  temp = temp.next

#list 2
head2 = ListNode(5)
temp = head2
for value in [6,4,1,1,2]:
  temp.next = ListNode(value)
  temp = temp.next
print(oddEvenList(head))
print(oddEvenList(head2))
