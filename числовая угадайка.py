from random import randint
import time


def is_valid(c):
    if c.isdigit() == False:
        print('Допускается вводить только цифры')
        return False
    else:
        c = int(c)
        if c > b or c < a:
            print('Вы указали число не из диапазоне, попробуйте снова')
            return False
        return True





def ugadai(a,b):
    chislo = randint(a,b)
    while True:

        print(f'Угадайте число от {a} до {b}')
        time.sleep(1)
        c = input('Введите число ' )
        time.sleep(3)
        if is_valid(c) == True:
            c = int(c)


            if c > chislo:
                print(f'Загаданное число меньше {c}, попробуйте ещё раз')
                time.sleep(2)
            elif c < chislo:
                print(f'Загаданное число больше {c} попробуйте ещё раз')
                time.sleep(2)
            elif c == chislo:
                print(f'Поздравляю, вы угадали число! Это действительно число {chislo}')
                time.sleep(5)
                break
        else:
            continue
a, b = int(input('Будем угадывать от этого числа ')), int(input('До этого '))
ugadai(a,b)