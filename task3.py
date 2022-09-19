def main():
    l_char = ['=','?','*','^','$','№','@','_']
    l = []
    print('Enter login:')
    login = input()
    for i in login:
        if i in l_char:
            l.append(i)
        else:
            break
    print(' '.join(l))
