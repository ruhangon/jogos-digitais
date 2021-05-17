from fases import PrimeiraFase
from menu import Menu
from personagem import Personagem
from pygame.locals import *
import os
import pygame
import sys

pygame.init()

tela = pygame.display.set_mode([500, 500])

pygame.display.set_caption('Ninguém viu esse tesouro')

tela.fill((255, 255, 255))

dir_trilha_menu = 'sons/trilhas/menu_principal.mp3'
menu_principal = Menu(pygame, dir_trilha_menu)
menu_principal.adiciona_item('novo jogo')
menu_principal.adiciona_item('sair do jogo')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

fase = 1
edd = Personagem()

menu_principal_ativo = True
while (menu_principal_ativo):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if (event.type == KEYDOWN):
            acao = menu_principal.faz_acao(pygame, event.key)
            if (acao == 'novo jogo'):
                pygame.mixer.music.stop()
                menu_principal_ativo = False
                break
            elif (acao == 'sair do jogo'):
                pygame.quit()
                sys.exit()

    if (menu_principal_ativo == False):
        if (fase == 1):
            fase_atual = PrimeiraFase()
    while (menu_principal_ativo == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == KEYDOWN):
                if ((event.key == pygame.K_w) or (event.key == pygame.K_a) or (event.key == pygame.K_s) or (event.key == pygame.K_d)):
                    edd.navega_no_mapa(pygame, event.key, fase_atual.mapa_da_fase)
                elif (event.key == pygame.K_1):
                    edd.mostra_informacoes_do_personagem()
                elif (event.key == pygame.K_2):
                    edd.mostra_coordenadas_do_personagem()
