class GuardaCapsulas:
    def init__(self):
        self.nome = 'Guarda cápsulas'
        self.capsulas = []

    def insere(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        self.capsulas.append(True)
        frase = 'Uma cápsula foi adicionada ao topo da pilha do guarda cápsulas.'
        o.speak(frase, interrupt=True)

    def retira(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        if (len(self.capsulas) > 0):
            cap = self.capsulas.pop()
            frase = 'A cápsula energizada do topo da pilha do guarda cápsulas foi retirada.'
            o.speak(frase, interrupt=True)
            return cap

    def __str__(self):
        return 'Nome: ' + self.nome + '. Quantidade: ' + str(len(self.capsulas)) + '.'

