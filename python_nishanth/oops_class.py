# # class person:
# #     def print_name(self,name):
# #         print("my name is "+name)
# #     def add(self,a,b):
# #          return a+b
# #     def sub(self,a,b):
# #         return a-b
# # person= person()
# # person.print_name("shiva")
# # sum= person.add(3,4)
# # print(sum)
# # sum2= person.sub(3,4)
# # print(sum2)

# class city:
#     def addCityDetails(self,name,country):
#         self.name = name
#         self.country = country 
#     def printCityDetails (self):
#         print("city name is "+self.name)
#         print("country name is "+ self.country)
# print("___________________________________________________________")
# delhi = city()
# delhi.addCityDetails("delhi","india")
# delhi.printCityDetails()
# print("------------------------------------------------")
# mumbai=city()
# mumbai.addCityDetails("mumbai","india")
# mumbai.printCityDetails()
# print("___________________________________________________________")
# banglore =city()
# banglore.addCityDetails("banglore","india")
# banglore.printCityDetails()
# print("___________________________________________________________")


class person():
    cityname = "mumbai"
    def printname(self,name):
        print(name)
class ashok(person):
    def printdetails(self):
        print("hello my nigga")
obj = ashok()
obj.cityname = "shengai"
obj.printname("mr.asok")
obj.printname("mr.asok")

