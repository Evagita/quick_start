# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток\n")
    return score


print("""Решение задачи "в лоб" """)
score_game(game_core_v1)


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # выход из цикла, если угадали


print("""Решение задачи с непрерывным сравнением """)
score_game(game_core_v2)


def game_bin_predict(number):
    '''Используем бирнарный поиск. По сути, это цикл действий:
    - находим середину отрезка чисел для разбиения на два под-отрезка,
    - сравниваем загаданное число с серединой,
    - переходим к тому под-отрезку, к которому принадлежит загаданное число (переопределяем край отрезка).
    Предварительная сортировка чисел не требуется - отрезок есть часть натурального ряда.
    Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    left_num, right_num = 1, 100
    predict = 50
    while number != predict:
        count += 1
        if number > predict:
            left_num = predict + 1
        elif number < predict:
            right_num = predict - 1
        predict = (left_num + right_num) // 2
    return count


print("Решение задачи с использованием бинарного поиска")
score_game(game_bin_predict)
