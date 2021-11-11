import sys
from rich.table import Table
from rich.console import Console
from rich import print

from ring import calculate_area_ring

from timems import converts_time_seconds
from yearr import checks_year_leap
from resistance import caculate_resistance_electrical_circuit
console = Console()


def programm(method, title, t_key=False):
    b1 = True
    while b1:
        str_out = ''
        try:
            method()
        except:
            console.print("Введенная вами строка недействительна,", "произошла ошибока ", sys.exc_info()[0], '!!!!')

        b11 = True
        while b11:
            contin = console.input("Попробовать ещё раз ? (y/n - д/н)")

            if contin == 'y' or contin == 'Y' or contin == 'д' or contin == 'Д':
                b1 = True
                b11 = False
            elif contin == 'n' or contin == 'N' or contin == 'н' or contin == 'Н':
                b1 = False
                b11 = False
            else:
                console.print("Недействительное значение, попробуйте еще раз!!!")
                b11 = True


def select_method():
    console.print("***Добро пожаловать в программу \"Задачи с условием\" ****")
    table = Table(title="Списоки методы шифра:")
    table.add_column("№", justify="center", style="cyan", no_wrap=True)
    table.add_column("Линейные задачи", style="magenta")

    table.add_row("1", "Программа вычисления площади кольца.")
    table.add_row("2", "Программа, которая переводит время из минут и секунд в секунды. ")
    table.add_row("3", "Программа, которая проверяет, является ли год високосным. ")
    table.add_row("4", "Программа вычисления сопротивления электрической цепи, состоящей из двух сопротивлений.")
    table.add_row("5", "Ппрограмма решения квадратного уравнения.")
    table.add_row("6", "Программа вычисления стоимости покупки с учетом скидки. Скидка в 10% предоставляется, "
                       "если сумма покупки больше 1000 руб")
    table.add_row("7", "Программа проверки знания даты начала второй мировой войны.")
    table.add_row("8", "Программа, которая сравнивает два введенных с клавиатуры числа")
    table.add_row("9", "Программа, которая запрашивает у пользователя номер месяца и затем выводит соответствующее "
                       "название времени года")

    table.add_row("e", "Нажмите клавишу \"е or в\", чтобы выйти из програмы.")

    console.print(table)

    select_x = input("Какой номер программы вы выберете ? ")

    sel = select_x

    if sel == '1':
        programm(calculate_area_ring, "Программа вычисления площади кольца.", True)

    elif sel == '2':
        programm(converts_time_seconds, "Программа, которая переводит время из минут и секунд в секунды. ", True)

    elif sel == '3':
        programm(checks_year_leap, "Программа, которая проверяет, является ли год високосным.", True)

    elif sel == '4':
        programm(caculate_resistance_electrical_circuit,
                 "Программа вычисления сопротивления электрической цепи, состоящей из двух сопротивлений.", True)

    elif sel == 'e' or sel == 'E' or sel == 'в' or sel == 'В':
        exit()

    else:
        console.print(
            "Произошла ошибка. Возможно, вы ввели неправильный номер метода или метод не был разработан "
            "программистом.!!!")


def loop_method():
    while True:
        select_method()


loop_method()
