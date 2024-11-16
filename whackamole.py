import pygame

def draw_grid(screen):
    grid_color = (0, 0, 255)  # Dark blue grid lines
    for x in range(0, 640, 32):  # Loop through the window width
        pygame.draw.line(screen, grid_color, (x, 0), (x, 512))
    for y in range(0, 512, 32):  # Loop through the window height
        pygame.draw.line(screen, grid_color, (0, y), (640, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 512))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("light green")
        draw_grid(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
