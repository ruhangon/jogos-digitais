class Personagem:
    def __init__(self):
        from item.guarda_capsulas import GuardaCapsulas
        self.nome = 'Edd'
        self.hp = 10
        self.largura = 3
        self.altura = 1
        self.guarda_capsulas = GuardaCapsulas()
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
        if ([(self.largura+1), self.altura] in pos_robombas):
            som_radar_robomba = 'sons/efeitos/radar_robomba.wav'
            som = pygame.mixer.Sound(som_radar_robomba)
            som.play()
        elif ([(self.largura-1), self.altura] in pos_robombas):
            som_radar_robomba = 'sons/efeitos/radar_robomba.wav'
            som = pygame.mixer.Sound(som_radar_robomba)
            som.play()
        elif ([self.largura, (self.altura-1)] in pos_robombas):
            som_radar_robomba = 'sons/efeitos/radar_robomba.wav'
            som = pygame.mixer.Sound(som_radar_robomba)
            som.play()
        elif ([self.largura, (self.altura+1)] in pos_robombas):
            som_radar_robomba = 'sons/efeitos/radar_robomba.wav'
            som = pygame.mixer.Sound(som_radar_robomba)
            som.play()

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

    def pega_capsula(self):
        self.guarda_capsulas.insere()

    def altera_item(self, pygame, event):
        if (event == pygame.K_LEFT):
            self.item_atual = 0
        elif (event == pygame.K_RIGHT):
            self.item_atual = 0

    def mostra_informacoes_do_item_atual(self):
        if (self.item_atual == 0):
            self.guarda_capsulas.mostra_informacoes()

