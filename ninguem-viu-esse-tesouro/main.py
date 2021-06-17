from fases import PrimeiraFase, SegundaFase, TerceiraFase, QuartaFase, QuintaFase
from menu import Menu
from personagem import Personagem
from pygame.locals import *
import os
import pygame
import sys

dir_principal = os.path.dirname(__file__)
dir_sons = os.path.join(dir_principal, 'data')

pygame.init()

tela = pygame.display.set_mode([500, 500])

pygame.display.set_caption('Ninguém viu esse tesouro')

tela.fill((255, 255, 255))

# menu de teclas
menu_de_teclas = Menu(pygame)
menu_de_teclas.adiciona_item('menu de ajuda com as teclas')
menu_de_teclas.adiciona_item('setas direcionais: navega por menus / repete diálogos / movimenta o personagem durante o jogo')
menu_de_teclas.adiciona_item('enter: seleciona opção do menu / avança em diálogos')
menu_de_teclas.adiciona_item('esc: pula diálogo da fase atual')
menu_de_teclas.adiciona_item('ctrl: navega pelos seus itens')
menu_de_teclas.adiciona_item('barra de espaço: interage com item selecionado com a tecla ctrl')
menu_de_teclas.adiciona_item('r: rastreia robombas próximos')
menu_de_teclas.adiciona_item('tab: altera alvo que está na mira da arma, quando possível (precisa habilitar a arma)')
menu_de_teclas.adiciona_item('1: informações do personagem, seu nome e seu hp atual')
menu_de_teclas.adiciona_item('2: coordenadas atuais do personagem')
menu_de_teclas.adiciona_item('voltar para o menu principal')

# menu de créditos
menu_de_creditos = Menu(pygame)
menu_de_creditos.adiciona_item('créditos')
menu_de_creditos.adiciona_item('Efeitos sonoros por Eric Matyas. Site: www.soundimage.org')
menu_de_creditos.adiciona_item('Música por Eric Matyas. Site: www.soundimage.org')
menu_de_creditos.adiciona_item('Desenvolvido por Ruhan Gonçalves')
menu_de_creditos.adiciona_item('voltar para o menu principal')

# menu principal
menu_principal = Menu(pygame, os.path.join(dir_sons, 'menu_principal.mp3'))
menu_principal.adiciona_item('novo jogo')
menu_principal.adiciona_item('ajuda com as teclas')
menu_principal.adiciona_item('créditos')
menu_principal.adiciona_item('sair do jogo')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

edd = Personagem()
fase = 1

