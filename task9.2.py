import sys
"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""

def a(distance_km):
    w = ((distance_km*1000)//140) * 0.25 + 4
    return w
h = a(200)
print(int(h))