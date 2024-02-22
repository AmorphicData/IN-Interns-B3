# Develop a system to manage rental vehicles. Create classes for Vehicle, Car, Truck, and RentalAgency. 
# Implement methods for renting vehicles, checking availability, and calculating rental charges based on vehicle type and rental duration.

from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, make, model, rental_rate):
        self.make = make
        self.model = model
        self.__rental_rate = rental_rate        #Private attribute
        self.available = True

    def calculate_rental_charge(self, days):                #Get overwritten by inherited class specific functionality
        raise NotImplementedError("Subclasses must implement calculate_rental_charge method.")

    def rent(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_vehicle(self):
        self.available = True

    def get_rental_rate(self):          #Getter function to access the private attribute rental rate
        return self.__rental_rate 

class Car(Vehicle):             #Class Vehicle inheritted by Class Car
    def __init__(self, make, model,custom_rent= None):
        if custom_rent is not None:
            super().__init__(make, model, rental_rate=custom_rent)
        else:
            super().__init__(make, model, rental_rate=50)

    def calculate_rental_charge(self, days):
        return self.get_rental_rate() * days    # Accessing private attribute of base class

class Truck(Vehicle):           #Class Vehicle inheritted by Class Truck; Thus a heirarchial inheritance
    def __init__(self, make, model, cargo_capacity):
        super().__init__(make, model, rental_rate=50)
        self.__cargo_capacity = cargo_capacity  # Private attribute for class Truck

    def calculate_rental_charge(self, days):
        return self.get_rental_rate() * days + self.__cargo_capacity * 0.1          # 0.1 given as a charge for cargo carried

class RentalAgency:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def check_availability(self, vehicle_type):
        for vehicle in self.vehicles:
            if isinstance(vehicle, vehicle_type) and vehicle.available: #If vehicle is an object of car/truck and available as well
                return True
        return False

    def rent_vehicle(self, vehicle_type, rental_duration):
        if self.check_availability(vehicle_type):
            for vehicle in self.vehicles:
                vehicle.available = False
                return vehicle, rental_duration
        else:
            print("Vehicle not available for rent.")
            return None, 0

    def return_vehicle(self, vehicle):
        vehicle.available= True
        vehicle.return_vehicle()

car1 = Car("Hyundai", "i20",80)
# car2 = Car("Mustang", "GT",100)
# car3 = Car("Maruti", "Swift")
# truck1 = Truck("Ford", "F150", cargo_capacity=1000)
# truck2 = Truck("Leyland", "Ashok", cargo_capacity=5000)

agency = RentalAgency()
agency.add_vehicle(car1)
# agency.add_vehicle(car2)
# agency.add_vehicle(car3)
# agency.add_vehicle(truck1)
# agency.add_vehicle(truck2)

vehicle_type = Car  #Change here for car/truck
ti = 5

if agency.check_availability(vehicle_type):
    rented_vehicle, duration = agency.rent_vehicle(vehicle_type, ti)
    if rented_vehicle:
        total_charge = rented_vehicle.calculate_rental_charge(duration)
        print("Vehicle rented successfully.")
        print("Total rental charge: ${}".format(total_charge))
        # agency.return_vehicle(rented_vehicle)                                 #Returns the vehicle back
else:
    print("No {} available for rent.".format(vehicle_type.__name__))

new_vehicle, dur = agency.rent_vehicle(vehicle_type, ti)                           #Recheck for same vehicle is renting

print("==============================================================================")

# Create classes for Restaurant, Menu, MenuItem, and Order. Implement methods for managing menus, 
# adding items to orders, and calculating bills for customers.

class MenuItem:                             #Put items into the list using this class
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu():                               #The menu list is here
    def __init__(self):
        self.items = []

    def add_item(self, dish):
        self.items.append(dish)

    def display(self):
        print("Menu:")
        for dish in self.items:
            print(f"{dish.name}: ${dish.price:.2f}")

class Order:                                    #Customer order using this class
    def __init__(self):
        self.eats = []
    def add(self, food):
        self.eats.append(food)

    def calculate_total(self):
        return sum(it.price for it in self.eats)

class Restaurant:
    def __init__(self):
        self.menus = {}
        self.orders = []

    def add_menu(self, menu_name, menu):
        self.menus[menu_name] = menu

    def display_menus(self):
        print("Available Menus:-----------")
        for menu_name, menu in self.menus.items():
            print(f"{menu_name} Menu:")
            print('-----------')
            menu.display()

    def create_order(self):
        order = Order()
        self.orders.append(order)
        return order

    def add_item(self, order, item):
        order.add(item)

    def calculate_bill(self, order):
        total = order.calculate_total()
        print(f">>>Total bill: ${total:.2f}")
        return total
    
    def show(self):
        print("Your Order:")
        for ord in self.orders:
            print("Order:")
            for dish in ord.eats:
                print(f"{dish.name}: ${dish.price:.2f}")
            self.calculate_bill(ord)

# Adding dishes to the menu by creating dishes object first 
pizza = MenuItem("Pizza", 12.99)
burger = MenuItem("Burger", 8.49)
salad = MenuItem("Salad", 5.99)
coffee = MenuItem("Coffee", 2.99)
tea = MenuItem("Tea", 1.99)

menu_dinner = Menu()        #One menu for dinner
menu_dinner.add_item(pizza)
menu_dinner.add_item(burger)
menu_dinner.add_item(salad)

menu_beverages = Menu()     #Second menu for beverages
menu_beverages.add_item(coffee)
menu_beverages.add_item(tea)

restaurant = Restaurant()
restaurant.add_menu("Dinner", menu_dinner)
restaurant.add_menu("Beverages", menu_beverages)
order1 = restaurant.create_order()
order2 = restaurant.create_order()

restaurant.display_menus()
print("-----------BILLS-------------")

restaurant.add_item_to_order(order1, pizza)
restaurant.add_item_to_order(order1, salad)
restaurant.add_item_to_order(order1, coffee)

restaurant.add_item_to_order(order2, burger)
restaurant.add_item_to_order(order2, tea)

restaurant.show()
