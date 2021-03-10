shop1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}
shop2 = {'mere': 11, 'pere': 15, 'prune': 6}
shop3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}
need_to_buy = {'mere': 2, 'pere': 3, 'prune': 6}
mag_dispo = {'Aldi': shop1, 'Penny': shop2, 'Mega': shop3}


def best_buy(mag_dispo, need_to_buy):
    min_price = None
    print(id(min_price))
    nume_mag = ''
    for shop_name, content in mag_dispo.items():
        sum1 = 0
        for product, quantity in need_to_buy.items():
            sum1 = sum1 + content.get(product) * quantity
        print('Suma partiala in:', shop_name, '+', sum1)
        if min_price is None or min_price > sum1:
            min_price = sum1
            nume_mag = shop_name

    print(min_price, nume_mag)


result = best_buy(mag_dispo=mag_dispo, need_to_buy=need_to_buy)
print(id(result))