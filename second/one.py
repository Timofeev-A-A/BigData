def sq_sum_counter():
    sum_of_digits = 0
    sq_sum = 0
    while True:
        digit = int(input())
        sum_of_digits += digit
        sq_sum += digit ** 2
        if sum_of_digits == 0:
            break
    print(sq_sum)


if __name__ == '__main__':
    sq_sum_counter()
