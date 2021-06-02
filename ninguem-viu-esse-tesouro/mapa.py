class Mapa:
    def __init__(self, largura, altura):
        from porta import Porta
        self.largura = largura
        self.altura = altura
        self.robombas = []
        self.capsulas = []
        self.porta_de_saida = Porta()

    def prepara_robombas(self, posicoes_dos_robombas):
        self.robombas = posicoes_dos_robombas

    def prepara_capsulas(self, posicoes_das_capsulas):
        self.capsulas = posicoes_das_capsulas

    def posiciona_porta(self, pos_porta):
        self.porta_de_saida.largura = pos_porta[0]
        self.porta_de_saida.altura = pos_porta[1]

    def verifica_armadilha_robomba(self, pygame, personagem):
        robomba_atual = 0
        for pos_robombas in self.robombas:
            if ((personagem.largura == pos_robombas[0]) and (personagem.altura == pos_robombas[1])):
                som_explosao = 'sons/efeitos/explosao.wav'
                som = pygame.mixer.Sound(som_explosao)
                som.play()
                personagem.hp -= 5
                self.robombas.pop(robomba_atual)
                break
            robomba_atual += 1

    def verifica_capsula(self, pygame, personagem):
        capsula_atual = 0
        for pos_capsulas in self.capsulas:
            if ((personagem.largura == pos_capsulas[0]) and (personagem.altura == pos_capsulas[1])):
                som_capsula = 'sons/efeitos/achou_capsula.wav'
                som = pygame.mixer.Sound(som_capsula)
                som.play()
                self.capsulas.pop(capsula_atual)
                return True
            capsula_atual += 1

