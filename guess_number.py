import numpy as np


def computer_guess(num):
    low = 1
    high = 100
    guess = 50
    count = 0

    while guess != num:

        guess = (low + high) // 2

        print("Пробую число %s..." % guess)
        if guess > num:
            high = guess
            count += 1
        elif guess < num:
            low = guess + 1
            count += 1

    print("Число %s отгадано за %s попытки(ок)." % (guess, count))


def main():
    num = int(input("Загадайте число от 1 до 100: "))

    if num < 1 or num > 100:
        print("Загадываемое число должно быть в интервале от 1 до 100.")
    else:
        computer_guess(num)


if __name__ == '__main__':
    main()
