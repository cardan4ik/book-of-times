from book import (InvalidCommand, AVAILABLE_COMMANDS, ANOTHER_COMMANDS, file_open, set_choice, set_save, save_dict)


def run():
    dictionary = file_open()
    while True:  # Работаем пока есть флаг
        print("Save - for save a new word, print command, your new word and translation, then press enter")
        print("Delete - for delete a word print command, it word, then press enter")
        print("Print - for print all words, print command, then press enter")
        print("End - for exit print command, then press enter")
        print("or press ENTER for start..")
        print('Введите команду:')
        cmd = input()
        cmd = cmd.upper()  # Make all the letters BIG
        try:  # просим попробовать пройти условие создаем обходчик ошибок
            if cmd not in AVAILABLE_COMMANDS.keys() and cmd not in ANOTHER_COMMANDS:  # если нигде нет нашей команды то..
                raise InvalidCommand("Err Type command: {} this command is not available".format(cmd))  # запускаем собственный тип исключения
        except InvalidCommand as e:  # после запуска исключения переходим сюда и выполняем действия ниже
            print(e)
        if cmd == 'END':
            print("The program is stopped..")
            break
        elif cmd in AVAILABLE_COMMANDS.keys():
                handler = AVAILABLE_COMMANDS[cmd](dictionary)  # Достаем нужный обработчик из хранилища обработчиков
                dictionary = handler
        else:
            set_choice(dictionary)
    save_dict(dictionary)
# -------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":  # проверяем условия что данную программу запускаем напрямую
    run()  # обращаемся к функции run()
