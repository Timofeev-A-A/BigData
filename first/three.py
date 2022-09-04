import math


def square_of_triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


if __name__ == '__main__':
    print("Через пробел введите стороны треугольника \n")
    a, b, c = map(int, input().split())
    print(square_of_triangle(a, b, c))
