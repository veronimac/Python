def add_pineapple_and_salad(func_list):
    func_list.extend(['salad', 'pineapple'])
    print('������ ������:')
    n = 1
    for i in func_list:
        print(str(n) + '. ' + i)
        n += 1


def make_list(list_):
    return list_

add_pineapple_and_salad(make_list(['bread', 'sauce', 'tomatoes', 'chicken', 'sauce']))
