from gameLogic import makeMove, chooseWord, setTries, showWord, record_update

print("Добрый вечер! Здравствуйте, уважаемые дамы и господа! Пятница! В эфире капитал-шоу «Поле чудес»!")
print('В игре есть 3 уровня сложности:')
print("EASY - 7 попыток угадать букву/слово")
print("MEDIUM - 5 попыток угадать букву/слово")
print("HARD - 3 попытки угадать букву/слово")

local_record = 0
try:
    while True:
        difficulty = input("Выберите уровень сложности игры - hard, medium, easy: ")
        tries = setTries(difficulty)
        word_hidden, progress = chooseWord()
        while tries > 0 and progress != word_hidden:
            showWord(progress, tries)
            progress, tries = makeMove(progress, tries, word_hidden)
            if progress == word_hidden:
                local_record += 1
            if tries == 0:
                print("У вас закончились попытки. Игра окончена.")


        record_update(local_record)
        print("Хотите сыграть еще раз? (да/нет)")
        a = input().lower()
        if a == "нет":
            print(f"Вы угадали {local_record} слов(-а)")
            break

except Exception:
    print("Непредвиденная ошибка. Перезапустите игру.")





