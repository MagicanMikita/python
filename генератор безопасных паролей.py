import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

danet = ['да', 'нет']

ans_dig = input('Включить ли в пароль цифры? Принимается ответ "Да" или "Нет" в любом регистре ')
while ans_dig.lower() not in danet:
    print('Принимается только да или нет, попробуй ещё раз')
    ans_dig = input('Включить ли в пароль цифры? Принимается ответ "Да" или "Нет" в любом регистре ')

ans_low = input('Включить ли в пароль буквы в нижнем регистре? Принимается ответ "Да" или "Нет" в любом регистре ')
while ans_low.lower() not in danet:
    print('Принимается только да или нет, попробуй ещё раз')
    ans_low = input('Включить ли в пароль буквы в нижнем регистре? Принимается ответ "Да" или "Нет" в любом регистре ')

ans_upp = input('Включить ли в пароль буквы в верхнем регистре? Принимается ответ "Да" или "Нет" в любом регистре ')
while ans_upp.lower() not in danet:
    print('Принимается только да или нет, попробуй ещё раз')
    ans_upp = input('Включить ли в пароль буквы в верхнем регистре? Принимается ответ "Да" или "Нет" в любом регистре ')

ans_punc = input('Включить ли в пароль пунктуацию? Принимается ответ "Да" или "Нет" в любом регистре ')
while ans_punc.lower() not in danet:
    print('Принимается только да или нет, попробуй ещё раз')
    ans_punc = input('Включить ли в пароль пунктуацию? Принимается ответ "Да" или "Нет" в любом регистре ')

ans_l0 = input('Включить ли в пароль неоднозначные символы "lOo0"? Принимается ответ "Да" или "Нет" в любом регистре ')
while ans_l0.lower() not in danet:
    print('Принимается только да или нет, попробуй ещё раз')
    ans_l0 = input('Включить ли в пароль неоднозначные символы "lOo0"? Принимается ответ "Да" или "Нет" в любом регистре ')


ans_colvo = input('Сколько паролей необходимо сгенерировать? ')
while ans_colvo.isdigit() == False:
    print('Допускаются только числа')
    ans_colvo = input('Сколько паролей необходимо сгенерировать? ')
ans_colvo = int(ans_colvo)

ans_len = input('Какой должна быть длина пароля? ')
while ans_len.isdigit() == False:
    print('Допускаются только числа')
    ans_len = int(input('Какой должна быть длина пароля? '))
ans_len = int(ans_len)










if ans_dig == 'да':
        chars += digits
if ans_low == 'да':
        chars += lowercase_letters
if ans_upp == 'да':
        chars += uppercase_letters
if ans_punc== 'да':
        chars += punctuation
if ans_l0 == 'нет':
    for c in '0Ool':
        chars = chars.replace(c, '')

passw = ''
for i in range(ans_colvo):
    for j in range(ans_len):
        passw += random.choice(chars)
    print(passw)
    passw = ''






