# shop1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}
# shop2 = {'mere': 11, 'pere': 15, 'prune': 6}
# shop3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}
# need_to_buy = {'mere': 2, 'pere': 3, 'prune': 6}
# mag_dispo = {'Aldi': shop1, 'Penny': shop2, 'Mega': shop3}
#
#
# def best_buy(mag_dispo, need_to_buy):
#     min_price = None
#     print(id(min_price))
#     nume_mag = ''
#     for shop_name, content in mag_dispo.items():
#         sum1 = 0
#         for product, quantity in need_to_buy.items():
#             sum1 = sum1 + content.get(product) * quantity
#         print('Suma partiala in:', shop_name, '+', sum1)
#         if min_price is None or min_price > sum1:
#             min_price = sum1
#             nume_mag = shop_name



    # print(min_price, nume_mag)
#
# result = best_buy(mag_dispo=mag_dispo, need_to_buy=need_to_buy)
# print(id(result))





lista_tel={"num1":1245673,"num2":3457965,"num3":6788798}

def suma_numerelor(lista_telefoane):
    resoult=[]
    for utilizator in lista_telefoane:
        var=lista_telefoane.get(utilizator)
        digit_sum=0
        for digit in str(var):
            digit_sum+=int(digit)
        if digit_sum > 50:
            resoult.append(utilizator)
    return resoult


print(suma_numerelor(lista_tel))


my_dict = {'Ana': 762399332,'Adi': 723432145,'Bogdan': 750567987}
def return_name(dict):
    lista = []
    for nume,nr in dict.items():
        s = 0
        for cifra in str(nr):
            s = s + int(cifra)
        if (s > 50):
            lista.append(nume)
    return lista
print(return_name(my_dict))








