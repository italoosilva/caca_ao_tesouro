# Jogo caça ao tesouro usando Pygame

import pygame
import random
import cores


def main():
   pygame.init()

   fonte = pygame.font.SysFont("Comic Sams MS", 30)

   tela = pygame.display.set_mode(1000, 800)
   pygame.display.set_caption( "Campo minado" )

   tela.fill(cores.verde)

   pygame.display.update()









if __name__ == "__main__":
    main()