class Personagem:
    def __init__(self):
        self.nome = 'Edd'
        self.hp = 10
        self.largura = 3
        self.altura = 1

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

