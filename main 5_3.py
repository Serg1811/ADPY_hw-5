import datetime
import settings as sett
from application.salary import calculate_salary
from application.db.people import get_employees


def decor_logger(path):
    def _decor_logger(old_function):
        def new_function(*args, **kwargs):
            with open(path, 'a', encoding='utf-8', ) as f:
                result = old_function(*args, **kwargs)
                info_tuple = (str(datetime.datetime.now()), old_function.__name__, str(args), str(kwargs), str(result))
                info = '\n'.join(info_tuple) + '\n' * 2
                f.write(info)
            return result

        return new_function

    return _decor_logger


class UserInterface:
    @decor_logger('5_3.log')
    def __init__(self):
        self.q_dict = {'q': self.exit_}
        self.s_dict = {'s': self.start_menu}
        self.com = {self.start_menu: {'command': {**{'1': self.calculate_salary_menu,
                                                     '2': self.get_employees_menu},
                                                  **self.q_dict},
                                      'menu': sett.commands_start},
                    self.calculate_salary_menu: {'command': {**self.s_dict, **self.q_dict},
                                                 'menu': sett.commands_calculate_salary},
                    self.get_employees_menu: {'command': {**self.s_dict, **self.q_dict},
                                              'menu': sett.commands_get_employees}}

    @decor_logger('5_3.log')
    def exit_(self, param='До новых встреч!!!'):
        if param is None:
            param = 'До новых встреч!!!'
        print(f'\n{sett.str_turquoise}{sett.str_fat}{sett.str_italics}{param}\n{sett.str_reset}')
        return False

    @decor_logger('5_3.log')
    def command_table(self, commands: list):  # создаём таблицу
        def str_table(x0, x1, x2, x3, x4):
            print('{0}{1:^10}{2}{3:<40}{4}'.format(x0, x1, x2, x3, x4))

        str_table(chr(int('250F', 16)), chr(int('2501', 16)) * 10, chr(int('2533', 16)), chr(int('2501', 16)) * 40,
                  chr(int('2513', 16)))
        str_table(chr(int('2503', 16)), 'Команда', chr(int('2503', 16)), 'Описание операции'.center(40),
                  chr(int('2503', 16)))
        for command in commands:
            str_table(chr(int('2523', 16)), chr(int('2501', 16)) * 10, chr(int('254B', 16)), chr(int('2501', 16)) * 40,
                      chr(int('252B', 16)))
            str_table(chr(int('2503', 16)), command['command'], chr(int('2503', 16)), command['description'],
                      chr(int('2503', 16)))
        str_table(chr(int('2517', 16)), chr(int('2501', 16)) * 10, chr(int('253B', 16)), chr(int('2501', 16)) * 40,
                  chr(int('251B', 16)))

    @decor_logger('5_3.log')
    def command_request(self, input_dict: dict, s='\nВведите команду: ', key=True):  # Запроскоманд
        command = input(s).lower()
        print()
        if command in input_dict:
            return input_dict[command]
        elif key:
            print(f'\n{sett.str_red}Команда не определена{sett.str_reset}\n')
            return self.command_request
        else:
            return command

    @decor_logger('5_3.log')
    def calculate_salary_menu(self):
        calculate_salary()
        return self.command_request

    @decor_logger('5_3.log')
    def get_employees_menu(self):
        get_employees()
        return self.command_request

    @decor_logger('5_3.log')
    def start_menu(self):
        return self.command_request


def current_date_str():
    current_date = datetime.datetime.now()
    return current_date.strftime('%d/%m/%y\n%H:%M:%S')


def main():
    c = UserInterface()
    command = c.start_menu
    input_dict = {}
    while command:
        if command == c.command_request:
            res = command(input_dict)
        elif command == c.exit_:
            res = command()
        else:
            res = command()
            c.command_table(c.com[command]['menu'])
            input_dict = c.com[command]['command']
        command = res


if __name__ == '__main__':
    print(current_date_str())
    main()
