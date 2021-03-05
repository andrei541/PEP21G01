# 20P
# 1) Prove "and" operation takes precedence over "or" operation by setting
# parentheses in the following expression (False or False and True or True)

or_variable1=(False or False)
or_variable2=(True or True)
print(or_variable1 and or_variable2)
#-------------------------------------
# print(False or False)and(True or True)
#########################################################
# 40P
# 2) Get from input two different times in the format dd:hh:mm:ss and print
 # the difference in seconds between them. The convert the result back to the initial
 # format and print that also
 # dd is number of days
 # hh si number of hours (00-23)
 # hh is number of hours (00-23)
 # mm is number od minutes (00-59)
 # ss is number of seconds (00-59)
start_time=input("Add a starting time in the format dd:hh:mm:ss=")
end_time=input("Add a end time in the format dd:hh:mm:ss=")
#start time
dd1=int(start_time[0:2])
hh1=int(start_time[3:5])
mm1=int(start_time[6:8])
ss1=int(start_time[9:10+1])
#end time
dd2=int(end_time[0:2])
hh2=int(end_time[3:5])
mm2=int(end_time[6:8])
ss2=int(end_time[9:10+1])
#start time conversion
dd1_to_ss1=dd1*86.400
if hh1 in range(0,24):
    hh1_to_ss1=hh1*3600
else:
    print("invalid hour")
if mm1 in range(0,60):
    mm1_to_ss1=mm1*60
else:
    print("invalid minutes")
total_start_seconds=dd1_to_ss1+hh1_to_ss1+mm1_to_ss1+ss1
#end time conversion
dd2_to_ss2=dd2*86.400
if hh2 in range(0,24):
    hh2_to_ss2=hh2*3600
else:
    print("invalid hour in end time")
if mm2 in range(0,60):
    mm2_to_ss2=mm2*60
else:
    print("invalid minutes in end time")
    #diference calculation
total_end_seconds=dd2_to_ss2+hh2_to_ss2+mm2_to_ss2+ss2
dif_sec=total_start_seconds-total_end_seconds
print("the difference in seconds is:",dif_sec)
#conversion back to dd:hh:mm:ss format
sec=dif_sec                  ##########################################################################
day=int(sec/60/60/24%365)    # for the record:pentru conversie a trebuit neaarat sa consult internetul#
hour=int(sec/60/60%24)       # deci nu stiu exact ce si cat de corect este                            #
min=int(sec/60%60)           ##########################################################################
sec=int(sec%60)
print(f"diferece in formated resoult = {day}:{hour}:{min}:{sec}")

# 40P
# Calculate the diagonal of a rectangle with sides 10 and 15

side1=10
side2=15
pow=(side1**2)+(side2**2)
radical=pow**(1/2)
print(radical)
print(int(radical))