import pygame 
from manager import Manager
from globaldata import screen_width, screen_hight

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_hight))


def main():
    mgr = Manager(screen)
    mgr.process(screen)
    pygame.quit()
    print("Игра окончена")


if __name__ == "__main__":
    main()
