def calculator():
    print("Через пробел введите два числа ")
    a, b = map(int, input().split())
    sign = input("Введите один из перечисленных знаков: +, -, /, //, *, ** \n")
    match sign:
        case "+":
            return a + b
        case "-":
            return a - b
        case "/":
            return a / b
        case "//":
            return a // b
        case "*":
            return a * b
        case "**":
            return a ** b


if __name__ == '__main__':
    print(calculator())
