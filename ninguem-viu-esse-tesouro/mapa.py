class Mapa:
    def __init__(self, largura, altura):
        from porta import Porta
        self.largura = largura
        self.altura = altura
        self.robombas = []
        self.baterias = []
        self.porta_de_saida = Porta()

    def prepara_robombas(self, posicoes_dos_robombas):
        self.robombas = posicoes_dos_robombas

    def prepara_baterias(self, posicoes_das_baterias):
        self.baterias = posicoes_das_baterias

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

    def verifica_bateria(self, pygame, personagem):
        bateria_atual = 0
        for pos_baterias in self.baterias:
            if ((personagem.largura == pos_baterias[0]) and (personagem.altura == pos_baterias[1])):
                som_bateria = 'sons/efeitos/achou_bateria.wav'
                som = pygame.mixer.Sound(som_bateria)
                som.play()
                self.baterias.pop(bateria_atual)
                return True
            bateria_atual += 1

    def encontra_saida(self, pygame):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        frase = 'ISA: Parabéns! Você encontrou a saída. Pressione enter para seguir.'
        o.speak(frase, interrupt=True)
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    if ((event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
                        o.speak(frase, interrupt=True)

                    if (event.key == pygame.K_RETURN):
                        return

