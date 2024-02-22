#Develop a system to manage rental vehicles. 

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.available = True

    @abstractmethod
    def calculate_rental(self, days):
        pass

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - Available: {self.available}"

class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_doors, fuel_type):
        super().__init__(make, model, year, daily_rate)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def calculate_rental(self, days):
        return self.daily_rate * days * (1.1 if self.fuel_type == "Hybrid" else 1)

    def __str__(self):
        return super().__str__() + f", Doors: {self.num_doors}, Fuel: {self.fuel_type}"

class Truck(Vehicle):
    def __init__(self, make, model, year, daily_rate, payload_capacity):
        super().__init__(make, model, year, daily_rate)
        self.payload_capacity = payload_capacity

    def calculate_rental(self, days):
        return self.daily_rate * days * (1.2 if self.payload_capacity >= 1000 else 1)

    def __str__(self):
        return super().__str__() + f", Payload Capacity: {self.payload_capacity} lbs"

class RentalAgency:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
        else:
            print("Invalid vehicle type. Only Car and Truck objects allowed.")

    def rent_vehicle(self, vehicle_type, days):
        available_vehicles = [v for v in self.vehicles if v.available and isinstance(v, vehicle_type)]
        if available_vehicles:
            rented_vehicle = available_vehicles[0]
            rented_vehicle.available = False
            return rented_vehicle, rented_vehicle.calculate_rental(days)
        else:
            return None, 0

    def list_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.vehicles:
            if vehicle.available:
                print(vehicle)

def rent_print(agency, vehicle_type, days):
    rented_vehicle, rental_cost = agency.rent_vehicle(vehicle_type, days)
    if rented_vehicle:
        print(f"Rented {rented_vehicle}: ${rental_cost}")
    else:
        print(f"No {vehicle_type.__name__} available for rent.")

agency = RentalAgency("My Car Rentals")

agency.add_vehicle(Car("Toyota", "Camry", 2022, 50, 4, "Hybrid"))
agency.add_vehicle(Truck("Ford", "F-150", 2021, 80, 1500))
agency.add_vehicle(Car("Kia", "Seltos", 2021, 50, 4, "Hybrid"))
agency.add_vehicle(Truck("ABC", "XYZ", 2021, 80, 1500))

rent_print(agency, Car, 3)
rent_print(agency, Truck, 3)
rent_print(agency, Truck, 3)
rent_print(agency, Truck, 3)

agency.list_vehicles()




#Create classes for Restaurant, Menu, MenuItem, and Order. 

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menus = []  

    def add_menu(self, menu):
        self.menus.append(menu)

    def get_menu_by_name(self, name):
        for menu in self.menus:
            if menu.name == name:
                return menu
        return None

    def create_order(self, customer_name, menu_name):
        menu = self.get_menu_by_name(menu_name)
        if menu:
            return Order(customer_name, menu)
        else:
            print(f"Menu '{menu_name}' not found.")
            return None

class Menu:
    def __init__(self, name):
        self.name = name
        self.items = [] 

    def add_item(self, item):
        self.items.append(item)

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Order:
    def __init__(self, customer_name, menu):
        self.customer_name = customer_name
        self.menu = menu
        self.items = []  

    def add_item(self, item_name, quantity):
        item = self.menu.get_item_by_name(item_name)
        if item:
            self.items.append((item, quantity))
        else:
            print(f"Item '{item_name}' not found in menu '{self.menu.name}'.")

    def bill(self):
        total_price = 0
        for item, quantity in self.items:
            total_price += item.price * quantity
        return total_price
    
def print_order(order):
    print(f"Customer: {order.customer_name}")
    print(f"Menu: {order.menu.name}")
    for item, quantity in order.items:
        print(f"{item.name}({quantity}) - Rs {item.price * quantity:}")
    print(f"Total: Rs {order.bill():}\n")

restaurant = Restaurant("My Restaurant")

breakfast_menu = Menu("Breakfast")
breakfast_menu.add_item(MenuItem("Pancakes", "Fluffy pancakes with butter and syrup", 70))
breakfast_menu.add_item(MenuItem("Omelette", "Made-to-order omelette with your choice of fillings", 60))

lunch_menu = Menu("Lunch")
lunch_menu.add_item(MenuItem("Burger", "Juicy burger with fries",90))
lunch_menu.add_item(MenuItem("Salad", "Fresh salad with your choice of toppings", 50))

restaurant.add_menu(breakfast_menu)
restaurant.add_menu(lunch_menu)

order1 = Order("Alice", lunch_menu)
order1.add_item("Burger", 1)
order1.add_item("Salad", 2)

order2 = Order("Bob", breakfast_menu)
order2.add_item("Pancakes", 1)

print_order(order1)
print_order(order2)
