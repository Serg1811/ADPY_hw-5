import datetime
from settings import *
from application.salary import *
from application.db.people import *


class UserInterface:
    def __init__(self):
        self.q_dict = {'q': {'command': self.exit_, 'param': None}}
        self.s_dict = {'s': {'command': self.start_menu, 'param': None}}

    def exit_(self, param='До новых встреч!!!'):
        if param is None:
            param = 'До новых встреч!!!'
        print(f'\n{str_turquoise}{str_fat}{str_italics}{param}\n{str_reset}')
        return exit()

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

    def command_request(self, input_dict: dict, s='\nВведите команду: ', key=True):  # Запроскоманд
        command = input(s).lower()
        print()
        if command in input_dict:
            return input_dict[command]['command'](input_dict[command]['param'])
        elif key:
            print(f'\n{str_red}Команда не определена{str_reset}\n')
            return self.command_request(input_dict)
        else:
            return command

    def calculate_salary_menu(self, param=None):
        calculate_salary()
        input_dict = {**self.s_dict, **self.q_dict}
        self.command_table(commands_calculate_salary)
        return self.command_request(input_dict, '\nВведите команду: ')

    def get_employees_menu(self, param=None):
        get_employees()
        input_dict = {**self.s_dict, **self.q_dict}
        self.command_table(commands_get_employees)
        return self.command_request(input_dict, '\nВведите команду: ')

    def start_menu(self, param=None):
        if param is not None:
            print(param)
        input_dict = {**{'1': {'command': self.calculate_salary_menu, 'param': None},
                         '2': {'command': self.get_employees_menu, 'param': None}},
                      **self.q_dict}
        self.command_table(commands_start)
        return self.command_request(input_dict)


def current_date_str():
    current_date = datetime.datetime.now()
    return current_date.strftime('%d/%m/%y\n%H:%M:%S')


if __name__ == '__main__':
    print(current_date_str())
    c = UserInterface()
    c.start_menu()
