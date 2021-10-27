import datetime


def decor_logger(old_function):
    def new_function(*args, **kwargs):
        with open('5_1.log', 'a', encoding='utf-8', ) as f:
            result = old_function(*args, **kwargs)
            info_tuple = (str(datetime.datetime.now()), old_function.__name__, str(args), str(kwargs), str(result))
            info = '\n'.join(info_tuple) + '\n' * 2
            f.write(info)
        return result

    return new_function


@decor_logger
def operation(a, b, action):
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '**':
        return a ** b
    elif action == '/':
        return a / b
    elif action == '//':
        return a // b
    elif action == '%':
        return a % b
    else:
        return 'Операция не определена'


if __name__ == '__main__':
    print(operation(7, 8, action='+'))
    print(operation(7, 8, action='-'))
    print(operation(7, 8, action='*'))
    print(operation(7, 8, action='**'))
    print(operation(7, 8, action='/'))
    print(operation(7, 8, action='//'))
    print(operation(7, 8, action='%'))
    print(operation(7, 8, action='+-'))
    print(operation(7, 8, action='///'))
