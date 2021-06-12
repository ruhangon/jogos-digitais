class Personagem:
    def __init__(self):
        from item.guarda_baterias import GuardaBaterias
        self.nome = 'Edd'
        self.hp = 10
        self.largura = 3
        self.altura = 1
        self.guarda_baterias = GuardaBaterias()
        self.item_atual = 0

    def navega_no_mapa(self, pygame, event, mapa):
        if (event == pygame.K_w):
            if ((self.altura+1) > mapa.altura):
                som_parede = 'sons/efeitos/parede.wav'
                som = pygame.mixer.Sound(som_parede)
                som.play()
            else:
                som_passos = 'sons/efeitos/passos.wav'
                som = pygame.mixer.Sound(som_passos)
                som.play()
                self.altura += 1
        elif (event == pygame.K_s):
            if ((self.altura-1) < 1):
                som_parede = 'sons/efeitos/parede.wav'
                som = pygame.mixer.Sound(som_parede)
                som.play()
            else:
                som_passos = 'sons/efeitos/passos.wav'
                som = pygame.mixer.Sound(som_passos)
                som.play()
                self.altura -= 1
        elif (event == pygame.K_a):
            if ((self.largura-1) < 1):
                som_parede = 'sons/efeitos/parede.wav'
                som = pygame.mixer.Sound(som_parede)
                som.play()
            else:
                som_passos = 'sons/efeitos/passos.wav'
                som = pygame.mixer.Sound(som_passos)
                som.play()
                self.largura -= 1
        elif (event == pygame.K_d):
            if ((self.largura+1) > mapa.largura):
                som_parede = 'sons/efeitos/parede.wav'
                som = pygame.mixer.Sound(som_parede)
                som.play()
            else:
                som_passos = 'sons/efeitos/passos.wav'
                som = pygame.mixer.Sound(som_passos)
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

    def radar_robombas(self, pygame, pos_robombas):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        alerta_robomba = False
        if ([(self.largura+1), self.altura] in pos_robombas):
            som_radar_robomba = 'sons/efeitos/radar_robomba.wav'
            som = pygame.mixer.Sound(som_radar_robomba)
            som.play()
            alerta_robomba = True
        elif ([(self.largura-1), self.altura] in pos_robombas):
            som_radar_robomba = 'sons/efeitos/radar_robomba.wav'
            som = pygame.mixer.Sound(som_radar_robomba)
            som.play()
            alerta_robomba = True
        elif ([self.largura, (self.altura-1)] in pos_robombas):
            som_radar_robomba = 'sons/efeitos/radar_robomba.wav'
            som = pygame.mixer.Sound(som_radar_robomba)
            som.play()
            alerta_robomba = True
        elif ([self.largura, (self.altura+1)] in pos_robombas):
            som_radar_robomba = 'sons/efeitos/radar_robomba.wav'
            som = pygame.mixer.Sound(som_radar_robomba)
            som.play()
            alerta_robomba = True
        if (alerta_robomba == True):
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

    def pega_bateria(self):
        self.guarda_baterias.insere()

    def localiza_porta(self, mapa):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        if ((self.largura == mapa.porta_de_saida.largura) and (self.altura == mapa.porta_de_saida.altura)):
            frase = 'Edd: A porta de saída dessa fase está aqui. Você pode inserir uma bateria energizada nela se tiver. Para isso encontre suas baterias com seta para esquerda ou seta para direita e quando encontrar aperte seta para cima.'
            o.speak(frase, interrupt=True)

    def insere_bateria_na_porta(self, pygame, mapa):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        if ((self.largura == mapa.porta_de_saida.largura) and (self.altura == mapa.porta_de_saida.altura)):
            if (self.guarda_baterias.retira() == True):
                mapa.porta_de_saida.insere_bateria_energizada(pygame, True)
                if (mapa.porta_de_saida.baterias_energizadas == 3):
                    som_porta_energizada = 'sons/efeitos/porta_energizada.wav'
                    som = pygame.mixer.Sound(som_porta_energizada)
                    som.play()
                    frase = 'Edd: A porta está energizada. Pressione enter para abrir ela e assim poder finalizar a fase.'
                    o.speak(frase, interrupt=False)
            else:
                frase = 'Edd: Você não tem baterias no topo da pilha.'
                o.speak(frase, interrupt=True)

    def abre_porta(self, pygame, mapa):
        if ((self.largura == mapa.porta_de_saida.largura) and (self.altura == mapa.porta_de_saida.altura)):
            if (mapa.porta_de_saida.baterias_energizadas == 3):
                mapa.porta_de_saida.trancada = False
                som_completou_fase = 'sons/efeitos/completou_fase.wav'
                som = pygame.mixer.Sound(som_completou_fase)
                som.play()
            else:
                som_porta_trancada = 'sons/efeitos/porta_trancada.wav'
                som = pygame.mixer.Sound(som_porta_trancada)
                som.play()

    def altera_item(self, pygame, event):
        if (event == pygame.K_LEFT):
            self.item_atual = 0
        elif (event == pygame.K_RIGHT):
            self.item_atual = 0

    def mostra_informacoes_do_item_atual(self):
        if (self.item_atual == 0):
            self.guarda_baterias.mostra_informacoes()

