from colorama import init
from colorama import Fore, Back, Style
init()  # Инициализация библиотеки colorama для работы с цветами в консоли

from random import choice  # Импортируем функцию для случайного выбора слова


# Функция для вывода текущего состояния слова и проверки попытки игрока
def print_word(ans: str) -> callable:
    # Подготовка начального состояния сетки игры
    list_of_words = [
        "  │   │   │   │   │   │",
        "  │   │   │   │   │   │",
        "  │   │   │   │   │   │",
        "  │   │   │   │   │   │",
        "  │   │   │   │   │   │",
        "  │   │   │   │   │   │",
    ]
    color = [
        [Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET],
        [Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET],
        [Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET],
        [Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET],
        [Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET],
        [Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET],
    ]
    answer = "  │   │   │   │   │   │"
    try_number = 0

    # Вложенная функция для проверки буквы в попытке и вывода текущего состояния
    def inner_print_word(trying: str) -> str:
        nonlocal try_number
        nonlocal ans
        nonlocal answer

        # Проверяем каждую букву в попытке и окрашиваем в зависимости от совпадений
        for i in range(5):
            if trying[i] in ans and i in find(ans, trying[i]):
                color[try_number][i] = Fore.RED
            elif trying[i] in ans:
                color[try_number][i] = Fore.YELLOW

        # Обновляем строку текущей попытки с учетом цвета букв
        list_of_words[try_number] = (
            f"  │ {color[try_number][0]}{trying[0]}{Fore.RESET} │ {color[try_number][1]}{trying[1]}{Fore.RESET} │ {color[try_number][2]}{trying[2]}{Fore.RESET} │ {color[try_number][3]}{trying[3]}{Fore.RESET} │ {color[try_number][4]}{trying[4]}{Fore.RESET} │"
        )

        try_number += 1
        # Отображаем текущее состояние сетки
        print("  ┌───┬───┬───┬───┬───┐")
        for try_ in list_of_words:
            print(try_)
            print("  ├───┼───┼───┼───┼───┤")
        if trying == ans or try_number == 6:
            answer = f"  │{Fore.RED}{Back.LIGHTYELLOW_EX}{Style.BRIGHT} {ans[0]} {Style.RESET_ALL}│{Fore.RED}{Back.LIGHTYELLOW_EX}{Style.BRIGHT} {ans[1]} {Style.RESET_ALL}│{Fore.RED}{Back.LIGHTYELLOW_EX}{Style.BRIGHT} {ans[2]} {Style.RESET_ALL}│{Fore.RED}{Back.LIGHTYELLOW_EX}{Style.BRIGHT} {ans[3]} {Style.RESET_ALL}│{Fore.RED}{Back.LIGHTYELLOW_EX}{Style.BRIGHT} {ans[4]} {Style.RESET_ALL}│"
        print(answer)
        print("  └───┴───┴───┴───┴───┘")

        if trying == ans:
            return "winner"
        if try_number == 6:
            return "looser"
        return ""

    return inner_print_word


# Функция для отображения алфавита с подсветкой использованных букв
def print_alphabet(answer: str) -> callable:
    # Подготовка словаря для букв алфавита с цветами
    alphabet = {
        "А": Fore.RESET,
        "Б": Fore.RESET,
        "В": Fore.RESET,
        "Г": Fore.RESET,
        "Д": Fore.RESET,
        "Е": Fore.RESET,
        "Ж": Fore.RESET,
        "З": Fore.RESET,
        "И": Fore.RESET,
        "Й": Fore.RESET,
        "К": Fore.RESET,
        "Л": Fore.RESET,
        "М": Fore.RESET,
        "Н": Fore.RESET,
        "О": Fore.RESET,
        "П": Fore.RESET,
        "Р": Fore.RESET,
        "С": Fore.RESET,
        "Т": Fore.RESET,
        "У": Fore.RESET,
        "Ф": Fore.RESET,
        "Х": Fore.RESET,
        "Ц": Fore.RESET,
        "Ч": Fore.RESET,
        "Ш": Fore.RESET,
        "Щ": Fore.RESET,
        "Ъ": Fore.RESET,
        "Ы": Fore.RESET,
        "Ь": Fore.RESET,
        "Э": Fore.RESET,
        "Ю": Fore.RESET,
        "Я": Fore.RESET,
    }
    for key in alphabet:
        alphabet[key] = Fore.RESET

    # Вложенная функция для обновления цвета букв в алфавите
    def inner_print_alphabet(my_word) -> None:
        nonlocal alphabet
        nonlocal answer
        count = -1
        for letter in my_word:
            if letter in answer:
                alphabet[letter] = Fore.RED
            else:
                alphabet[letter] = Fore.LIGHTBLACK_EX

        # Отображаем алфавит с текущими подсветками
        for letter in alphabet:
            count += 1
            if count % 8 == 0:
                print("")
            print(f" {alphabet[letter]}{letter}", end=" ")

    return inner_print_alphabet


