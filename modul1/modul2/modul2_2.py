# # #slice
# # string1='My string'
# # resoult = string1[0]
# # print(resoult)
# # resoult=string1[0:4]
# # print(resoult)
# #
# # resoult=string1[4:]
# # print(resoult)
# #
# # resoult=string1[4:8]
# # print(resoult)
# # # T E X T
# # # 0 1 2 3
# # #-4-3-2-1
# # resoult=string1[4:-1]
# # print(resoult)
# # resoult=string1[-5:-1]
# # print(resoult)
# #
# # resoult=string1[0:8:2]
# # print(resoult)
# # resoult=string1[0::2]
# # print(resoult)
# #
# # encode='My test to encode'
# # resoult= encode[0::2] + encode[1::2]
# # print(resoult)
# # encode='My test to encode'
# # resoult= encode[5:] + encode[0:5]
# # print(resoult)
# # encode='My test to encode'
# # resoult= encode[-5:] + encode[0:5]
# # print(resoult)
# # resoult=resoult[-5:]+ resoult[:-5]
# # print(resoult)
# # resoult=encode[::-1]
# # print('reverse:',resoult)
# # resoult=resoult[::-1]
# # print('original:',resoult)
# encode='My test to encode'
# resoult=encode[5:] + encode[:-5]
# print (resoult)
# print()
#
# print(encode[-1:-10:-1])


#chr , ord

print(chr(100))
print(ord('d'))
encode='abc'
result=chr(ord(encode[0])+1)+\
       chr(ord(encode[1])+1)+\
       chr(ord(encode[2])+1)
print(result)
#cast
print(ord('1'))
print(int('1'))
print(type(int('1')))

#ex: time difference

# start_time =input("Start time: ")
# end_time = input("End time:")
# start_time_m = int(start_time[0:2])
# start_time_s = int(start_time[3:])
# start_time_conv = 60 * start_time_m + start_time_s
# end_time_m = int(end_time[0:2])
# end_time_s = int(end_time[3:])
# end_time_conv = 60 * end_time_m + end_time_s
# diff = end_time_conv - start_time_conv
# print(diff)
# my_input=complex(input('Enter your text here:'))
# print('yout tiped: ',my_input)

#None
# print_result=print("exemplu")
# print("rezultatul este:",print_result)
# print(type(print_result))
#
# print(None)

#bool objects
# print(True)
# print(False)
#
# print(id(None),id(True),id(False))

# var_1=str(input("Primul string: "))
# var_2=str(input("Al doilea string: "))
# print("Primul numar este mai mic:",var_1.__lt__(var_2))
# print("Primul numar este mai mare",var_1.__gt__(var_2))
# print("egalitate:",var_1.__eq__(var_2))
# print("diferenta:",var_1.__ne__(var_2))

# a=input("primul:")
# b=input("al doileea:")
# print('a > b: ',a.__gt__(b))
# print('a < b: ',a.__lt__(b))
# print('a >= b: ',a.__ge__(b))
# print('a <= b: ',a.__le__(b))
# print('a == b: ',a.__eq__(b))
# print('a != b: ',a.__ne__(b))

# var_1="abc\n"
# var_2='a'+'b'+'c'
# print(f'var_1={var_1},var_2={var_2}')
# print('==',var_1==var_2)
# print(var_1 is var_2)
print("A".center(5,"_"))
print("A_A".center(5,"_"))
print("A_A_A".center(5,"_"))
print(" _A_ ".center(5,"_"))
