eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def shifr_en(c,k):
    c_shifr = ''

    for i in c:
        if i in eng_lower_alphabet:
            mesto = eng_lower_alphabet.find(i)
            k_new = mesto + k
            if k_new <= (len(eng_lower_alphabet) - 1):
                c_shifr += eng_lower_alphabet[mesto+k]
            else:
                c_shifr += eng_lower_alphabet[mesto-(len(eng_lower_alphabet)-k)]
        elif i in eng_upper_alphabet:
            mesto = eng_upper_alphabet.find(i)
            k_new = mesto + k
            if k_new <= (len(eng_upper_alphabet) - 1):
                c_shifr += eng_upper_alphabet[mesto+k]
            else:
                c_shifr += eng_upper_alphabet[mesto-(len(eng_lower_alphabet)-k)]
        else:
            c_shifr += i
    return c_shifr

def shifr_ru(c,k):
    c_shifr = ''

    for i in c:
        if i in rus_lower_alphabet:
            mesto = rus_lower_alphabet.find(i)
            k_new = mesto + k
            if k_new <= (len(rus_lower_alphabet) - 1):
                c_shifr += rus_lower_alphabet[mesto+k]
            else:
                c_shifr += rus_lower_alphabet[mesto-(len(rus_lower_alphabet)-k)]
        elif i in rus_upper_alphabet:
            mesto = rus_upper_alphabet.find(i)
            k_new = mesto + k
            if k_new <= (len(rus_upper_alphabet) - 1):
                c_shifr += rus_upper_alphabet[mesto+k]
            else:
                c_shifr += rus_upper_alphabet[mesto-(len(rus_lower_alphabet)-k)]
        else:
            c_shifr += i
    return c_shifr

def deshifr_en(c,k):
    c_deshifr = ''

    for i in c:
        if i in eng_lower_alphabet:
            mesto = eng_lower_alphabet.find(i)
            k_new = mesto - k
            c_deshifr += eng_lower_alphabet[k_new]

        elif i in eng_upper_alphabet:
            mesto = eng_upper_alphabet.find(i)
            k_new = mesto - k
            c_deshifr += eng_upper_alphabet[k_new]
        else:
            c_deshifr += i
    return c_deshifr


def deshifr_ru(c, k):
    c_deshifr = ''

    for i in c:
        if i in rus_lower_alphabet:
            mesto = rus_lower_alphabet.find(i)
            k_new = mesto - k
            c_deshifr += rus_lower_alphabet[k_new]

        elif i in rus_upper_alphabet:
            mesto = rus_upper_alphabet.find(i)
            k_new = mesto - k
            c_deshifr += rus_upper_alphabet[k_new]
        else:
            c_deshifr += i
    return c_deshifr

language = input('Введите язык, ru or eng ')
while True:
    if language.lower() != 'en' and language.lower()!= 'ru':
        language = input('Введите КОРРЕКТНО язык, ru or eng ')
    break
vid = input('Введите S - shifr, D- deshifr ')
c = input('Введите фразу для шифрования ')
k = int(input('Введите шаг '))


if vid.lower() == 's':
    if language.lower() == 'ru':
        print(shifr_ru(c,k))
    elif language.lower() == 'en':
        print(shifr_en(c,k))
if vid.lower() == 'd':
    if language.lower() == 'ru':
        print(deshifr_ru(c,k))
    elif language.lower() == 'en':
        print(deshifr_en(c,k))

def deshifr(c):
    pass