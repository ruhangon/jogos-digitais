class Porta:
    def __init__(self):
        self.largura = -1
        self.altura = -1
        self.trancada = True
        self.capsulas_energizadas = 0

    def insere_capsula_energizada(self, pygame, tem_capsula):
        if (tem_capsula == True):
            self.capsulas_energizadas += 1
            som_capsula_inserida = 'sons/efeitos/inseriu_capsula.wav'
            som = pygame.mixer.Sound(som_capsula_inserida)
            som.play()

    def abre_porta(self, pygame):
        if (self.capsulas_energizadas == 3):
            self.trancada = False
            som_abertura = 'sons/efeitos/abriu_porta.wav'
            som = pygame.mixer.Sound(som_abertura)
            som.play()

