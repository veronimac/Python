"""
�������� ������� ������� ��������� 2 ����� � ������� ��� ����� ����� ���� ������� ������� �� 3.
�������� ��������� ������� ������� �����:
"������ ������� ������� ��� ����� ����� ����� � � ����� �"(���� ���������� ����� ��� ��������� �������)
� �������� ������� ����� ������ ����� ���������� ����� �� �����������
"""
def decorate(f):
    print('������ ������� ������� ��� ����� ����� ' + str(f[0]) + ' � ' + str(f[1]))
    print(*f[2:])

def func(a, b):
    stack = [a, b]
    for i in range(a, b + 1):
        if i % 3 == 0:
            stack.append(i)
    return stack

decorate(func(int(input('Enter number: ')), int(input('Enter number: '))))