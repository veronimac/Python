prdct = input('Категория товара:').lower()
price = 0
if prdct == 'продукты':
    price = input('Цена:').lower()
else:
    if price<100:
        print('Попробуйте нашу выпечку!')
    elif 99<price<500:
        print('Как насчёт орехов в шоколаде?')
    elif price>499:
        print('Попробуйте экзотические фрукты!')
    else:
        print('Загляните в товары для дома!')