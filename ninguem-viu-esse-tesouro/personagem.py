class Personagem:
    def __init__(self):
        from item.arma import Arma
        from item.guarda_baterias import GuardaBaterias
        self.nome = 'Edd'
        self.hp = 10
        self.largura = 3
        self.altura = 1
        self.guarda_baterias = GuardaBaterias()
        self.arma = Arma()
        self.item_atual = 0

    def navega_no_mapa(self, pygame, event, mapa, os, dir_sons):
        if (event == pygame.K_UP):
            if ((self.altura+1) > mapa.altura):
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'parede.wav'))
                som.play()
            else:
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'passos.wav'))
                som.play()
                self.altura += 1
        elif (event == pygame.K_DOWN):
            if ((self.altura-1) < 1):
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'parede.wav'))
                som.play()
            else:
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'passos.wav'))
                som.play()
                self.altura -= 1
        elif (event == pygame.K_LEFT):
            if ((self.largura-1) < 1):
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'parede.wav'))
                som.play()
            else:
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'passos.wav'))
                som.play()
                self.largura -= 1
        elif (event == pygame.K_RIGHT):
            if ((self.largura+1) > mapa.largura):
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'parede.wav'))
                som.play()
            else:
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'passos.wav'))
                som.play()
                self.largura += 1

    def mostra_informacoes_do_personagem(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        nome = 'Nome: ' + self.nome
        hp = 'Vida: ' + str(self.hp)
        frase = nome +'. '+ hp
        o.speak(frase, interrupt=True)

    def mostra_coordenadas_do_personagem(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        x = 'X: ' + str(self.largura)
        y = 'Y: ' + str(self.altura)
        coord = x +'. '+ y
        o.speak(coord, interrupt=True)

    def sobrevive(self):
        if (self.hp > 0):
            return True
        return False

    def revive(self):
        self.hp = 10
        self.largura = 3
        self.altura = 1
        self.guarda_baterias.baterias.clear()
        self.arma.municao.clear()

    def passa_de_fase(self):
        self.hp = 10
        self.largura = 3
        self.altura = 1

    def radar_robombas(self, pygame, pos_robombas, os, dir_sons):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        alerta_robomba = False
        if ([self.largura, (self.altura+1)] in pos_robombas):
            alerta_robomba = True
        elif ([(self.largura+1), self.altura] in pos_robombas):
            alerta_robomba = True
        elif ([self.largura, (self.altura-1)] in pos_robombas):
            alerta_robomba = True
        elif ([(self.largura-1), self.altura] in pos_robombas):
            alerta_robomba = True
        if (alerta_robomba == True):
            som = pygame.mixer.Sound(os.path.join(dir_sons, 'radar_robomba.wav'))
            som.play()
            frase = 'Edd: Há pelo menos um robomba localizado.'
            o.speak(frase, interrupt=False)

    def rastreia_robombas(self, pygame, pos_robombas):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        robombas_localizados = ''
        if ([(self.largura-1), self.altura] in pos_robombas):
            robombas_localizados += 'Há um robomba na sua esquerda. '
        if ([(self.largura+1), self.altura] in pos_robombas):
            robombas_localizados += 'Há um robomba na sua direita. '
        if ([self.largura, (self.altura+1)] in pos_robombas):
            robombas_localizados += 'Há um robomba acima. '
        if ([self.largura, (self.altura-1)] in pos_robombas):
            robombas_localizados += 'Há um robomba abaixo.'
        if (robombas_localizados != ''):
            frase = 'Radar do Edd: ' + robombas_localizados
            o.speak(frase, interrupt=True)

    def procura_robombas(self, pos_robombas):
        self.arma.mira_atual = -1
        self.arma.alvos_na_mira = [0, 0, 0, 0]
        if ([self.largura, (self.altura+1)] in pos_robombas):
            self.arma.alvos_na_mira[0] += 1
            self.arma.mira_atual = 0
        if ([(self.largura+1), self.altura] in pos_robombas):
            self.arma.alvos_na_mira[1] += 1
            self.arma.mira_atual = 1
        if ([self.largura, (self.altura-1)] in pos_robombas):
            self.arma.alvos_na_mira[2] += 1
            self.arma.mira_atual = 2
        if ([(self.largura-1), self.altura] in pos_robombas):
            self.arma.alvos_na_mira[3] += 1
            self.arma.mira_atual = 3

    def pega_bateria(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        self.guarda_baterias.insere()
        frase = 'Edd: Uma bateria foi adicionada ao topo da pilha do guarda baterias e será energizada.'
        o.speak(frase, interrupt=False)

    def pega_municao_e_recarrega(self, pygame, os, dir_sons):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        self.arma.insere()
        som = pygame.mixer.Sound(os.path.join(dir_sons, 'achou_municao_e_recarregou.wav'))
        som.play()
        frase = 'Edd: Peguei uma munição e coloquei no fim da fila ao recarregar a arma.'
        o.speak(frase, interrupt=False)

    def localiza_porta(self, mapa):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        if ((self.largura == mapa.porta_de_saida.largura) and (self.altura == mapa.porta_de_saida.altura)):
            frase = 'Edd: A porta de saída dessa fase está aqui. Você pode inserir uma bateria energizada nela se tiver. Para isso encontre suas baterias com a tecla CTRL e quando encontrar aperte barra de espaço.'
            o.speak(frase, interrupt=True)

    def insere_bateria_na_porta(self, pygame, mapa, os, dir_sons):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        if ((self.largura == mapa.porta_de_saida.largura) and (self.altura == mapa.porta_de_saida.altura)):
            if (self.guarda_baterias.retira() == True):
                frase = 'Edd: A bateria energizada do topo da pilha do guarda baterias foi retirada.'
                o.speak(frase, interrupt=False)
                mapa.porta_de_saida.insere_bateria_energizada(pygame, True, os, dir_sons)
                if (mapa.porta_de_saida.baterias_energizadas == 3):
                    som = pygame.mixer.Sound(os.path.join(dir_sons, 'porta_energizada.wav'))
                    som.play()
                    frase = 'Edd: A porta está energizada. Pressione enter para abrir ela e assim poder finalizar a fase.'
                    o.speak(frase, interrupt=False)
            else:
                frase = 'Edd: Você não tem baterias no topo da pilha.'
                o.speak(frase, interrupt=True)

    def altera_alvo(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        alvos = self.arma.alvos_na_mira.count(1)
        if (alvos > 1):
            while (True):
                if (self.arma.mira_atual == 3):
                    self.arma.mira_atual = 0
                else:
                    self.arma.mira_atual += 1
                if (self.arma.alvos_na_mira[self.arma.mira_atual] == 1):
                    break
        if (alvos > 0):
            if (self.arma.mira_atual == 0):
                frase = 'Edd: Mira focada no robomba acima.'
                o.speak(frase, interrupt = True)
            elif (self.arma.mira_atual == 1):
                frase = 'Edd: Mira focada no robomba a direita.'
                o.speak(frase, interrupt = True)
            elif (self.arma.mira_atual == 2):
                frase = 'Edd: Mira focada no robomba abaixo.'
                o.speak(frase, interrupt = True)
            elif (self.arma.mira_atual == 3):
                frase = 'Edd: Mira focada no robomba a esquerda.'
                o.speak(frase, interrupt = True)

    def aperta_gatilho(self, pygame, mapa, os, dir_sons):
        if (self.arma.mira_atual != -1):
            if (self.arma.mira_atual == 0):
                tem_municao = self.arma.atira(pygame, os, dir_sons)
                if (tem_municao == True):
                    mapa.robombas.remove([self.largura, (self.altura+1)])
                    som = pygame.mixer.Sound(os.path.join(dir_sons, 'explosao.wav'))
                    som.play()
                    self.arma.mira_atual = -1
            elif (self.arma.mira_atual == 1):
                tem_municao = self.arma.atira(pygame, os, dir_sons)
                if (tem_municao == True):
                    mapa.robombas.remove([(self.largura+1), self.altura])
                    som = pygame.mixer.Sound(os.path.join(dir_sons, 'explosao.wav'))
                    som.play()
                    self.arma.mira_atual = -1
            elif (self.arma.mira_atual == 2):
                tem_municao = self.arma.atira(pygame, os, dir_sons)
                if (tem_municao == True):
                    mapa.robombas.remove([self.largura, (self.altura-1)])
                    som = pygame.mixer.Sound(os.path.join(dir_sons, 'explosao.wav'))
                    som.play()
                    self.arma.mira_atual = -1
            elif (self.arma.mira_atual == 3):
                tem_municao = self.arma.atira(pygame, os, dir_sons)
                if (tem_municao == True):
                    mapa.robombas.remove([(self.largura-1), self.altura])
                    som = pygame.mixer.Sound(os.path.join(dir_sons, 'explosao.wav'))
                    som.play()
                    self.arma.mira_atual = -1

    def abre_porta(self, pygame, mapa, os, dir_sons):
        if ((self.largura == mapa.porta_de_saida.largura) and (self.altura == mapa.porta_de_saida.altura)):
            if (mapa.porta_de_saida.baterias_energizadas == 3):
                mapa.porta_de_saida.trancada = False
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'completou_fase.wav'))
                som.play()
            else:
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'porta_trancada.wav'))
                som.play()

    def altera_item(self):
        if (self.item_atual == 0):
            self.item_atual = 1
        else:
            self.item_atual = 0

    def mostra_informacoes_do_item_atual(self):
        if (self.item_atual == 0):
            self.guarda_baterias.mostra_informacoes()
        elif (self.item_atual == 1):
            self.arma.mostra_informacoes()

