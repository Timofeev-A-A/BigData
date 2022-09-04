import three
import math


def find_square():
    figure = input("type one of the following: triangle, rectangle, circle \n")
    match figure:
        case "triangle":
            print("Через пробел введите стороны треугольника \n")
            a, b, c = map(int, input().split())
            square = three.square_of_triangle(a, b, c)
        case "rectangle":
            print("Через пробел введите стороны прямоугольника \n")
            a, b = map(int, input().split())
            square = a * b
        case "circle":
            r = int(input("Введите радиус круга \n"))
            square = math.pi * math.pow(r, 2)
    return {figure: square}


if __name__ == '__main__':
    print(find_square())
