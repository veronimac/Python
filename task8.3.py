"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).
Ученикам без допуска должно печататься "Вы отчислены".
Выдачу допуска реализуй как функцию.
"""
def exam(number_of_students):
    for i in range(0, number_of_students):
        score = int(input('Enter your score: '))
        if score > 50:
            print('Допущен')
        else:
            print('Вы отчислены')


exam(int(input('Enter number of students')))
