import random
import pygame

CELL, COLS, ROWS = 20, 30, 20


def main():
    pygame.init()
    screen = pygame.display.set_mode((CELL * COLS, CELL * ROWS))
    clock = pygame.time.Clock()
    snake = [(COLS // 2, ROWS // 2)]
    direction = (1, 0)
    apple = (random.randrange(COLS), random.randrange(ROWS))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # TODO: styr ormen med piltangenterna

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)
        # TODO: växa när ormen äter äpplet, annars ta bort svansen
        snake.pop()

        screen.fill((20, 24, 32))
        pygame.draw.rect(screen, (220, 60, 60), (*[c * CELL for c in apple], CELL, CELL))
        for x, y in snake:
            pygame.draw.rect(screen, (80, 200, 120), (x * CELL, y * CELL, CELL, CELL))
        pygame.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()
