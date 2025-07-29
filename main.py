import random
import pygame

pygame.init()
game_status = "base_menu" # game, failed
record = 0
title = "Змейка"
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h 
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
font = pygame.font.SysFont(None, 36)


def base_menu():
    """
    создает экран начального меню, будет вызываться в начале и если игрок захочет выйти в главное меню
    return: bool -> 1 если мышка на кнопке старта, 0 если нет
    """
    # покрасил в темно синий
    screen.fill((22, 7, 163))
    # нахожу середину, кнопка будет занимать 10% экрана в длину и 5% в ширину
    width, height = 0.1 * WIDTH, 0.1 * HEIGHT
    x, y = (WIDTH - width) // 2, (HEIGHT - height) // 2 
    color = (255, 0, 0)

    rect = pygame.Rect(x, y, width, height)
    mouse_pos = pygame.mouse.get_pos()
    if rect.collidepoint(mouse_pos):
        color = (0, 255, 0)
    else:
        color = (255, 0, 0)

    pygame.draw.rect(screen, color, rect)
    return rect.collidepoint(mouse_pos)


def game():
    """основной процесс игры"""
    screen.fill((0, 0, 0))


def main():
    global game_status
    # имя окна
    pygame.display.set_caption(title)
    

    # объект управления кадрами в секунду
    clock = pygame.time.Clock()

    startpressed = False
    run = True
    while run: 
        # для работы alt+f4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startpressed:
                    game_status = "game"

        screen.fill((0, 0, 0))
        if game_status == "base_menu":
            startpressed = base_menu()
        elif game_status == "game":
            game()
            

        # дебаг количества fps
        fps = clock.get_fps()
        fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))
        pygame.display.flip()
        clock.tick(240)


if __name__ == "__main__":
    main()