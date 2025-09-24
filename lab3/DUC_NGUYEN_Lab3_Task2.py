class Computer:
    def __init__(self,manufacturer,model,processor,ram,display_size):
        #TODO_1: Define the constructor of the Base class 'Computer'
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.display_size = display_size

    def print_info(self):
        #TODO_2: Define this method. It should print all the data attributes of a given 'Computer' object
        print("Computer Information:")
        print("Manufacturer     : ", self.manufacturer)
        print("Model            : ", self.model)
        print("Processor        : ", self.processor)
        print("Ram              : ", self.ram)
        print("Display size     : ", self.display_size)


class Laptop(Computer):
    def __init__(self, m,md,p,r,s,w,it):
        #TODO_3: Define the constructor of the derived class 1 (Laptop)
        #Hint: You will need to call the constructor of the base class
        Computer.__init__(self,m,md,p,r,s)
        self.weight = w
        self.is_touch_screen = it

    def print_info(self):
        #TODO_4: this method should print all the data attributes of a 'Laptop' object
        Computer.print_info(self)
        print("Weight           : ", self.weight)
        print("Is Touch Screen  : ", self.is_touch_screen)


class Desktop(Computer):
    def __init__(self, m,md,p,r,s,type):
        # TODO_5: Define the constructor of the derived class 2 (Desktop)
        # Hint: Again, you will need to call the constructor of the base class
        Computer.__init__(self,m,md,p,r,s)
        self.type = type

    def print_info(self):
        #TODO_6: this method should print all the data attributes of the 'Desktop' object
        Computer.print_info(self)
        print("Type             : ", self.type)


# driver code. No modification is necessary after this line.
computer1 = Laptop('Apple', 'MacBook Air', 'Apple M1', '16GB', '13.3"', '2.7 lbs', False)
computer2 = Laptop('HP', 'Envy', 'core i5', '8GB', '15.6"', '4lbs', True)
computer3 = Desktop('Dell', 'Inspiron', 'core i7', '32GB', '27"', 'All-in-One')
computer1.print_info()
computer2.print_info()
computer3.print_info()
