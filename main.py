import pygame 
from manager import *
from globaldata import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock() 


def main():
    mgr = Manager()
    mgr.process(screen)
    pygame.quit()
    print("OK")


if __name__ == "__main__":
    main()