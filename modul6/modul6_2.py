# # # #iterator
# # #
# # # class MyInt(int):
# # #     def __init__(self,number:int):
# # #         super(MyInt, self).__init__()
# # #         self.number=number
# # #     def __iter__(self):
# # #
# # #         number_list=[i for i in range(self.number+1)]
# # #         iter_something=Iter1(number_list)
# # #         return iter_something
# # #
# # #
# # # class Iter1():
# # #     def __init__(self,my_list:list):
# # #         self.my_list=my_list
# # #     def __iter__(self):
# # #         return self
# # #
# # #     def __next__(self):
# # #         if self.my_list:
# # #             return self.my_list.pop(0)
# # #         else:
# # #             raise StopIteration
# # #
# # # # my_iter=Iter1([1,2,3])
# # # # print(next(my_iter))
# # # # print(next(my_iter))
# # # # print(next(my_iter))
# # # # print(next(my_iter))
# # #
# # # class Obj1():
# # #     def __iter__(self):
# # #         return Iter1([1,2,3])
# # #
# # # obj1=Obj1()
# # # obj2=MyInt(5)
# # # print(5==obj2,"comparare")
# # # for i in obj2:
# # #     print(i)
# # #
# # # # for i in obj1:
# # # #     print(i,type(1))
# # #
# # #
# # # # class A():
# # # #     def __init__(self):
# # # #         print("in class A")
# # # #
# # # # class B(A):
# # # #     def __init__(self):
# # # #         super(B, self).__init__()
# # # #         print("in class B")
# # # #
# # # # class C(B):
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #
# # # #
# # # # c=C()
# #
# #
# # # with open('my_file','w') as file:
# # #     file.write('test1')
# # #     # raise AttributeError
# # #
# # # class MyFileOpen():
# # #     def __enter__(self):
# # #         print("in enter method")
# # #     def __exit__(self, exc_type, exc_val, exc_tb):
# # #         print("in exit method")
# # #
# # # with MyFileOpen() as my_file_open:
# # #     print('in context')
# #
# # class PythonCodeGet():
# #     def __enter__(self):
# #         f = open('my_file', 'w')
# #         self.f = f
# #         return self
# #
# #     def get_code(self):
# #         prompt = ">>>"
# #         indent = '    '
# #         counter = 0
# #         a = input(prompt + counter * indent)
# #         self.f.write(counter * indent + a + '\n')
# #         while a != '' or counter != 0:  # while a or counter
# #             if a.endswith(':'):
# #                 prompt = '... '
# #                 counter = counter + 1
# #             a = input(prompt + counter * indent)
# #             if not a:
# #                 counter = counter - 1
# #             self.f.write(counter * indent + a + "\n")
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         self.f.close()
# #
# #
# # with PythonCodeGet() as code_get:
# #     code_get.get_code()
