import random
from choice import (time, form, pronoun)
from simple import (rule_one)


dictionary = {}


class InvalidCommand(Exception):
    # создаем новый объект типа эксепшен
    # Чтобы описать собственный тип исключения, нужно создать новый класс, унаследованный от базового типа Exception.
    # Это позволит запускать особые виды исключений в ситуациях, когда поведение пользователя не соответствует
    # алгоритму программы. В конструкторе Exception указываем текст исключения. После того, как оно сработало и было
    # перехвачено, можно его получить с помощью str.
    pass  # Оператор-заглушка, равноценный отсутствию операции.


def file_open():
    try:
        with open('sheetEn.txt', 'r') as file:  # открываем файл
            for num, line in enumerate(file, 1):  # берем строку, определяем ее номер(с 1) и значение в ней
                if num >= 1 and len(line) > 10:  # Если номер больше или = 0, то
                        create_dictionary(line, dictionary)  # запускаем словарь
            if dictionary == {}:  # если словарь пустой, то ...
                print('Недостаточно данных в файле, создайте новый словарь!')
                set_save(dictionary)  # вызываем функцию ввода данных
            return dictionary
    except OSError:  # если не получилось открыть файл
        print("Файл не открылся, создайте новый словарь!", 31)
        set_save(dictionary)  # вызываем функцию ввода данных


def create_dictionary(line, dictionary):
    try:  # побольше почитать об исключениях и как их обходить!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!????
        blockdata = {}
        inkey = 1
        verbs, translationX = line.split(" - ")  # делим строку на слова и их перевод
        verb = verbs.split(", ")  # слова делим между собой на раздельные
        V1 = verb[0]
        if V1 in dictionary.keys():  # dictionary.setdefault(keyname, value)
            print('Данное слово уже существует, заменить его значения на новые?')
            choice = input('Yes?')
            if choice != '':
                return dictionary
        for i in verb[1:]:
            inkey += 1
            num = str(inkey)
            blockdata['V'+num] = i
        translation = translationX.replace("\n", '')
        blockdata['tr'] = translation
        dictionary.setdefault(V1, blockdata)
    except:
        print('Ошибка чтения слова в словаре, строка:')  # переделать на нормальную ошибку!!!!!!!!!!!!!!!!!!????

# ------------------------------------------------------------
def set_save(dictionary):
    if dictionary == {}:  # если словарь пустой - значит не прочитали файл, создаем новый файл удаляя старый
        print('Словарь пустой!')
    while True:
        print("Введите: глагол, глагол во второй форме(если есть) - перевод")
        line = input()
        if line == '':
            break
        create_dictionary(line, dictionary)
    set_print(dictionary)
    return dictionary


def set_delete(dictionary):
    print('Введите слово которое требуется удалить или нажмите Enter для выхода')
    while True:
        set_print(dictionary)
        key = input(':')
        if key == '':
            break
        else:
            if key in dictionary:
                print('Слово: ', key, dictionary[key])
                dictionary.pop(key)
                continue
            else:
                print("Ошибка ввода слова!")
        return dictionary
    save_dict(dictionary)  # записываем в файл новый словарь
    return dictionary


def set_print(dictionary):
    print('Словарь:')
    number = 0
    for n in dictionary:
        line = outdict(n, dictionary)
        number += 1
        print(str(number) + ':', line)
    print()
    print('Колличество слов в словаре:', number)
    print()
    return dictionary
# line = lineV12.ljust(13, ' ') + '- ' + linetr  # прижимает влево и заполняет пустоту
# ------------------------------------------------------------

def set_choice(dictionary):
    dd = 0
    while True:
        ti = random.choice(list(time))
        frm = random.choice(list(form))
        pr = random.choice(list(pronoun))
        ver = random.choice(list(dictionary.keys()))  # сделать автоматическое определение длины
        print('Задание: Составьте преложение {} {}, используя:'.format(time[ti], form[frm]), '"', pronoun[pr], '+', ver, '"')
        print('press ENTER for continue or End for exit..')
        cmd = input('')
        cmd = cmd.upper()  # Make all the letters BIG
        if cmd == 'END':
            break
        print('Ответ: ', end='')
        rule_one(ti, frm, pr, ver, dictionary)
        dd += 1
        print('# ', dd)
        input()



def save_dict(dictionary):
    with open('sheetEn - копия.txt', 'w') as file:  # открываем файл
        for n in dictionary:
            line = outdict(n, dictionary)
            file.write(line + '\n')
    return


def outdict(n, dictionary):
    blockdata = dictionary[n]
    lineV1 = n
    linetr = blockdata['tr']
    lineV2 = ''
    if 'V2' in blockdata.keys():
        lineV2 = ', ' + blockdata['V2']
    lineV12 = lineV1 + lineV2
    line = lineV12 + '- ' + linetr  # прижимает влево и заполняет пустоту
    return line


AVAILABLE_COMMANDS = {  # Хранилище всех доступных обработчиков
    'SAVE': set_save,
    'DELETE': set_delete,
    'PRINT': set_print
}
ANOTHER_COMMANDS = {'END', ''}
# Множество значений для выхода
# Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
