eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def shifr_len(fraza):
    got_fraza = ''
    for c in fraza:
        lenght = 0
        for k in c:
            if k.isalpha() == True:
                lenght += 1
        for l in c:
            if l.isalpha() == True:
                if l in eng_lower_alphabet:
                    mesto = eng_lower_alphabet.find(l)
                    mesto_new = mesto + lenght
                    if mesto_new <= (len(eng_lower_alphabet) - 1):
                        got_fraza += eng_lower_alphabet[mesto + lenght]
                    else:
                        got_fraza += eng_lower_alphabet[mesto - (len(eng_lower_alphabet) - lenght)]


                else:
                    mesto = eng_upper_alphabet.find(l)
                    mesto_new = mesto + lenght
                    if mesto_new <= (len(eng_upper_alphabet) - 1):
                        got_fraza += eng_upper_alphabet[mesto + lenght]
                    else:
                        got_fraza += eng_upper_alphabet[mesto - (len(eng_upper_alphabet) - lenght)]


            else:
                got_fraza += l
        got_fraza += ' '
    return got_fraza


c = input().split()

print(shifr_len(c))



c = input('Введите фразу для шифрования ').split()





