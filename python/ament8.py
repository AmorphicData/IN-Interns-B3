# class vehicle():
#         company=""
#         name=""
#         start_status=0
#         def __init__(self):
#                 print("Vehicle created")
#         def ignition(self,val):
#                 if(val==1):
#                         self.start_status=1
#                         print("Vehicle is started")
#                 else:
#                         raise ValueError
#         def checkstatus(self):
#                 if(self.start_status==1):
#                         print("Vehicle is Active")
#                 else:
#                         print("Inactive")
# class car(vehicle):
#         def __init__(self,name,company):
#                 print("Car created")
#                 self.name=name
#                 self.company=company
#         def ignition(self, val):
#                 if(val==2):
#                         self.start_status=2
#                         print(f"Your {self.name} has started")
#                 else:
#                         raise ValueError
#         def checkstatus(self):
#                 if(self.start_status==2):
#                         print("Car is Active")
#                 else:
#                         print("Inactive")
# class truck(vehicle):
#         def __init__(self,name,company):
#                 print("Truck created")
#                 self.name=name
#                 self.company=company
#         def ignition(self, val):
#                 if(val==3):
#                         self.start_status=3
#                         print(f"Your {self.name} has started")
#                 else:
#                         raise ValueError
#         def checkstatus(self):
#                 if(self.start_status==3):
#                         print("Truck is Active")
#                 else:
#                         print("Inactive")
# class RentalA():
#         __di={}
#         __di2={}
#         __di3={}
#         def __init__(self):
#                 print("Agency obj created")
#         def assigningvalues(self,vehicle,val):
#                 self.__di2[vehicle.name]=val
#         def up(self,name,rentch,rentdu):
#                 self.__di[name]=[(rentch/rentdu),rentdu]
#                 print(self.__di[name][0])
#         def checkrent(self,vehicle,week):
#                 name=vehicle.name
#                 if(self.__di2[name]==0):
#                         return "Data not available"
#                 return f"Charges for {name} are {self.__di[name][0]*week} for {week} weeks"
#         def rent(self,vehicle,name):
                
#                 if(self.__di2[vehicle.name]==0):
#                         return "Data not available"
#                 else:
#                    self.__di3[vehicle.name]=name
#                    self.__di2[vehicle.name]-=1
#         def servicecompleted(self,vehicle):
#                 self.__di2[vehicle.name]+=1
#                 self.__di3[vehicle.name]=""
                
#         # def checkstatus(self,vehicle):

# a=car("Fortuner","Toyota")
# b=truck("A1","Tata")

# ro=RentalA()
# ro.up("Fortuner",1200,1)
# ro.assigningvalues(a,1)
# print(ro.checkrent(a,2))









# class Restaurent():
#     name=""
#     address=""
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
# class menu(Restaurent):
#     menu_no=-1
#     di={}
#     def __init__(self,menu_no):
#         self.menu_no=menu_no
#     def insert(self,menuitem,price):
#         self.di[menuitem]=price
# a=Restaurent("Dhaba","Delhi")
# me=menu(1)
# me.insert("Alloo Paratha",50)
# me.insert("Chicken tikka",120)
# class order(Restaurent):
#     order_no=0
#     def __init__(self):
#         self.order_no=1
#     def create(self,o,tdi,name):
#         di={}
#         di[name]={'Order-No':o.order_no}
#         g_t=0
        
#         for key,value in tdi.items():
#             g_t+=value
#         di['Orders_details']=tdi
#         di['TOTAL']=g_t
#         di['Order Object']=o
#         return di



# class customer():
#     name=""
#     def __init__(self,name):
#         self.name=name
#     def createorder(self,menu):
#         tdi={}
#         while(True):
#             order_item=input()
#             if(order_item=="none"):
#                 break
#             qu=int(input())
#             if(menu.di.get(order_item,0)==0):
#                 print("Item Not Available")
#                 continue
#             price=menu.di[order_item]
#             tdi[order_item]=(price*qu)
#         o=order()
#         D=o.create(o,tdi,self.name)
#         return D
# c=customer("Saksham")
# print(c.createorder(me))



    


                