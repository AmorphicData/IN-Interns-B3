#Class and Objects

#Q1

class Vehicle:
    def __init__(self, company, mileage, daily_rate):
        self.company = company
        self.mileage = mileage
        self.daily_rate = daily_rate
        self.available = True

    def rent(self, duration):
        if self.available:
            self.available = False
            total_charge = self.daily_rate * duration
            print(f"{self.company} rented for {duration} days. Total rental charges: Rs {total_charge}")
        else:
            print(f"{self.company} is not available for rent.")

    def return_vehicle(self):
        if not self.available:
            self.available = True
            print(f"{self.company} returned successfully.")
        else:
            print(f"{self.company} was not rented.")


class Car(Vehicle):
    def __init__(self, company, mileage, daily_rate, num_seats):
        super().__init__(company, mileage, daily_rate)
        self.num_seats = num_seats


class Truck(Vehicle):
    def __init__(self, company, mileage, daily_rate, weight_capacity):
        super().__init__(company, mileage, daily_rate)
        self.weight_capacity = weight_capacity

class RoyalBrothers:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def check_availability(self):
        for vehicle in self.vehicles:
            print(f"{vehicle.company} is available." if vehicle.available else
                  f"{vehicle.company} is not available.")

    def rent_vehicle(self, company, duration):
        for vehicle in self.vehicles:
            if vehicle.company == company:
                if vehicle.available:
                    total_charge = vehicle.daily_rate * duration
                    vehicle.rent(duration)
                    print(f"Total rental charges: Rs {total_charge}")
                else:
                    print(f"{vehicle.company} is not available for rent.")
                return
        print("Vehicle not found.")

    def return_vehicle(self, company):
        for vehicle in self.vehicles:
            if vehicle.company == company:
                vehicle.return_vehicle()
                return
        print("Vehicle not found.")


c1 = Car("BMW", 7, 50000, 4)
c2 = Car("Buggati", 4, 100000, 2)
t1 = Truck("Mercedes", 12, 1500000, "1000 kg")

a = RoyalBrothers([c1, c2, t1]) #create an instance of the RoyalBrothers

a.check_availability()

a.rent_vehicle("BMW", 3)
a.rent_vehicle("BMW", 4)  
a.rent_vehicle("Buggati", 5)  

a.return_vehicle("Buggati")
a.return_vehicle("BMW")

#Q2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.items = []  

    def add_to_menu(self, item):
        self.items.append(item)

    def display_menu(self):
        print("Menu: ")
        for item in self.items:
            print(f"{item.name} - Rs {item.price}")


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def amount(self):
        total = 0
        for item in self.items:
            total += item.price
        return total



menu_item1 = MenuItem("Shake", 300)
menu_item2 = MenuItem("Thali", 400)
menu_item3 = MenuItem("Pasta", 250)

restaurant = Restaurant("Cafe Story")
restaurant.add_to_menu(menu_item1)
restaurant.add_to_menu(menu_item2)
restaurant.add_to_menu(menu_item3)

restaurant.display_menu()

order = Order()
order.add_item(menu_item1)
order.add_item(menu_item2)
order.add_item(menu_item3)

total_bill = order.amount()
print(f"Total Bill: Rs {total_bill}")