# Функция для поиска всех позиций буквы в слове
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


# Основная игровая логика
stop_game = "1"
with open("words.txt", encoding="UTF8") as file_words:
    all_words = file_words.read().split("\n")

# Выводим правила игры и сетку для визуализации
print(
    f"\n\n\n{Fore.RED}...{Style.RESET_ALL}................---------====  {Style.BRIGHT}{Fore.RED}W {Fore.YELLOW}O {Fore.BLUE}R {Fore.GREEN}D {Fore.RED}L {Fore.BLUE}E{Style.RESET_ALL} ====---------................{Fore.RED}...{Style.RESET_ALL}\n"
)
print("Правила:")
print(
    f"1. {Fore.RED}Отгадай слово {Style.RESET_ALL}из пяти букв русского языка - существительное в единственном числе."
)
print(f"2. Просто введи в консоли слово и нажми {Fore.YELLOW}Enter{Style.RESET_ALL}.")
print(
    f"3. Если угадал с {Fore.BLUE}первого раза, {Style.RESET_ALL}ты молодец, сходи купи лотерейный билет."
)
print(
    f"4. Если какая-нибудь буква в твоём слове есть и в загаданном слове, то она меняет \nцвет на {Fore.RED}{Style.BRIGHT}КРАСНЫЙ{Style.RESET_ALL}, если совпали и позиции букв, и {Fore.YELLOW}{Style.BRIGHT}ЖЕЛТЫЙ{Style.RESET_ALL} - если позиции не совпали."
)
print(
    f"5. Для удобства нарисован алфавит, где уже использованные буквы подкрашиваются {Fore.LIGHTBLACK_EX}СЕРЕНЬКИМ{Style.RESET_ALL}."
)
print(
    f"6. Буквы {Fore.YELLOW}Ё{Fore.RESET} у нас нет, вместо нее - буква {Fore.GREEN}Е{Fore.RESET}"
)
print(f"7. У тебя только {Fore.BLUE}шесть {Style.RESET_ALL}попыток!\n")
print(
    """┌───┬───┬───┬───┬───┐
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
└───┴───┴───┴───┴───┘"""
)

# Основной игровой цикл
while stop_game == "1":
    answer = choice(all_words).upper()  # Загаданное слово
    game = print_word(answer)
    keyboard = print_alphabet(answer)
    keyboard("     ")

    for _ in range(6):  # Игроку дается шесть попыток
        while True:
            trying = input(f"{Style.RESET_ALL}Вводи слово!  ").upper()
            if trying.lower() in all_words:
                break
            if len(trying) != 5:
                print("Слово должно быть из 5 букв?")
            else:
                print("Попробуй другое слово")
        result = game(trying)
        keyboard(trying)
        if result == "winner":
            print(f"\n {Fore.RED}АЙ МАЛАЦА!!!{Style.RESET_ALL}")
            break
        if result == "looser":
            print(f"\n {Fore.YELLOW}НУ Ё-МАЁ, НУ ВАЩЕЕЕЕ!!!{Style.RESET_ALL}")
            break
    if (
        input(
            f"Ещё разок? 1 - {Fore.RED}Давай!{Style.RESET_ALL}, эни эназа чар - {Fore.YELLOW}Нееее...{Style.RESET_ALL}"
        )
        != "1"
    ):
        stop_game = 0
