#Q1
from abc import ABC,abstractmethod
class vehicle:
    def __init__(self,make,model,year):
        #this is a my constructor
        #aese karke mene un sab ko proctacted bana diya hai
        self.__make=make
        self.__model=model
        self.__year=year #all these attribute now become protected one
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    #These all are getter and setter function
    #jo mujhe proctacted value laake denge

    # An abstract method is a method declared within a class, but it does not contain any implementation. Instead, its implementation is expected to be provided by its subclasses. 
    @abstractmethod
    def calculate_rent(self,days):
        pass
class car(vehicle):
    def __init__(self, make, model, year,daily_rate):
        super().__init__(make, model, year)
        self.__daily_rate=daily_rate
    def calculate_rent(self, days):
        return self.__daily_rate*days
    
class Truck(vehicle):
    def __init__(self, make, model, year,daily_rate,weight_cap):
        super().__init__(make, model, year)
        self.__daily_rate=daily_rate
        self.__weight_cap=weight_cap
    def calculate_rent(self, days):
        return self.__daily_rate*days

class RentalAgency:
    def __init__(self):
        self.__vehicles=[]
    def add_vehicle(self,vehicle):
        return self.__vehicles.append(vehicle)
    def rent_vehicle(self,make,model,days):
        for vehicle in self.__vehicles:
            if isinstance(vehicle,car) or isinstance(vehicle,Truck):
                if vehicle.get_make()==make and vehicle.get_model()==model:
                    return vehicle.calculate_rent(days)
        return None

    
rental_agency=RentalAgency()
car1=car("Mahindra","XUV",2020,50)
car2=car("Ford","Endevor",2021,100)
truck1 = Truck("Ford", "F-150", 2018, 80, 2000)
truck2 = Truck("Chevrolet", "Silverado", 2017, 90, 2500)

rental_agency.add_vehicle(car1)
rental_agency.add_vehicle(car2)
rental_agency.add_vehicle(truck1)
rental_agency.add_vehicle(truck2)


print("Rent for Mahindra XUV:",rental_agency.rent_vehicle("Mahindra","XUV",7))
print("Rent for Ford Endevor:",rental_agency.rent_vehicle("Ford","Endevor",4))

print("Rent for Ford Truck:",rental_agency.rent_vehicle("Ford","F-150",3))
print("Rent for Chevrolet Truck:",rental_agency.rent_vehicle("Chevrolet","Silverado",5))

#Q2
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
            print(f"{item.get_name()} - ${item.get_price()}")
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
    item1=Menuitem("Burger",200)
    item2=Menuitem("Chole Buthere",160)
    item3=Menuitem("Pizza",400)
    
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