def show_letters(some_str):
    for i in some_str:
            yield''.join([letter for letter in some_str if letter.isalpha()])
random_str = show_letters('A!sdf 09 _ w')
print(next(random_str))
