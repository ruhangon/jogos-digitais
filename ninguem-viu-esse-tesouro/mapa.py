class Mapa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.robombas = []

    def prepara_robombas(self, posicoes_dos_robombas):
        self.robombas = posicoes_dos_robombas

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

