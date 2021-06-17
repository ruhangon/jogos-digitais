class Arma:
    def __init__(self):
        from collections import deque
        self.nome = 'Arma'
        self.municao = deque()
        self.alvos_na_mira = [0, 0, 0, 0]
        self.mira_atual = -1

    def insere(self):
        self.municao.append(True)

    def atira(self, pygame, os, dir_sons):
        if (len(self.municao) > 0):
            atirou = self.municao.popleft()
            som = pygame.mixer.Sound(os.path.join(dir_sons, 'tiro.wav'))
            som.play()
            return atirou
        else:
            som = pygame.mixer.Sound(os.path.join(dir_sons, 'sem_municao.wav'))
            som.play()
            return False

    def mostra_informacoes(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        item = 'Item = ' + self.nome
        quantidade = 'Quantidade de munição = ' + str(len(self.municao))
        frase = 'Edd: ' + item + '. ' + quantidade
        o.speak(frase, interrupt=True)

