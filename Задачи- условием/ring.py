import math


def calculate_area_ring():
    print("Вычисление площади кольца.")
    print("Введите исходные данные:")
    rr = float(input("Радиус кольца (см) : "))
    hr = float(input("Радиус отверстия (см) : "))
    if hr > rr:
        print("Ошибка! Радиус отверстия не может быть больше радиуса кольца.")
    else:
        print("Площади кольца : ", math.pi * (rr * rr - hr * hr))



