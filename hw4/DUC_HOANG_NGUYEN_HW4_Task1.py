class LinkedListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next
        
    def isOneElement(self): #constraint: each node/player must have a different value (identity)
        return self.next == self #check if the list looped to itself
 
    def createLoopedList(self, *inputs):
        #head/start of the looped
        self.val = inputs[0]
        current = self
        
        for num in inputs[1:]:
            current.next = LinkedListNode(num)
            current = current.next
        #connect back to the head    
        current.next = self
        return self
               
    def printLoopedList(self):
        print('----------------')
        valSet = set()
        current = self
        while current.val not in valSet:
            print(current.val)
            valSet.add(current.val)
            if current.next:
                current = current.next
        
    def potatoGame(self, steps):
        if steps < 1:
            raise ValueError("Steps must be >= 1")

        # Initialize previous node
        prev = self
        while prev.next != self:
            prev = prev.next
        current = self
        
        # Loop until only one node remains
        while not current.isOneElement():
            # Move (steps - 1) times; counting starts at current node
            for _ in range(steps - 1):
                prev = current
                current = current.next 
            
            # Now current is the node to delete
            deleteNode = current
            print(f"Delete player {deleteNode.val}")
            prev.next = deleteNode.next #skip/delete the middle (current node) -

            current = current.next #current point to the next node
            deleteNode.next = None #remove all link to/from the grabage node
        
        print(f"Potato game complete. The last player is: {current.val}")
        self.val, self.next = current.val, current.next
        return current.val
            

    
# head = LinkedListNode()

# head.createLoopedList(10,11,12,13,14,15,16,17,18)
# head.printLoopedList()

# head.potatoGame(2)
# head.printLoopedList()


