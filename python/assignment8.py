#Class and objects

#Develop a system to manage rental vehicles. Create classes for Vehicle, Car, Truck, and RentalAgency. Implement methods for renting vehicles, checking availability, and calculating rental charges based on vehicle type and rental duration.

class Vehicle:
    def __init__(self,manufac,model,year):
        self.manufac=manufac
        self.model=model
        self.year=year
        self.is_rented=False

    def description(self):
        return f"{self.year} {self.manufac} {self.model}"
    def available(self):
        return not self.is_rented
    def rent(self):
        if self.available():
            self.is_rented=True
            return f"{self.description()} has been rented"
        else:
            return f"{self.description()} is currently not available for rent"
    def return_vehicle(self):
        self.is_rented=False
        return f"{self.description()} has been returned"
    
    
class Car(Vehicle):
    def __init__(self,manufac,model,year,person_capacity):
        super().__init__(manufac,model,year)
        self.person_capacity=person_capacity
    def rental_charge(self,days):
        return 2500*days

class Truck(Vehicle):
    def __init__(self,manufac,model,year,payload_capacity):
        super().__init__(manufac,model,year)
        self.payload_capacity=payload_capacity
    def rental_charge(self,days):
        return 3500*days

class Rental:
    def __init__(self,vehicles):
        self.vehicles=vehicles
    def available(self):
        available_vehicles=[vehicle.description() for vehicle in self.vehicles if vehicle.available() ]
        return available_vehicles
    def rent_vehicle(self,vehicle_index,rental_days):
        if 0<= vehicle_index<len(self.vehicles):
            vehicle=self.vehicles[vehicle_index]
            if vehicle.available():
                vehicle.rent()
                r_c=vehicle.rental_charge(rental_days)
                return f"{vehicle.description()} has been rented and Rental charges: {r_c}"
            else:
                return f"{vehicle.description()} is not valid for rent"
        else:
            return "Invalid vehicle index"
                                          
    def return_vehicle(self, vehicle_index):
        if 0 <= vehicle_index < len(self.vehicles):
            return self.vehicles[vehicle_index].return_vehicle()
        else:
            return "Invalid vehicle index."
    
   
    
car1 = Car("Toyota", "Camry", 2022, 4)
car2 = Car("Honda", "Accord", 2021, 4)
car3 = Car("Chevrolet", "Malibu", 2022, 4)

truck1 = Truck("Ford", "F-150", 2022, 2000)
truck2 = Truck("Chevrolet", "Silverado", 2021, 2500)
truck3 = Truck("Random", "H-350", 2022, 1800)
        

agency = Rental([car1, car2, car3, truck1, truck2, truck3])
print("Available vehicles:", agency.available())


print(agency.rent_vehicle(0,5))  
print(agency.rent_vehicle(3,9)) 

print("Available vehicles:", agency.available())


print(agency.return_vehicle(3))  

print("Available vehicles:", agency.available())


# #Create classes for Restaurant, Menu, MenuItem, and Order. Implement methods for managing menus, adding items to orders, and calculating bills for customers.


class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
class Menu:
    def __init__(self):
        self.menu_items=[]
    
    def add_item(self,menu_item):
        self.menu_items.append(menu_item)

    def display_menu(self):
        print("Menu:")
        for item in self.menu_items:
            print(f"{item.get_name()} - {item.get_price()}")
class Order:
    def __init__(self):
        self.order_items=[]
    def order_item(self,menu_item):
        self.order_items.append(menu_item)

    def cal_bill(self):
        bill=0
        for item in self.order_items:
            bill+=item.get_price()
        return bill
class Restaurant:
    def __init__(self):
        self.menu=Menu()
        self.order=Order()

    def add_item(self,menu_item):
        self.menu.add_item(menu_item)
    
    def display_menu(self):
        self.menu.display_menu()
    
    def place_order(self,menu_item):
        self.order.order_item(menu_item)

    def generate_bill(self):
        bill_amount=self.order.cal_bill()
        print(f"Total bill: {bill_amount}")

if __name__ == "__main__":
  
    item1 = MenuItem("Burger", 110)
    item2 = MenuItem("Pizza", 155)
    item3 = MenuItem("Salad", 75)
    item4 = MenuItem("Pasta", 220)
    item5 = MenuItem("Biryani",350)
    item6 = MenuItem("Coffee",45)

    restaurant = Restaurant()

    
    restaurant.add_item(item1)
    restaurant.add_item(item2)
    restaurant.add_item(item3)
    restaurant.add_item(item4)
    restaurant.add_item(item5)
    restaurant.add_item(item6)


    restaurant.display_menu()


    restaurant.place_order(item1)
    restaurant.place_order(item3)
    restaurant.place_order(item4)
    restaurant.place_order(item6)


    restaurant.generate_bill() 
    


