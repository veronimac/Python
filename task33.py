"""
Даны два списка чисел. Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
"""
list1 = [1,2,3,4,5,6]
list2 = [4,16,1,3,8,2]
listL1 = set(list1)
listL2 = set(list2)
print(listL1 & listL2)