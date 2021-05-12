class Personagem:
    def __init__(self):
        self.nome = 'Edd'
        self.hp = 10
        self.altura = 0
        self.largura = 2
        self.anel_de_lista = None
        self.chave_eletronica_de_pilha = None
        self.arma_de_portais_com_fila = None

    def navega_no_mapa(self, pygame, event, mapa):
        if (event == pygame.K_w):
            if ((self.altura+1) > (mapa.altura-1)):
                som_parede = 'sons/efeitos/parede.wav'
                som = pygame.mixer.Sound(som_parede)
                som.play()
                return
            else:
                som_passos = 'sons/efeitos/passos.wav'
                som = pygame.mixer.Sound(som_passos)
                som.play()
                self.altura += 1
                return

        elif (event == pygame.K_s):
            if ((self.altura-1) < 0):
                som_parede = 'sons/efeitos/parede.wav'
                som = pygame.mixer.Sound(som_parede)
                som.play()
                return
            else:
                som_passos = 'sons/efeitos/passos.wav'
                som = pygame.mixer.Sound(som_passos)
                som.play()
                self.altura -= 1
                return

        elif (event == pygame.K_a):
            if ((self.largura-1) < 0):
                som_parede = 'sons/efeitos/parede.wav'
                som = pygame.mixer.Sound(som_parede)
                som.play()
                return
            else:
                som_passos = 'sons/efeitos/passos.wav'
                som = pygame.mixer.Sound(som_passos)
                som.play()
                self.largura -= 1
                return

        elif (event == pygame.K_d):
            if ((self.largura+1) > (mapa.largura-1)):
                som_parede = 'sons/efeitos/parede.wav'
                som = pygame.mixer.Sound(som_parede)
                som.play()
                return
            else:
                som_passos = 'sons/efeitos/passos.wav'
                som = pygame.mixer.Sound(som_passos)
                som.play()
                self.largura += 1
                return

