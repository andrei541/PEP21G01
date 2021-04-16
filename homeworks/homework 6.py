"""" Homework 6 - needs to be presented before exam day
# O fabrica de masini are nevoie de un obiect iterabil care sa contina seriile si loturile masinilor produse in ziua respectiva.
# Seriile si loturile sunt numere intregi de tip int
# Un lot este alcatuit din 20 de masini si primele 10 din lot sunt cu volan pe dreapta iar urmatoarele 10 cu volan pe stanga
# Numerotarea loturilor incepe de la prima masina produsa cu seria 1 si lot 1
# Ziua de lucru stocata in obiectul contruit de voi poate incepe cu orice numar de serie si numarul de bucati produse in acea zi poate avea orice valoare
# Obiectul iterat va returna numerele loturilor din care fac parte masinile din acea zi, numerotarea lor a inceput de la prima masina produsa cu seria 0 si lot 0
# Masinile cu serii pare sunt cu volan pe dreapta iar cele cu serii impare cu volan pe stanga
# 1)Definire: 40p
#   - Creati o clasa pentru un obiect iterabil
#    a) constructorul primeste doua argumente de tip int, seria de inceput si numarul de bucati. ex: (101, 41) 10p
#    b) obiectul are doua metode: prima returneaza o lista cu seriile cu volan pe dreapta si a doua o lista cu seriile cu volan pe stanga 15p
#    c) iterator-ul returnat de object va comtine loturile din care fac parte seriile din obiectul curent  15p
# 2) Executie: 40p
# - Creati o instanta a clasei de mai sus dand ca argumente: serie_inceput 314, bucati 90. 10p
# - Iterati obiectul creat si salvati fiecare valoare din iteratie in acelas fisier pe linie noua. 30p
# 3) Documentatie: 20p
#    a) adaugati type hints 5p
#    a) documentati modulul 5p
#    b) documentati clasele 5p
#    c) documentati metodele 5p
"""



class Car_factory():
    def __init__(self,date:str):
        self.date=date

    def __iter__(self):
        all_cars_series = []
        for series in all_cars_series:
            all_cars_series.extend(series)

            return CarsIter(all_cars_series)





    def add_cars(self,serie:int,nr_buc:int):
#adauga serile masinilor si numarul de bucati
        all_cars_series=[]
        right_steering = []
        left_steering = []
        self.serie=serie
        self.nr_buc=nr_buc

        for  i in range(nr_buc):
            all_cars_series.append(serie+i)
            all_cars_series=all_cars_series

        for x in all_cars_series: #iteram toate serile masinilor si stabilim care sunt cu volan pe dreapta si care
            if x % 2 ==0:         # sunt cu volan pe stanga
                right_steering.append(x)
            else:
                left_steering.append(x)
        print("right steering wheel:",right_steering)
        print("left steering wheel:",left_steering)
        for i in right_steering:
            f=open('../modul6/my_file', 'w')
            f.write("right steering wheel:"+str(i)+'\n')
        for x in left_steering:
            f = open('../modul6/my_file', 'w')
            f.write("left steering wheel:" + str(x) + '\n')




class CarsIter():
#iteratorul
    def __init__(self,serie:list):
        self.serie=series
    def __iter__(self):
        return self
    def __next__(self):
        if not self.serie:
            raise StopIteration
        else:
            return self.serie.pop(0)



car1=Car_factory("12.04.2021")
car1.add_cars(101,30)
car1.add_cars(314,90)



