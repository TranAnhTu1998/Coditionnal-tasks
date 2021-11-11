
def converts_time_seconds():
    try:
        ms = input("Ведите время (минут. секунд) : ")
        arrMS = ms.split('.')
        minutes = int(arrMS[0])
        seconds = int(arrMS[1])
        if seconds > 60:
            print("Ошибка! Количество секунд не может быть больше 60")
        else:
            print("Время из  минут и секунд в секунды : ", minutes * 60 + seconds, 's')
    except:
        print("Ошибка! Вы ввели неверные данные!!")

