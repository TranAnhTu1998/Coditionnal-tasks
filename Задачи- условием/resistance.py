
def caculate_resistance_electrical_circuit():
    try:
        print("Введите исходные данные:")
        r1 = float(input("Величина первого сопротивления(Ом) : "))
        r2 = float(input(" Величина второго сопротивления(Ом) : "))
        tc = input("Тип соединения (1 - последовательное, 2 - параллельное) : ")
        r = 0
        if tc == '1':
            r = r1 + r2
        elif tc == '2':
            r = 1 / (1 / r1 + 1 / r2)
            r = round(r, 2)
        print("Сопротивление цепи : ", r, "Ом")
    except:
        print("Ошибка! Вы ввели неверные данные!!")

