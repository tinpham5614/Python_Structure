def getNode(head, positionFromTail):
    # Write your code here
    curr = head 
    counter = 0
    while head.next: 
        head = head.next
        counter += 1
        
    for i in range(counter - positionFromTail):
        curr = curr.next
    return curr.data
