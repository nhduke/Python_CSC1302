class Day:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt
    
    def traverse(self, k):
        if k > 1:
            return self.nxt.traverse(k - 1)
        print('arrive at node', self.data)
            

    def printLinkedList(self):  # start from first real node if head is dummy
        print(self.data)
        if self.nxt:
            return self.nxt.printLinkedList()
            
    def deleteNote(self, k):
        if k > 2:
            return self.nxt.deleteNote(k - 1)
        self.nxt = self.nxt.nxt
    
    def insertNote(self, data, k):
        if k > 1:
            return self.nxt.insertNote(data, k - 1)
        dummy = Day(data, self.nxt)
        self.nxt = dummy
        
        
        
day7 = Day("Saturday", None)  
day6 = Day("Friday", day7)        
day5 = Day("Thursday", day6)
day4 = Day("Wednesday", day5)
day3 = Day("Tuesday", day4)  
day2 = Day("Monday", day3)
day1 = Day("Sunday", day2)


day1.printLinkedList()

# day1.deleteNote(5)
# print('______')
# day1.printLinkedList()
day1.traverse(5)

day1.insertNote('thu5', 5)
print('______')
day1.printLinkedList()



