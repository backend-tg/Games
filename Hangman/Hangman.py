import random
import time

# Приветствие:
print("\nДобро пожаловать в игру 'Виселица'!\n")
name = input("Введите ваше имя: ")
print(f"Привет, {name}! Удачи!")
time.sleep(2)
print("Игра вот-вот начнётся!\nДавайте играть в 'Виселицу'!")
time.sleep(3)

# Параметры игры:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["январь", "граница", "изображение", "фильм", "обещание", "дети", "легкие", "кукла", "рифма", "ущерб", "растения"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# Цикл для повторной игры:
def play_loop():
    global play_game
    play_game = input("Хотите сыграть снова? в = да, н = нет \n")
    while play_game not in ["в", "н", "В", "Н"]:
        play_game = input("Хотите сыграть снова? в = да, н = нет \n")
    if play_game.lower() == "в":
        main()
    else:
        print("Спасибо за игру! Ждём вас снова!")
        exit()

# Основная логика игры:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input(f"Слово: {display}. Введите букву: \n").strip().lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Некорректный ввод. Попробуйте ещё раз.\n")
        hangman()
    elif guess in already_guessed:
        print("Вы уже пробовали эту букву. Попробуйте другую.\n")
    elif guess in word:
        already_guessed.append(guess)
        word_as_list = list(display)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
            word_as_list[index] = guess
        display = ''.join(word_as_list)
        print(display + "\n")
    else:
        count += 1
        print_hangman(count, limit)
        print(f"Ошибок осталось: {limit - count}\n")
    if display == word:
        print("Поздравляем! Вы угадали слово!")
        play_loop()
    elif count == limit:
        print("Вы проиграли. Слово было:", word)
        play_loop()
    else:
        hangman()

def print_hangman(count, limit):
    stages = [
        "   _____ \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "__|__\n",

        "   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "__|__\n",

        "   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "__|__\n",

        "   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |      \n"
        "  |      \n"
        "__|__\n",

        "   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\\ \n"
        "  |    / \\ \n"
        "__|__\n"
    ]
    print(stages[count - 1])

main()
hangman()
