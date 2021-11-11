
def checks_year_leap():
    try:
        y = int(input("Введите год : "))
        if y % 4 == 0:
            print("Год ", y, " - високосный.")
        else:
            print(y , "год - не високосный")
    except:
        print("Ошибка! Вы ввели неверные данные!!")

