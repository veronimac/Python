"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)

news = set(newspaper)
magazi = set(magazine)
bit = set(both)

pre_RES = news | magazi
RESULT = pre_RES.difference(bit)

print(len(RESULT))