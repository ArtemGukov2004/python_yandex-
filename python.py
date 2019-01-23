def decode_from_morse(code):
    errors = []
    indexes_errors = []
    normal_text = ''
    for elem in range(len(code)):
        flag = False
        for letter in MorseCode:
            if MorseCode[letter] == code[elem] or MorseCode[letter] + '#' == code[elem]:
                if code[elem][-1] == '#':
                    letter_lower = letter.lower()
                    normal_text += letter_lower
                else:
                    normal_text += letter
                flag = True
        if flag is False:
            errors.append(code[elem])
            indexes_errors.append(str(elem + 1))
    if len(normal_text) > 0:
        print(normal_text)
    if len(errors) > 0:
        print('Данные элементы кода не декодируются.')
        print(' '.join(errors))
        print('Их номера в ряду.')
        print(' '.join(indexes_errors))


def encode_to_morse(text):
    errors = []
    indexes_errors = []
    morse_code = []
    for elem in range(len(text)):
        if text[elem] not in MorseCode:
            errors.append(main_text[elem])
            indexes_errors.append(str(elem + 1))
        else:
            morse_code.append(MorseCode[text[elem]])
    if len(morse_code) > 0:
        print(' '.join(morse_code))
    if len(errors) > 0:
        print('Данные элементы не кодируются.')
        print(' '.join(errors))
        print('Их номера в ряду.')
        print(' '.join(indexes_errors))


def main():
    global MorseCode
    print('Мы рады, что вы звхотели воспользоваться нашими услугами МорзаКод.')
    print('Хотите ли вы закодировать текст? Ответьте да или нет.')
    while True:
        answer1 = input().lower()
        if len(answer1) == 0 or (answer1 != 'да' and answer1 != 'нет'):
            print('Простите, но вы ничего не написали, либо такого ответа нет.')
        else:
            break
    if answer1 == 'да':
        print('Введите ваш текст.')
        global main_text
        while True:
            main_text = input()
            text_copy = main_text.upper()
            if len(text_copy) == 0:
                print('Простите, но вы ничего не написали')
            else:
                break
        encode_to_morse(text_copy)
    print('Хотите ли декодировать текст? Ответьте да или нет.')
    while True:
        answer2 = input().lower()
        if len(answer2) == 0 or (answer2 != 'да' and answer2 != 'нет'):
            print('Простите, но вы ничего не написали, либо такого ответа нет.')
        else:
            break
    if answer2 == 'да':
        print('''Введите ваш код.(Если несколько элементов, пишите их через пробел.)
Если вы захотите поменять регистр буквы на нижний, в конце элемента напишите #''')
        while True:
            code = input()
            if len(code) == 0:
                print('Простите, но вы ничего не написали')
            else:
                break
        if ' ' in code:
            code = [i for i in code.split()]
        else:
            code = [code]
        decode_from_morse(code)
    print('Удачного вам дня!')


main()
