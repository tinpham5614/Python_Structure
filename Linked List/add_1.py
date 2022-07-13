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
def addOne(head:ListNode):
  addWithCarry(head)
  return head
  
def addWithCarry(head: ListNode):
  if (head == None):
    return 1
    
  carry = addWithCarry(head.next)
  sum = head.val + carry
  
  head.val = (sum) % 10
  return (sum) // 10
  #still bugged
#test case
#list 1
head = ListNode(9)
temp = head
for value in [9]:
  temp.next = ListNode(value)
  temp = temp.next

#list 2
head2 = ListNode(5)
temp = head2
for value in [6,4,1,1,2]:
  temp.next = ListNode(value)
  temp = temp.next
print(addOne(head))
