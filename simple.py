from choice import (pronoun, time, form, question_words)
import random

def rule_one(ti, frm, pr, ver, dictionary):
    ansver = ''
    third_person_singular = {"He", "She", "It"}
    end_listS = ['s', 'ss', 'sh', 'ch', 'x', 'o']
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    # qw = question_words[qw] - дополнить правио составлением вопроса с использование вопросительного слова

    if time[ti] == "Future":  # время будущее
        if form[frm] == "Question":  # вопрос в будущем
            ansver = 'Will ' + pronoun[pr] + ' ' + ver + '?'  # Вперед ставим Will и знак ?
            # ansver2 = qw + 'will ' + pronoun[pr] + ' ' + ver + '?'
        elif form[frm] == "Positive":  # Утверждение в будущем
            ansver1 = pronoun[pr] + ' will ' + ver  # первый вариант ответа
            ansver2 = pronoun[pr] + "'ll " + ver  # сокращенный вариант ответа
            list_ansver = [ansver1, ansver2]  # создание листа с ответами
            ansver = random.choice(list_ansver)  # выбор случайный выбор ответа из предложенных
        elif form[frm] == "Negative":
            ansver1 = pronoun[pr] + ' will ' + 'not ' + ver
            ansver2 = pronoun[pr] + " won’t " + ver
            list_ansver = [ansver1, ansver2]  # создание листа с ответами
            ansver = random.choice(list_ansver)  # выбор случайный выбор ответа из предложенных

    elif time[ti] == "Present":
        if form[frm] == "Question":
            if pronoun[pr] in third_person_singular:  # = {"He", "She", "It"}
                V_help = 'Does '
            else:
                V_help = 'Do '
            ansver = V_help + pronoun[pr] + ' ' + ver + '?'
        elif form[frm] == "Positive":  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if pronoun[pr] in third_person_singular:  # = {"He", "She", "It"}
                if ver[-2:] in end_listS:
                    ver = ver + 'es'
                    # print("Если глагол оканчивается на -s, -ss, -sh, -ch, -x, -o, то к нему прибавляется окончание -es")
                elif ver[-1] in 'y':  # если глагол заканчивается на -у
                    if ver[-2] in vowels:  # если -у предшествует гласная, то..
                        ver = ver + 's'  # добавляем окончание -s, -y сохраняем
                    else:
                        ver = ver[:-1] + 'ies'  # если у предшествует согласная, то удаляем у и добавляем ies
                else:
                    ver = ver + 's'
                ansver = pronoun[pr] + ' ' + ver  # She / He / It + V + s (es)
            else:
                ansver = pronoun[pr] + ' ' + ver  # I / We / You / They + V
        elif form[frm] == "Negative":
            if pronoun[pr] in third_person_singular:
                V_help = " doesn't "
            else:
                V_help = " don't "
            ansver = pronoun[pr] + V_help + ver

    elif time[ti] == "Past":
        if form[frm] == "Question":
            ansver = 'Did ' + pronoun[pr] + ' ' + ver + '?'
        elif form[frm] == "Positive":  # прошлое утвердительное
                blockdata = dictionary[ver]  # достаем данные о ключе(слове)
                if 'V2' in blockdata.keys():  # проверяем наличие там ключа V2
                    v_ed = blockdata['V2']  # если находим то v_ed равно 2-й форме глагола
                else:
                    if ver[-1] == 'e':  # если -у предшествует гласная, то..
                        v_ed = ver + 'd'  # добавляем окончание -s, -y сохраняем
                    elif ver[-1] == 'y':  # если -у предшествует гласная, то..
                        v_ed = ver[:-1] + 'ied'  # добавляем окончание -s, -y сохраняем
                    else:
                        v_ed = ver + 'ed'  # или к окончанию глагола добавляется окончание ed
                ansver = pronoun[pr] + ' ' + v_ed  # наш ответ
        elif form[frm] == "Negative":  # прошлое отрицательное
            ansver1 = pronoun[pr] + ' did ' + "n't " + ver
            ansver2 = pronoun[pr] + ' did ' + 'not ' + ver
            list_ansver = [ansver1, ansver2]  # создание листа с ответами
            ansver = random.choice(list_ansver)  # выбор случайный выбор ответа из предложенных
    print(ansver)

