# Jogo caça ao tesouro usando Pygame

import pygame

from pygame.locals import *
# ('*' Serve para dizer que está importando constantes e os sub modulos)

from sys import exit
# Serve para fechar a janela 

pygame.init()
# Serve para inicializar todas as funções e variaveis

pygame.display.set_caption('JOGO')
# Serve para mudar o nome do jogo

import cores


def main():

   fonte = pygame.font.SysFont("Comic Sams MS", 30)

   tela = pygame.display.set_mode((1000, 800))
   pygame.display.set_caption( "Campo minado" )

   tela.fill(cores.marrom)

   while True:
   # Loop do jogo pois o jogo tem que atualizar  
      for event in pygame.event.get():
      # LOOP for ser ve para verificar se algum evento ocorreu 
         if event.type == QUIT:
            pygame.quit()
            exit()
            # comando para fechar o jogo
      pygame.display.update()
    # serve para atualizar a tela do jogo caso aja uma interação

#Pedro Join the Server







if __name__ == "__main__":
    main()