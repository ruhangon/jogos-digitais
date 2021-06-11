class Dialogo:
    def __init__(self):
        from collections import deque
        self.iniciais = deque()
        self.finais = deque()

    def mostra_dialogos_iniciais(self, pygame):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        frase_atual = self.iniciais.popleft()
        o.speak(frase_atual, interrupt=True)
        while (len(self.iniciais) > 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RETURN):
                        frase_atual = self.iniciais.popleft()
                        o.speak(frase_atual, interrupt=True)
                    elif ((event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
                        o.speak(frase_atual, interrupt=True)
                    elif (event.key == pygame.K_ESCAPE):
                        self.iniciais.clear()
                        self.iniciais.append('Pressione enter para iniciar a fase.')
                        frase_atual = self.iniciais.popleft()
                        o.speak(frase_atual, interrupt=True)

    def mostra_dialogos_finais(self, pygame):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        frase_atual = self.finais.popleft()
        o.speak(frase_atual, interrupt=True)
        while (len(self.finais) > 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RETURN):
                        frase_atual = self.finais.popleft()
                        o.speak(frase_atual, interrupt=True)
                    elif ((event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
                        o.speak(frase_atual, interrupt=True)
                    elif (event.key == pygame.K_ESCAPE):
                        self.finais.clear()

