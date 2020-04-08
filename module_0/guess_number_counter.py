import numpy as np


def computer_guess_test():
    low = 1
    high = 100
    guess = 50
    count = 0
    num = np.random.randint(1, 100)

    while guess != num:
        guess = (low + high) // 2
        if guess > num:
            high = guess
            count += 1
        elif guess < num:
            low = guess + 1
            count += 1
    return count


def score_game(computer_guess_test):
    counter = []

    for i in range(1, 1001):
        c = computer_guess_test()
        counter.append(c)
    score = int(np.mean(counter))
    print('В среднем компьютер угадывает число за %s попытки(ок).' % score)


score_game(computer_guess_test)
