
class Vehicle:
    def __init__(self, brand, model, mileage, daily_rate):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.daily_rate = daily_rate
        self.is_rented = False
       

    def __str__(self):
        return f" {self.brand} {self.model}"

    def rent(self):
        if self.is_rented==False:
            self.is_rented = True
            return True
        else:
            return False

    def return_vehicle(self):
        self.is_rented = False

    def calculate_rental_cost(self, rental_duration):
        return self.daily_rate * rental_duration


class Car(Vehicle):
    def __init__(self, brand, model, mileage, daily_rate, doors):
        super().__init__(brand, model, mileage, daily_rate)
        self.doors=doors

class Truck(Vehicle):
    def __init__(self, brand, model, mileage, daily_rate):
        super().__init__(brand, model, mileage, daily_rate)
        self.__engine = 2000
        
    def print_engine(self):
        return self.__engine


class RentalAgency:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def check_availability(self):
        available_vehicles = []
        for vehicle in self.vehicles:
            if vehicle.is_rented ==False:
                available_vehicles.append(vehicle)
        return available_vehicles


    def rent_vehicle(self, vehicle, rental_duration):
        if vehicle.rent()==True:
            return vehicle.calculate_rental_cost(rental_duration)
        else:
            return "Vehicle is already rented."

    def return_vehicle(self, vehicle):
        vehicle.return_vehicle()


if __name__ == "__main__":
    agency = RentalAgency()

    car1 = Car("Toyota", "Car123", 30000, 30,4)
    car2 = Car("Honda", "Car234", 25000, 35,4)
    truck1 = Truck("Truck", "123", 40000, 50)

    agency.add_vehicle(car1)
    agency.add_vehicle(car2)
    agency.add_vehicle(truck1)

    print("Available vehicles:")
    for vehicle in agency.check_availability():
        print(vehicle)

    rental_duration = 5
    selected_car = car1
    rental_cost = agency.rent_vehicle(selected_car, rental_duration)
    print(f"Rented {selected_car} for {rental_duration} days. Total cost: ${rental_cost}")

    print("Available cars after renting:")
    for car in agency.check_availability():
        print(car)

    agency.return_vehicle(selected_car)

    print("Available cars after returning:")
    for car in agency.check_availability():
        print(car)

    rental_duration = 10
    selected_car2 = truck1
    print(selected_car2.print_engine())
    rental_cost = agency.rent_vehicle(selected_car2, rental_duration)
    print(f"Rented {selected_car2} for {rental_duration} days. Total cost: ${rental_cost}")

    print("Available cars after renting:")
    for car in agency.check_availability():
        print(car)

# class MenuItem:
    
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class Menu:
#     def __init__(self):
#         self.items=[]

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         self.items.remove(item)

#     def display_menu(self):
#         print("Menu:")
#         for item in self.items:
#             print(item)


# class Order:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         self.items.remove(item)

#     def calculate_total(self, *args):
#         total = 0
#         for item in args:
#             total += item
#         return total


# class Restaurant:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
   
# if __name__ == "__main__":
#     restaurant = Restaurant("Udupi Restaurant")
#     print(f"Menu for {restaurant.name}: ")
#     food_menu = Menu()
#     food_menu.add_item("Burger")
#     food_menu.add_item("Pasta")
#     food_menu.add_item("Sandwich")
#     food_menu.display_menu()

#     food_order = Order()
#     food_order.add_item("Burger")
#     food_order.add_item("Pasta")
#     bill = food_order.calculate_total(10,20)
#     print(bill)

    

