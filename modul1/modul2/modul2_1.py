# number_3 = 3
# print(number_3)
# number_three=3
# print(number_three)
# response = type(number_3)
# print (response)
# response = type(number_three)
# print (response)
# var1=123
# print (type(var1))
# #integer base
# bin_number = 0b10
# print(bin_number)
#
# octal_number= 0o10
# print(octal_number)
# hex_number=0x10
# print(hex_number)
# print(bin_number+octal_number)
# print(bin_number.__mul__(octal_number))
# print(3**3)
# print(number_3.__mul__(number_3.__mul__(number_3)))
# print(pow(3,3))
# print(number_3.__pow__(3))
# #division
# print("division")
# print(number_3/3)
# result=number_3/3
# print(type(result))
# print(number_3.__truediv__(3))
# #exercitiu
# a=3
# b=4
# c=5
# radical=(b**2-4*a*c)**(1/2)
# x=(-b-radical)/(2*a)
# print (type(x))
# print(x)
# # ex using methods
# _4ac = (4).__mul__(a.__mul__(c))
# b_sqr = b.__pow__(2)
# sqr_result = b_sqr.__sub__(_4ac)
# sqrt_result = pow(sqr_result, (1).__truediv__(2))
# minus_b = (0).__sub__(b)
# # div_up = minus_b.__add__(sqrt_result)
# div_up = sqrt_result.__add__(minus_b)
# div_down = (2).__mul__(a)
# result = div_up.__truediv__(div_down)
# print(result)
string1="This is a string \n this is a new line"
string2="This is a string2"
string3='''This a string3
 this is a new line 
 and another'''
# x="This is a new line\n"
# print(x*100)
# print(u.__mul__(100))
# string1="Andrei"
# string2="Patcas"
# string3="declaratie"
# formatable_string=f'Subsenatul:{string1},{string2} \nDeclar: {string3}'
# print (formatable_string)
string1='Subsemnatul:{}'
string2='Declar:{}'
resoult=string1.format('Patcas Andrei')
declaratie=string2.format('urmatoarele chestii')
print(resoult)
print(declaratie)
resoult=string1.replace('{','(')
resoult=resoult.replace('}',')')
print(resoult)