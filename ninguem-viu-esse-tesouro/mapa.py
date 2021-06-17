class Mapa:
    def __init__(self, largura, altura):
        from porta import Porta
        self.largura = largura
        self.altura = altura
        self.robombas = []
        self.baterias = []
        self.municoes = []
        self.porta_de_saida = Porta()

    def prepara_robombas(self, posicoes_dos_robombas):
        self.robombas = posicoes_dos_robombas

    def prepara_baterias(self, posicoes_das_baterias):
        self.baterias = posicoes_das_baterias

    def prepara_municoes(self, posicoes_das_municoes):
        self.municoes = posicoes_das_municoes

    def posiciona_porta(self, pos_porta):
        self.porta_de_saida.largura = pos_porta[0]
        self.porta_de_saida.altura = pos_porta[1]

    def verifica_armadilha_robomba(self, pygame, personagem, os, dir_sons):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        robomba_atual = 0
        for pos_robombas in self.robombas:
            if ((personagem.largura == pos_robombas[0]) and (personagem.altura == pos_robombas[1])):
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'explosao.wav'))
                som.play()
                personagem.hp -= 5
                frase = 'Edd: Acho que pisei em um robomba.'
                o.speak(frase, interrupt=True)
                self.robombas.pop(robomba_atual)
                break
            robomba_atual += 1

    def verifica_bateria(self, pygame, personagem, os, dir_sons):
        bateria_atual = 0
        for pos_baterias in self.baterias:
            if ((personagem.largura == pos_baterias[0]) and (personagem.altura == pos_baterias[1])):
                som = pygame.mixer.Sound(os.path.join(dir_sons, 'achou_bateria.wav'))
                som.play()
                self.baterias.pop(bateria_atual)
                return True
            bateria_atual += 1

    def verifica_municao(self, pygame, personagem):
        municao_atual = 0
        for pos_municoes in self.municoes:
            if ((personagem.largura == pos_municoes[0]) and (personagem.altura == pos_municoes[1])):
                self.municoes.pop(municao_atual)
                return True
            municao_atual += 1

