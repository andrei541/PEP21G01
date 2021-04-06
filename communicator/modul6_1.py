# # #classes
# #
# # class Object:
# #     variable="this is my text"
# #     def print_var(self):
# #         print(self.variable)
# #     def change_var(self):
# #         self.variable="this is another text"
# #
# # Object1=Object()
# # Object1.print_var()
# # Object1.change_var()
# # print("class variable:",Object.variable)
# # print("instance variable:",Object1.variable)
# # import random
# # class Object2:
# #     variable=[1,2,3]
# #     def change_var(self):
# #         self.variable.append(random.randint(1,100))
# #
# # Object2=Object2()
# # print("class variable:",Object2.variable)
# # print("instance variable:",Object2.variable)
# # Object2.change_var()
# # print("-----------------")
# # print("class variable:",Object2.variable)
# # print("instance variable:",Object2.variable)
# # Object3=Object2
# # print(Object3.variable)
#
# # class Cars:
# #     counter=[0]
# #     def __init__(self):
# #         self.counter.insert(0,self.counter.pop(0)+1)
# #
# # car1=Cars()
# # car2=Cars()
# # car3=Cars()
# # car4=Cars()
# # print(car1.counter)
# #host si port
#
# class Conector:
#     def __init__(self,host,port):
#         self.port=port
#         self.host=host
#
# class Client(Conector):
#     pass
#
#
#
# class Server(Conector):
#     pass
#
#
# conector_obj=Conector("localhost",8080)