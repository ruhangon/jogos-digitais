class Menu:
    def __init__(self, pygame, dir_trilha):
        self.lista_opcoes = []
        self.ponteiro = 0
        self.musica = pygame.mixer.music.load(dir_trilha)

    def adiciona_item(self, item):
        self.lista_opcoes.append(str(item))

    def faz_acao(self, pygame):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP):
                    if ((self.ponteiro-1) < 0):
                        o.speak(self.lista_opcoes[self.ponteiro], interrupt=True)
                    else:
                        self.ponteiro -= 1
                        o.speak(self.lista_opcoes[self.ponteiro], interrupt=True)

                elif (event.key == pygame.K_DOWN):
                    if ((self.ponteiro+1) >= len(self.lista_opcoes)):
                        o.speak(self.lista_opcoes[self.ponteiro], interrupt=True)
                    else:
                        self.ponteiro += 1
                        o.speak(self.lista_opcoes[self.ponteiro], interrupt=True)

                elif (event.key == pygame.K_RETURN):
                    som_enter = 'sons/efeitos/enter.wav'
                    som = pygame.mixer.Sound(som_enter)
                    som.play()
                    return self.lista_opcoes[self.ponteiro]

