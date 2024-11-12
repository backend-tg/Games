import pygame
import random
import time

# Инициализируем Pygame
pygame.init()

# Настраиваем отображение
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Matching Game")
font = pygame.font.Font(None, 74)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройки карты
CARD_SIZE = 100
MARGIN = 20

# Создание позиций карт
def create_card_positions():
    positions = []
    for i in range(4):
        for j in range(4):
            x = MARGIN + j * (CARD_SIZE + MARGIN)
            y = MARGIN + i * (CARD_SIZE + MARGIN)
            positions.append((x, y))
    return positions

positions = create_card_positions()

# Генерируем пары
def generate_pairs():
    symbols = list(range(8)) * 2
    random.shuffle(symbols)
    return symbols

pairs = generate_pairs()

# Класс карты
class Card:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], CARD_SIZE, CARD_SIZE)
        self.revealed = False
        self.matched = False

    def draw(self, screen):
        if self.revealed or self.matched:
            pygame.draw.rect(screen, WHITE, self.rect)
            font = pygame.font.Font(None, 74)
            text = font.render(str(self.symbol), True, BLACK)
            screen.blit(text, (self.position[0] + 35, self.position[1] + 25))
        else:
            pygame.draw.rect(screen, GREEN, self.rect)

# Создание объектов карты
cards = [Card(pairs[i], positions[i]) for i in range(16)]

# Игровые переменные
first_card = None
second_card = None
matches = 0
attempts = 0
running = True
clock = pygame.time.Clock()

# Показать все карточки в начале
screen.fill(BLACK)
for card in cards:
    card.revealed = True
    card.draw(screen)
screen.blit(font.render("Запомните пары ", True, WHITE), (10, 500))
pygame.display.flip()

# Подождите 10 секунд
time.sleep(10)

# Скрыть все карты после первого раскрытия
for card in cards:
    card.revealed = False

# Игровой цикл
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if first_card is None or (first_card and second_card is None):
                for card in cards:
                    if card.rect.collidepoint(event.pos) and not card.revealed and not card.matched:
                        card.revealed = True
                        if first_card is None:
                            first_card = card
                        elif second_card is None:
                            second_card = card
                            attempts += 1

    # Проверяем совпадение
    if first_card and second_card:
        pygame.time.wait(500)
        if first_card.symbol == second_card.symbol:
            first_card.matched = True
            second_card.matched = True
            first_card = None
            second_card = None
            matches += 1
        else:
            first_card.revealed = False
            second_card.revealed = False
            first_card = None
            second_card = None

    # Вытягивать карты
    for card in cards:
        card.draw(screen)

    # Отображение количества совпадений
    font = pygame.font.Font(None, 36)
    text = font.render(f"Совпадений: {matches}  Попытки: {attempts}", True, WHITE)
    screen.blit(text, (10, 500))

    # Проверяем победу
    if matches == 8:
        font = pygame.font.Font(None, 74)
        win_text = font.render("Ты выиграл!", True, RED)
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()