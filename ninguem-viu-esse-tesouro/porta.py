class Porta:
    def __init__(self):
        self.largura = -1
        self.altura = -1
        self.trancada = True
        self.baterias_energizadas = 0

    def insere_bateria_energizada(self, pygame, tem_bateria):
        if (tem_bateria == True):
            self.baterias_energizadas += 1
            som_bateria_inserida = 'sons/efeitos/inseriu_bateria.wav'
            som = pygame.mixer.Sound(som_bateria_inserida)
            som.play()

    def abre_porta(self, pygame):
        if (self.baterias_energizadas == 3):
            self.trancada = False
            som_abertura = 'sons/efeitos/abriu_porta.wav'
            som = pygame.mixer.Sound(som_abertura)
            som.play()

