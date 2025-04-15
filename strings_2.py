import math

radius, side_length = map(float, input("введите радиус окружности и сторону квадрата: ").split())

circumference = 2 * math.pi * radius  
circle_area = math.pi * radius**2   
square_area = side_length**2    

percentage = (circle_area / square_area) * 100

circumference_rounded = round(circumference, 2)
percentage_rounded = round(percentage, 2)

print(f'длина окружности равна {circumference_rounded}. Площадь круга составляет {percentage_rounded}% от площади квадрата.')
