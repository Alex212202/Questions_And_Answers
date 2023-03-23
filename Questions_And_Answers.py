questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
print("Привет! Предлагаю проверить свои знания английского! Наберите 'ready', чтобы начать")
correct_count = 0
incorrect_count = 0
ready = input()
if ready == "ready":
    print(questions[0])
    firstAnswer = input()
    if firstAnswer == answers[0]:
        correct_count += 1
        wright1 = "Ответ верный!"
        print(wright1)
    else:
        incorrect_count += 1
        print(f"Неправильно! Правильный ответ: {answers[0]}")
    print(questions[1])
    secondAnswer = input()
    if secondAnswer == answers[1]:
        correct_count += 1
        wright2 = "Ответ верный"
        print(wright2)
    else:
        incorrect_count += 1
        print(f"Неправильно! Правильный ответ: {answers[1]}")
    print(questions[2])
    thirdAnswer = input()
    if thirdAnswer == answers[2]:
        correct_count += 1
        wright3 = str("Ответ верный")
        print(wright3)
    else:
        incorrect_count += 3
        print(f"Неправильно! Правильный ответ: {answers[2]}")

    percent_count = round(correct_count/len(questions)*100)
    print(f"Вот и все! Вы ответили на {len(questions)} вопросов из {correct_count} верно, это {percent_count} процентa(ов).")
else:
    print("Кажется вы не хотите играть! Очень жаль.")
