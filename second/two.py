def ladder_counter(n):
    list = []
    condition = n > 0
    number = 1
    while condition:
        for i in range(number):
            list.append(number)
            n -= 1
            if n <= 0:
                condition = False
                break
        number += 1
    print(*list)


if __name__ == '__main__':
    ladder_counter(24)