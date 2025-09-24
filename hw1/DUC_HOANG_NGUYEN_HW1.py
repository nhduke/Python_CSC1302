import math

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distance(self, other): #add distance method to calculate distance easier, and for possible future extensive use
        d = math.sqrt(pow((other.x - self.x), 2) + pow((other.y - self.y), 2))
        return d
    
class Car():
    def __init__(self, name, location, cost):
        self.car_name = name
        self.location = location #take location as an Location object, not inherit as a sub class
        self.cost_per_mile = cost
        
    def __str__(self):
        return f"Car: {self.car_name}, Location: {self.location}, Cost: {self.cost_per_mile}"
    
    def move_to(self, new_x, new_y):
        self.location.x = new_x
        self.location.y = new_y
    
    def __eq__(self, other): #add __eq__ overload operator to compare 2 cars, to help the RideSharingApp.remove_car works properly
        return self.car_name == other.car_name
        
class Passenger:
    def __init__(self, name, location):
        self.passenger_name = name
        self.location = location
    
    def __str__(self):
        return f"Passenger Name: {self.passenger_name}, Location: {self.location}"
    
    def move_to(self, new_x, new_y): 
        self.location.x = new_x #use self.location.x or location.y to access to Location class attribute
        self.location.y = new_y
    
    def __eq__(self, other):
        return self.passenger_name == other.passenger_name #add overload operator to help RideSharingApp.remove_passenger works properly
        
    
class RideSharingApp:
    def __init__(self): #initiate empty lists of cars and passengers, instances of cars and passengers will be added later by add_car and add_passenger method
        self.cars = []
        self.passengers = []
    
    def add_car(self, car): #add the new car as a latest member of cars[] list
        self.cars.append(car)
        
    def add_passenger(self, passenger):
        self.passengers.append(passenger) #add the new passenger as the lastest member of passenger[] list
    
    def remove_car(self, car):
        self.cars.remove(car) #remove car with the same car_name as the input object
    
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger) #remove passenger witht the same passenger_name as the input object
    
    def find_cheapest_car(self):
        cheapest_car_num = 0
        cheapest_cost = self.cars[0].cost_per_mile
        for i in range(0, len(self.cars)):#scan the whole cars[] list to find the cheapest cost one
            if self.cars[i].cost_per_mile < cheapest_cost:
                cheapest_car_num = i
                cheapest_cost = self.cars[i].cost_per_mile
        return print(f'The cheapest car is: {self.cars[cheapest_car_num]}')

    def find_nearest_car(self, passenger):
        nearest_car_num = 0
        nearest_distance = self.cars[0].location.distance(passenger.location)
        for i in range(0, len(self.cars)): #scan the whole cars[] list to find the shortest distance
            if self.cars[i].location.distance(passenger.location) < nearest_distance:
                nearest_car_num = i
                nearest_distance = self.cars[i].location.distance(passenger.location)
        return print(f'The nearest car is: {self.cars[nearest_car_num]}, distance: {nearest_distance:.2f}')

        
            
    

#For the remaining code (after this line), no modification is required
print('---------------------Object Creation------------------')
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 0.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)

location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)

mobileApp = RideSharingApp()
mobileApp.add_car(car1)
mobileApp.add_car(car2)
mobileApp.add_passenger(passenger1)
mobileApp.add_passenger(passenger2)

print('-----------------------Scenario 1---------------------')
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 2---------------------')
car1.move_to(0,-5)
passenger1.move_to(0,3)
print('car1\'s location has been updated:',car1)
print('passenger1\'s location has been updated:', passenger1)

mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 3---------------------')
car3= Car('car3', Location(0,2), 0.3)
mobileApp.add_car(car3)
print('New car added:',car3)

mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

