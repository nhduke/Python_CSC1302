class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
        
class Vegetable():
    def __init__(self,name, location):
        self.name = name
        self.location = location

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
        
class Vegetable(Location):
    def __init__(self,name, x, y):
        self.name = name
        Location.__init__(self, x, y)

        
def main():
    
    locat1 = Location(1, 2)
    vege1 = Vegetable("Rau cu qua", 1,2)
    print(locat1)
    print(vege1.name, vege1.x, vege1.y)
    
main()