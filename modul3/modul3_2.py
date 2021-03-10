# def my_func(arg1,arg2,arg=3):
#     print(arg1,arg2,arg3)
#
# my_func("value 1","value 2")
#
#
#
# def prime(max_prime):
#     my_primes=[]
#
#     for number in range(1, max_prime + 1):
#         if number < 3:
#             my_primes.append(number)
#
#             continue
#         for divider in range(2, number):
#             if number % divider == 0:
#
#                 break
#         else:
#             my_primes.append(number)
#     return my_primes
# my_primes=prime(21)
# print(my_primes)
# my_list=[1,2,3]
# list_itter=my_list.__iter__()
# for number in my_list:
#     print(number)

# number=1
# print(id(number))
# number+=1
# print(id(number))
#
# print(id(my_list))
# my_list.append(4)
# print(my_list)
# print(id(my_list))
# print(my_list ==[1,2,3,4])
# print(id(my_list),id(my_list.append(5)))
#
# new_object1="my_str_{}".format("1")
# print(new_object1)
# new_object2=[1,2,3].append(4)
# print(new_object2)

# my_list=[]
# print(type(my_list)==str)
# print(type(my_list)==list)

# data=[1,[2,[3]],4,[5,[6]],7,[8,[9]]]
# resoult=[1,2,3,4,5,6,7,8,9]
# def flatten_list(complex_list):
#     flat_list=[]
#     for obj_primary in complex_list:
#         if type(obj_primary )==list:
#             for obj_secondary in obj_primary:
#                 if  type(obj_secondary)==list:
#                     for obj_third in obj_secondary:
#                         if type(obj_third)==list:
#                           pass
#                         else:
#                             flat_list.append(obj_third)
#                 else:
#                     flat_list.append(obj_secondary)
#         else:
#             flat_list.append(obj_primary)
#     return flat_list
# resoult=flatten_list(complex_list=data)
# print(resoult)


# print(11 & 10)
# print((11).__and__(10))
# #1010-10
# #1011-11
# #1010-10
# print(11^10)
# print((11).__xor__(10))
# resoult=(11).__xor__(10)
# resoult=resoult.__xor__(10)
# print("resoult este:",resoult)
# #1011-11
# #1010-10
# #1001-1

#

# def encripted(text,number=144):
#     my_list=[]
#     for letter in text:
#         my_letter=chr(ord(letter).__xor__(number))
#         my_list.append(my_letter)
#     resoult="".join(my_list)
#     return resoult
#
# print(encripted(text))

# def add_number():
#     suma=0
#     while suma<100:
#         number=int(input("add your number here"))
#

data=[1,[2,[3]],4,[5,[6]],7,[8,[9]]]
resoult=[1,2,3,4,5,6,7,8,9]
def flatten_list(complex_list):
    flat_list=[]
    for obj_primary in complex_list:
        if type(obj_primary )==list:
            result= flatten_list(obj_primary)
            flat_list.extend(result)
        else:
            flat_list.append(obj_primary)
    return flat_list
resoult=flatten_list(complex_list=data)
print('Flat list:',resoult)