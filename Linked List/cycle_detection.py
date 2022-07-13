def has_cycle(head):
    if head and head.next is None:
        return False
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
        if fast == slow:
            return True
    return False
