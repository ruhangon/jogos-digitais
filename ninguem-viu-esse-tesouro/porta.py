class Porta:
    def __init__(self):
        self.largura = -1
        self.altura = -1
        self.trancada = True
        self.baterias_energizadas = 0

    def insere_bateria_energizada(self, pygame, tem_bateria):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        if (tem_bateria == True):
            self.baterias_energizadas += 1
            som_bateria_inserida = 'sons/efeitos/inseriu_bateria.wav'
            som = pygame.mixer.Sound(som_bateria_inserida)
            som.play()
            falta = 3-self.baterias_energizadas
            frase = 'Edd: Faltam ' + str(falta) + ' baterias para energizar a porta.'
            o.speak(frase, interrupt=False)

