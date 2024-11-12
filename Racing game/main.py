import pygame
import random

# Инициализируем Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 100
ROAD_WIDTH = 400
FPS = 30  # Частота кадров

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Загрузка изображений
car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))

# Настраиваем отображение
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Race Game")

# Шрифт
font = pygame.font.Font(None, 36)


# Класс автомобиля
class Car:
    def __init__(self):
        self.image = car_img
        self.x = (SCREEN_WIDTH - CAR_WIDTH) // 2
        self.y = SCREEN_HEIGHT - CAR_HEIGHT - 10
        self.speed = 5

    def move_left(self):
        if self.x > (SCREEN_WIDTH - ROAD_WIDTH) // 2:
            self.x -= self.speed

    def move_right(self):
        if self.x < (SCREEN_WIDTH + ROAD_WIDTH) // 2 - CAR_WIDTH:
            self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# Класс препятствий
class Obstacle:
    def __init__(self):
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.x = random.randint(
            (SCREEN_WIDTH - ROAD_WIDTH) // 2,
            (SCREEN_WIDTH + ROAD_WIDTH) // 2 - CAR_WIDTH,
        )
        self.y = -self.height
        self.speed = 5

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

    def check_collision(self, car):
        if self.y + self.height > car.y and self.y < car.y + CAR_HEIGHT:
            if self.x + self.width > car.x and self.x < car.x + CAR_WIDTH:
                return True
        return False


# Игровой цикл
def game_loop():
    car = Car()
    obstacles = []
    score = 0
    clock = pygame.time.Clock()
    running = True
    start_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.move_left()
        if keys[pygame.K_RIGHT]:
            car.move_right()

        if random.randint(1, 30) == 1:
            obstacles.append(Obstacle())

        screen.fill(GRAY)
        pygame.draw.rect(
            screen,
            BLACK,
            ((SCREEN_WIDTH - ROAD_WIDTH) // 2, 0, ROAD_WIDTH, SCREEN_HEIGHT),
        )

        car.draw(screen)

        for obstacle in obstacles[:]:
            obstacle.move()
            obstacle.draw(screen)
            if obstacle.is_off_screen():
                obstacles.remove(obstacle)
                score += 1
            if obstacle.check_collision(car):
                running = False

        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)
    final_score_text = font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

    # Рассчитать и отобразить время игры
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # in seconds
    time_text = font.render(f"Time: {elapsed_time} seconds", True, WHITE)
    screen.blit(time_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    pygame.time.wait(5000)

    pygame.quit()

    pygame.quit()


if __name__ == "__main__":
    game_loop()
