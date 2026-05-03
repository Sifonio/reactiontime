import random
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    running_timer = True

    W, H = (800,600)

    RED = (255, 50, 50)
    GREEN = (50, 255, 50)
    WHITE = (255, 255, 255)
    BLACK = (30, 30, 30)
    GRIS = (60, 60, 60)

    flags = pygame.DOUBLEBUF | pygame.HWSURFACE

    screen = pygame.display.set_mode((W, H), flags, vsync = 0)

    font = pygame.font.SysFont("Arial", 48)

    pygame.display.set_caption("Reaction test")
    pygame.display.flip()

    run = True
    state = 0

    start_time = 0
    result_time = 0
    appearance_time = 0

    while run:
        now = pygame.time.get_ticks()
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if state == 0:
                    state = 1
                    time_to_wait = random.randint(2000, 3000)
                    appearance_time = pygame.time.get_ticks() + time_to_wait
                elif state == 1:
                    state = 3
                elif state == 2:
                    result_time = now - start_time
                    state = 4
                elif state == 3 or state == 4:
                    state = 0

            if e.type == pygame.QUIT:
                run = False

        if state == 0:
            screen.fill((0,0,255))
            text = font.render("Click to start", True, WHITE)

        if state == 1:
            screen.fill(RED)
            text = font.render("Wait", True, WHITE)

        if state == 1 and now >= appearance_time:
            state = 2
            start_time = pygame.time.get_ticks()

        if state == 2:
            screen.fill(GREEN)
            text = font.render("Click!", True, WHITE)

        if state == 3:
            screen.fill(GRIS)
            text = font.render("Too early!!!", True, WHITE)

        if state == 4:
            screen.fill(GRIS)
            text = font.render(f"Reaction time: {result_time} ms", True, WHITE)

        text_rect = text.get_rect(center=(W // 2, H // 2))
        screen.blit(text, text_rect)


        pygame.display.flip()

    pygame.quit()



