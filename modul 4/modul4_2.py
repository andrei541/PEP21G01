#set
# empty_set=set()
# set1={1,2,3}
# set2={2,3,4}
# intersect=set1 | set2
# print(intersect)
# intersect=set1.intersection(set2)
# print(intersect)
# union=set1.union(set2)
# print(union)
#pinball test


# test_data=[[1,2,3],[3,3,5],[8,9,4],[2,8,4]]
# iter_test_data=[]
#
# def pinball_test(data):
#
#     comparison_data=list(range(1,11))
#     print(comparison_data)
#     for test_data in comparison_data.copy():
#         for iner_list in data:
#
#             for elem in iner_list:
#                 if elem  in comparison_data:
#                     comparison_data.remove(elem)
#     return comparison_data
#
# resoult=pinball_test(test_data)
# print(resoult)
#
# test_data = [[1,2,3],[3,3,5],[8,9,4],[2,8,4]]
# def func(data_set):
#     full_data = set()
#     set_test_data = set()
#     miss_data = set()
#     for z in range(1,11):
#         full_data.add(z)
#     for x in data_set:
#         for y in x:
#             set_test_data.add(y)
#     miss_data = full_data.difference(set_test_data)
#     return list(miss_data)
#
# print(func(test_data))


# set1={0,1,2,3}
# set2={2,3,4,5}
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.symmetric_difference_update(set2))
# print(set2.symmetric_difference(set1))
# print("new update:",set1)

# def hello():
#     name=input("hello,what is your name:")
#     question(name)
#
# def question(name):
#     print(f"how is your day {name}?")
#
#
# hello()
# def wrapeper():
#     name="Sir" #this is not used
#     def conversation():
#         answear=""
#
#         name='Domle'
#         def hello ():
#             nonlocal name
#             print(f'Hello,{name}!')
#         def question():
#             print(f"how is your day {name}?")
#         def response():
#             nonlocal name
#             name = input('My name is ')
#             print(f'My name is:{name}')
#
#         def question2():
#             print(f"how was your day,{name}?")
#         def answear2():
#             nonlocal answear
#             answear=intput()
#
#         def question3():
#             if answear=="good":
#                 print("great")
#             else:
#                 print("how so?")
#         hello()
#         response()
#         question()
#         question2()
#         answear2()
#         question3()
#
# conversation()

#factorial!!!!!!!!

# def factorial(num):
#     resoult=1
#     n=range(1,num+1)
#     for i in n:
#         resoult*=i
#     return resoult
#
# print(factorial(1))

# def factorial(number):
#     number=list(range(1,number+1))
#
#     if len(number)<=1:
#         return 1
#     else:
#         return number[-1] * factorial(number[-2])
#
# print(factorial(3))


# def flatten_list(complex_list):
#     flat_list=[]
#     for obj_primary in complex_list:
#         if type(obj_primary )==list:
#             result= flatten_list(obj_primary)
#             flat_list.extend(result)
#         elif type(obj_primary)==tuple:
#             result = flatten_list(obj_primary)
#             flat_list.extend(result)
#         else:
#             flat_list.append(obj_primary)
#     return flat_list
# resoult=flatten_list(complex_list=data)
# print('Flat list:',resoult)


# data=[1,[2,[3,{'a','b'}]],4,[5,[6,{'a':'a','b':'b'}]],7,[8,[9,('a','b')]]]
# resoult=[1,2,3,4,5,6,7,8,9]
# def flatten_list(complex_list):
#     flat_list=[]
#     for obj_primary in complex_list:
#         if type(obj_primary )==list:
#             result= flatten_list(obj_primary)
#             flat_list.extend(result)
#         elif type(obj_primary)==tuple:
#             result = flatten_list(obj_primary)
#             flat_list.extend(result)
#         elif type(obj_primary)== set:
#             result = flatten_list(obj_primary)
#             flat_list.extend(result)
#         elif type(obj_primary)== dict:
#             result = flatten_list(obj_primary)
#             flat_list.extend(result)
#         else:
#             flat_list.append(obj_primary)
#     return flat_list
# resoult=flatten_list(complex_list=data)
# print('Flat list:',resoult)

def flatten_list(complex_list):
    flat_list = []
    for obj_primary in complex_list:
        if type(obj_primary) == str and len(obj_primary) == 1:
            flat_list.append(obj_primary)
        elif getattr(obj_primary, '__iter__', False):
            result = flatten_list(obj_primary)
            flat_list.extend(result)
        else:
            flat_list.append(obj_primary)
    return flat_list