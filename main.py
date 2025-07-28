import pygame
import random



def base_menu(last=-1):
    """
    создает экран начального меню, будет вызываться в начале и в момент проигрыша
    last:int - последний счет (по умолчанию -1, т.к. меньше 0 результат быть не может)
    """


def main():
    pygame.init()

    # имя окна
    title = "Змейка"
    pygame.display.set_caption(title)

    # узнать размер текущего дисплея
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h 

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    font = pygame.font.SysFont(None, 36)

    # объект управления кадрами в секунду
    clock = pygame.time.Clock()


    base_menu()
    run = True
    while run: 
        # для работы alt+f4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.fill((0, 0, 0))

        # дебаг количества fps
        fps = clock.get_fps()
        fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))

        pygame.display.flip()
        clock.tick(240)


if __name__ == "__main__":
    main()