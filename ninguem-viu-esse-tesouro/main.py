from fases import PrimeiraFase, SegundaFase, TerceiraFase
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

# menu de teclas
menu_de_teclas = Menu(pygame)
menu_de_teclas.adiciona_item('menu de ajuda com as teclas')
menu_de_teclas.adiciona_item('seta para cima ou seta para baixo: navega por menus / repete diálogos')
menu_de_teclas.adiciona_item('enter: seleciona opção do menu / avança em diálogos')
menu_de_teclas.adiciona_item('w, a, s, d: movimenta o personagem')
menu_de_teclas.adiciona_item('seta para esquerda ou seta para direita: navega pelos seus itens')
menu_de_teclas.adiciona_item('barra de espaço: interage com item selecionado com as setas')
menu_de_teclas.adiciona_item('r: rastreia robombas próximos')
menu_de_teclas.adiciona_item('tab: altera alvo que está na mira da arma, quando possível (precisa habilitar a arma)')
menu_de_teclas.adiciona_item('1: informações do personagem, seu nome e seu hp atual')
menu_de_teclas.adiciona_item('2: coordenadas atuais do personagem')
menu_de_teclas.adiciona_item('voltar para o menu principal')

# menu principal
dir_trilha_menu = 'sons/trilhas/menu_principal.mp3'
menu_principal = Menu(pygame, dir_trilha_menu)
menu_principal.adiciona_item('novo jogo')
menu_principal.adiciona_item('ajuda com as teclas')
menu_principal.adiciona_item('sair do jogo')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

edd = Personagem()
fase = 1

menu_principal_ativo = True
while (menu_principal_ativo == True):
    acao_menu = menu_principal.faz_acao(pygame)
    if (acao_menu == 'novo jogo'):
        som_enter = 'sons/efeitos/enter.wav'
        som = pygame.mixer.Sound(som_enter)
        som.play()
        pygame.mixer.music.stop()
        menu_principal_ativo = False
    elif (acao_menu == 'ajuda com as teclas'):
        som_enter = 'sons/efeitos/enter.wav'
        som = pygame.mixer.Sound(som_enter)
        som.play()
        acao_menu = ''
        while (True):
            acao_menu = menu_de_teclas.faz_acao(pygame)
            if (acao_menu == 'voltar para o menu principal'):
                som_esc = 'sons/efeitos/esc.wav'
                som = pygame.mixer.Sound(som_esc)
                som.play()
                break
        menu_principal.ponteiro = 0
        menu_de_teclas.ponteiro = 0
    elif (acao_menu == 'sair do jogo'):
        pygame.quit()
        sys.exit()

    if (menu_principal_ativo == False):
        fase_atual = PrimeiraFase()
        fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
        sobrevive = True
    while (menu_principal_ativo == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == KEYDOWN):
                if ((event.key == pygame.K_w) or (event.key == pygame.K_a) or (event.key == pygame.K_s) or (event.key == pygame.K_d)):
                    edd.navega_no_mapa(pygame, event.key, fase_atual.mapa_da_fase)
                    if (fase_atual.mapa_da_fase.verifica_bateria(pygame, edd)):
                        edd.pega_bateria()
                    if (fase >=3):
                        edd.procura_robombas(fase_atual.mapa_da_fase.robombas)
                        if (fase_atual.mapa_da_fase.verifica_municao(pygame, edd)):
                            edd.pega_municao_e_recarrega(pygame)
                    edd.localiza_porta(fase_atual.mapa_da_fase)
                    fase_atual.mapa_da_fase.verifica_armadilha_robomba(pygame, edd)
                    edd.radar_robombas(pygame, fase_atual.mapa_da_fase.robombas)
                    if (edd.sobrevive() == False):
                        dir_trilha_menu = 'sons/trilhas/menu_derrota.mp3'
                        menu_derrota = Menu(pygame, dir_trilha_menu)
                        menu_derrota.adiciona_item('reiniciar fase')
                        menu_derrota.adiciona_item('sair do jogo')
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play(-1)
                        acao_menu = menu_derrota.faz_acao(pygame)
                        if (acao_menu == 'reiniciar fase'):
                            som_enter = 'sons/efeitos/enter.wav'
                            som = pygame.mixer.Sound(som_enter)
                            som.play()
                            pygame.mixer.music.stop()
                            if (fase == 1):
                                fase_atual = PrimeiraFase()
                                edd.revive()
                                fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                            elif (fase == 2):
                                fase_atual = SegundaFase()
                                edd.revive()
                                fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                            elif (fase == 3):
                                fase_atual = TerceiraFase()
                                edd.revive()
                                fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                        elif (acao_menu == 'sair do jogo'):
                            pygame.quit()
                            sys.exit()

                elif ((event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT)):
                    if (fase >= 3):
                        edd.altera_item()
                    edd.mostra_informacoes_do_item_atual()

                elif (event.key == pygame.K_SPACE):
                    if (edd.item_atual == 0):
                        edd.insere_bateria_na_porta(pygame, fase_atual.mapa_da_fase)
                    elif (edd.item_atual == 1):
                        edd.aperta_gatilho(pygame, fase_atual.mapa_da_fase)

                elif (event.key == pygame.K_RETURN):
                    edd.abre_porta(pygame, fase_atual.mapa_da_fase)
                    if (fase_atual.mapa_da_fase.porta_de_saida.trancada == False):
                        fase_atual.dialogos.mostra_dialogos_finais(pygame)
                        dir_trilha_menu = 'sons/trilhas/menu_vitoria.mp3'
                        menu_vitoria = Menu(pygame, dir_trilha_menu)
                        menu_vitoria.adiciona_item('ir para a próxima fase')
                        menu_vitoria.adiciona_item('sair do jogo')
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play(-1)
                        acao_menu = menu_vitoria.faz_acao(pygame)
                        if (acao_menu == 'ir para a próxima fase'):
                            pygame.mixer.music.stop()
                            if (fase == 1):
                                fase += 1
                                fase_atual = SegundaFase()
                                edd.revive()
                                fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                            elif (fase == 2):
                                fase += 1
                                fase_atual = TerceiraFase()
                                edd.revive()
                                fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                        elif (acao_menu == 'sair do jogo'):
                            pygame.quit()
                            sys.exit()

                elif (event.key == pygame.K_1):
                    edd.mostra_informacoes_do_personagem()

                elif (event.key == pygame.K_2):
                    edd.mostra_coordenadas_do_personagem()

                elif (event.key == pygame.K_r):
                    edd.rastreia_robombas(pygame, fase_atual.mapa_da_fase.robombas)

                elif (event.key == pygame.K_TAB):
                    if (edd.item_atual == 1):
                        edd.altera_alvo()

