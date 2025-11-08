class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode):
    dummy = ListNode(0)
    head = ListNode(0,dummy)
    remainder = 0
    
    while l1.next or l2.next:
        dummy.val = l1.val + l2.val + remainder
        remainder = dummy.val // 10
        dummy.val = dummy.val % 10
        
        l1 = l1.next 
        l2 = l2.next
        dummy.next = ListNode()
        dummy = dummy.next
        
    dummy.val = l1.val + l2.val + remainder
    if dummy.val >= 10:
        dummy.val = dummy.val % 10
        dummy.next = ListNode(dummy.val // 10, None)
    
    return head.next
        


l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
print(l1)
print(l2)
result = addTwoNumbers(l1,l2)

while result.next:
    print(result.val)
    result = result.next
print(result.val)


        