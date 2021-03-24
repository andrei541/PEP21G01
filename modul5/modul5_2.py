import random

def check_cpu():
    output = """top - 16:18:11 up  5:12,  2 users,  load average: 0.12, 0.03, 0.01
Tasks: 138 total,   1 running, 137 sleeping,   0 stopped,   0 zombie
%Cpu(s):  {} us,  0.0 sy,  0.0 ni, {} id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   7962.4 total,   7176.4 free,    164.8 used,    621.1 buff/cache
MiB Swap:   1971.0 total,   1971.0 free,      0.0 used.   7552.2 avail Mem """
    while True:
        yield output.format(random.randint(0, 100), random.randint(0, 100))

from time import sleep

for i in check_cpu():
    counter=0
    for line in i.splitlines():
        if line.startswith("%Cpu"):
            list1=line.split(":")[1].split(",")
            print(int(list1[0].strip().split(" ")[0]))
            print(int(list1[3].strip().split(" ")[0]))
            if (int(list1[0].strip().split(' ')[0]) > 80 or int(list1[3].strip().split(' ')[0]) > 80):
                print('Alarm!!!')

            sleep(2)





generators

def values_3():
    yield 1
    yield 2
    yield 3

gen=values_3()
print(type(gen))
gen.__next__()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def values_inf():
    counter=0
    while True:
        counter+=1
        yield counter

gen = values_inf()
for value in gen:
    print(value)

def generator():
        for counter in range(10,25):
            yield counter
            counter += 1


fun=generator()
for value in fun:
    print(value)

def string_iterator(name):
    for carac in name:
        yield carac
fun=string_iterator("andrei")
for i in fun:
    move=input("type anything to move to the next caracter:")
    if move!=None:
        print(i)


import random
def ip_generator(subnet):
    ip,masc =subnet.split("/")
    print(ip,masc,sep="\n")
    if masc!="24":
        raise ValueError("masc is incorect")
    ip4=ip.rsplit(".",maxsplit=1)[0]

    for i in random.sample(range(0,256),256):
        new_ip=ip4+"."+str(i)
        yield new_ip+"/"+masc


ip_gen=ip_generator("192.168.0.3/24")
for j in ip_gen:
    print(j)

