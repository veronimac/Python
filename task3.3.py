prdct1 = int(input(К оплате:))
prdct2 = int(input(К оплате:))
prdct3 = int(input(К оплате:))
amount = sum([prdct1+prdct2+prdct3])
if prdct1 < prdct2 and prdct2 < prdct3:
    print('Акция!')
    print('К оплате:', amount/2)
elif prdct3 < prdct2 and prdct2 < prdct1:
    print('Акция!')
    print('К оплате:', amount/3)
else:
    print('К оплате:', amount)

