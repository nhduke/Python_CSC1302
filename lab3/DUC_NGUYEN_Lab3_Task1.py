class Location:
    def __init__(self, x:float, y:float)-> None:
        self.x = x
        self.y = y
        #TODO: Define the constructor to initialize x and y coordinates

    def __le__(self, other: "Location") -> bool:
        compareX = self.x <= other.x
        compareY = self.y <= other.y
        if compareX and compareY:
            return True
        else:
            return False
        # TODO_1: Implement this method to compare two Location objects based on their distance from the origin (0,0)

    def __eq__(self, other: "Location") -> bool:
        compareX = self.x == other.x
        compareY = self.y == other.y
        if compareX and compareY:
            return True
        else:
            return False
        # TODO_2: Implement this method to check if two Location objects are at the same coordinates
    
if __name__ == "__main__":
    loc1 = Location(3, 4)
    loc2 = Location(5, 8)

    print(loc1 == loc2)  # False
    print(loc1 <= loc2)  # True