menu_principal_ativo = True
while (menu_principal_ativo == True):
    acao_menu = menu_principal.faz_acao(pygame)
    if (acao_menu == 'novo jogo'):
        som = pygame.mixer.Sound(os.path.join(dir_sons, 'enter.wav'))
        som.play()
        pygame.mixer.music.stop()
        menu_principal_ativo = False
    elif (acao_menu == 'ajuda com as teclas'):
        som = pygame.mixer.Sound(os.path.join(dir_sons, 'enter.wav'))
        som.play()
        acao_menu = ''
        while (True):
            acao_menu = menu_de_teclas.faz_acao(pygame)
            if (acao_menu == 'voltar para o menu principal'):
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'esc.wav'))
                som.play()
                break
        menu_principal.ponteiro = 0
        menu_de_teclas.ponteiro = 0
    elif (acao_menu == 'créditos'):
        som = pygame.mixer.Sound(os.path.join(dir_sons, 'enter.wav'))
        som.play()
        acao_menu = ''
        while (True):
            acao_menu = menu_de_creditos.faz_acao(pygame)
            if (acao_menu == 'voltar para o menu principal'):
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'esc.wav'))
                som.play()
                break
        menu_principal.ponteiro = 0
        menu_de_creditos.ponteiro = 0
    elif (acao_menu == 'sair do jogo'):
        pygame.quit()
        sys.exit()

    if (menu_principal_ativo == False):
        fase = 1
        fase_atual = PrimeiraFase()
        fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
        sobrevive = True
    while (menu_principal_ativo == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == KEYDOWN):
                if ((event.key == pygame.K_UP) or (event.key == pygame.K_LEFT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_RIGHT)):
                    edd.navega_no_mapa(pygame, event.key, fase_atual.mapa_da_fase, os, dir_sons)
                    if (fase_atual.mapa_da_fase.verifica_bateria(pygame, edd, os, dir_sons)):
                        edd.pega_bateria()
                    if (fase >=3):
                        edd.procura_robombas(fase_atual.mapa_da_fase.robombas)
                        if (fase_atual.mapa_da_fase.verifica_municao(pygame, edd)):
                            edd.pega_municao_e_recarrega(pygame, os, dir_sons)
                    edd.localiza_porta(fase_atual.mapa_da_fase)
                    fase_atual.mapa_da_fase.verifica_armadilha_robomba(pygame, edd, os, dir_sons)
                    edd.radar_robombas(pygame, fase_atual.mapa_da_fase.robombas, os, dir_sons)
                    if (edd.sobrevive() == False):
                        menu_derrota = Menu(pygame, os.path.join(dir_sons, 'menu_derrota.mp3'))
                        menu_derrota.adiciona_item('reiniciar fase')
                        menu_derrota.adiciona_item('sair do jogo')
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play(-1)
                        acao_menu = menu_derrota.faz_acao(pygame)
                        if (acao_menu == 'reiniciar fase'):
                            som = pygame.mixer.Sound(os.path.join(dir_sons, 'enter.wav'))
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
                            elif (fase == 4):
                                fase_atual = QuartaFase()
                                edd.revive()
                                fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                            elif (fase == 5):
                                fase_atual = QuintaFase()
                                edd.revive()
                                fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                        elif (acao_menu == 'sair do jogo'):
                            pygame.quit()
                            sys.exit()

                elif (event.key == pygame.K_LCTRL):
                    if (fase >= 3):
                        edd.altera_item()
                    edd.mostra_informacoes_do_item_atual()

                elif (event.key == pygame.K_SPACE):
                    if (edd.item_atual == 0):
                        edd.insere_bateria_na_porta(pygame, fase_atual.mapa_da_fase, os, dir_sons)
                    elif (edd.item_atual == 1):
                        edd.aperta_gatilho(pygame, fase_atual.mapa_da_fase, os, dir_sons)

                elif (event.key == pygame.K_RETURN):
                    edd.abre_porta(pygame, fase_atual.mapa_da_fase, os, dir_sons)
                    if (fase_atual.mapa_da_fase.porta_de_saida.trancada == False):
                        if (fase <= 4):
                            fase_atual.dialogos.mostra_dialogos_finais(pygame)
                            menu_vitoria = Menu(pygame, os.path.join(dir_sons, 'menu_vitoria.mp3'))
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
                                    edd.passa_de_fase()
                                    fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                                elif (fase == 2):
                                    fase += 1
                                    fase_atual = TerceiraFase()
                                    edd.passa_de_fase()
                                    fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                                elif (fase == 3):
                                    fase += 1
                                    fase_atual = QuartaFase()
                                    edd.passa_de_fase()
                                    fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                                elif (fase == 4):
                                    fase += 1
                                    fase_atual = QuintaFase()
                                    edd.passa_de_fase()
                                    fase_atual.dialogos.mostra_dialogos_iniciais(pygame)
                            elif (acao_menu == 'sair do jogo'):
                                pygame.quit()
                                sys.exit()
                        else:
                            pygame.mixer.music.load(os.path.join(dir_sons, 'final.mp3'))
                            pygame.mixer.music.set_volume(0.1)
                            pygame.mixer.music.play(-1)
                            fase_atual.dialogos.mostra_dialogos_finais(pygame)
                            pygame.mixer.music.stop()
                            menu_principal_ativo = True

                elif (event.key == pygame.K_1):
                    edd.mostra_informacoes_do_personagem()

                elif (event.key == pygame.K_2):
                    edd.mostra_coordenadas_do_personagem()

                elif (event.key == pygame.K_r):
                    edd.rastreia_robombas(pygame, fase_atual.mapa_da_fase.robombas)

                elif (event.key == pygame.K_TAB):
                    if (edd.item_atual == 1):
                        edd.altera_alvo()

