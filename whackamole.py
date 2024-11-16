import pygame
import random

def draw_grid(screen):
    grid_color = (0, 0, 255)
    for x in range(0, 640, 32):
        pygame.draw.line(screen, grid_color, (x, 0), (x, 512))
    for y in range(0, 512, 32):
        pygame.draw.line(screen, grid_color, (0, y), (640, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 512))
    clock = pygame.time.Clock()

    # Load mole image
    mole_image = pygame.image.load("mole.png")

    # Initial mole position
    mole_x, mole_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if mole was clicked (within the 32x32 grid)
                if mole_x <= event.pos[0] < mole_x + 32 and mole_y <= event.pos[1] < mole_y + 32:
                    # Move mole to a random square
                    mole_x = random.randrange(0, 640, 32)
                    mole_y = random.randrange(0, 512, 32)

        screen.fill("light green")
        draw_grid(screen)
        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))  # Mole position
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
