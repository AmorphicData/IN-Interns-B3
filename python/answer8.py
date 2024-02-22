from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        

    def get_make(self):
        return self.make 
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year

    #def return_vehicle(self):
    #    self.is_available = True

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass


class Car(Vehicle):
    def __init__(self, make, model, year,rate):
        super().__init__(make, model, year)
        self.rate=rate
    def calculate_rental_cost(self, days):
        return self.rate*days  

class Truck(Vehicle):
    def __init__(self, make, model, year, daily_rate):
        super().__init__(make, model, year)
        self.daily_rate=daily_rate
    def calculate_rental_cost(self, days):
        return self.daily_rate*days

class RentalAgency:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def rent_vehicle(self, make, model, days):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car) or isinstance(vehicle, Truck):
                if vehicle.get_make() == make and vehicle.get_model() == model:
                    return vehicle.calculate_rental_cost(days)
        return None


# Example usage

agency = RentalAgency()


car1 = Car("Toyota", "Camry", 2020,10)
car2 = Car("Honda", "Accord", 2019, 5)
truck1 = Truck("Ford", "F-150", 2021, 80)
truck2 = Truck("Chevrolet", "Silverado", 2017, 90)
agency.add_vehicle(car1)
agency.add_vehicle(car2)
agency.add_vehicle(truck1)
agency.add_vehicle(truck2)

print("Rent for Toyota Camry:",agency.rent_vehicle("Toyota","Camry",10))
print("Rent for Honda Accord:",agency.rent_vehicle("Honda","Accord",10))
print("Rent for Ford Truck:",agency.rent_vehicle("Ford","F-150",10))
print("Rent for Chevrolet Truck:",agency.rent_vehicle("Chevrolet","Silverado",10))



 


class FoodItem:
    def __init__(self,name,price):
        self.__name=name
        self.__price=price
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
class Menuitem(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)
class Menu:
    def __init__(self):
        self.__items = []
    def add_item(self, item):
        self.__items.append(item)
    def display_menu(self):
        print("Menu:")
        for item in self.__items:
            print(f"{item.get_name()} - rupees {item.get_price()}")
class Order:
    def __init__(self):
        self.__items = []
    def add_item(self, item):
        self.__items.append(item)
    def calculate_total(self):
        total = 0
        for item in self.__items:
            total += item.get_price()
        return total
class Restraurent:
    def __init__(self):
        self.__menu=Menu()
    def add_menu_item(self,item):
        self.__menu.add_item(item)
    def display_menu(self):
        self.__menu.display_menu()
    def take_order(self, order):
        return order.calculate_total()
if __name__=="__main__":
    item1=Menuitem("momos",100)
    item2=Menuitem("burger",200)
    item3=Menuitem("icecream",300)
    #now i will make object of Restraurent
    restraurent=Restraurent()
    restraurent.add_menu_item(item1)
    restraurent.add_menu_item(item2)
    restraurent.add_menu_item(item3)
    restraurent.display_menu()
    #now i will take order
    order=Order()
    order.add_item(item1)
    order.add_item(item3)
    #now i will calculate total price of order
    bill=restraurent.take_order(order)
    print("Total Bill is:",bill)

