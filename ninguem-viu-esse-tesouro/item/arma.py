class Arma:
    def __init__(self):
        from collections import deque
        self.nome = 'Arma'
        self.municao = deque()
        self.alvos_na_mira = [0, 0, 0, 0]
        self.mira_atual = -1

    def insere(self):
        self.municao.append(True)

    def atira(self, pygame):
        if (len(self.municao) > 0):
            atirou = self.municao.popleft()
            som_tiro = 'sons/efeitos/tiro.wav'
            som = pygame.mixer.Sound(som_tiro)
            som.play()
            return atirou
        else:
            som_sem_municao = 'sons/efeitos/sem_municao.wav'
            som = pygame.mixer.Sound(som_sem_municao)
            som.play()
            return False

    def mostra_informacoes(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        item = 'Item = ' + self.nome
        quantidade = 'Quantidade de munição = ' + str(len(self.municao))
        frase = 'Edd: ' + item + '. ' + quantidade
        o.speak(frase, interrupt=True)

