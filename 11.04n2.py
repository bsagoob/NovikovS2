import math

def calculate_circle_properties(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return circumference, area

radius = float(input("Введите радиус: "))
side_length = float(input("Введите сторону квадрата: "))

circumference, area = calculate_circle_properties(radius)
square_area = side_length ** 2

area_ratio = (area / square_area) * 100

print(f"Длина окружности равна {circumference:.2f}. Площадь круга составляет {area_ratio:.2f}% от площади квадрата.")
