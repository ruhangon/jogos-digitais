class GuardaCapsulas:
    def __init__(self):
        self.nome = 'Guarda cápsulas'
        self.capsulas = []

    def insere(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        self.capsulas.append(True)
        frase = 'Edd: Uma cápsula foi adicionada ao topo da pilha do guarda cápsulas.'
        o.speak(frase, interrupt=True)

    def retira(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        if (len(self.capsulas) > 0):
            cap = self.capsulas.pop()
            frase = 'Edd: A cápsula energizada do topo da pilha do guarda cápsulas foi retirada.'
            o.speak(frase, interrupt=True)
            return cap

    def mostra_informacoes(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        item = 'Item = ' + self.nome
        quantidade = 'Quantidade = ' + str(len(self.capsulas))
        frase = 'Edd: ' + item + '. ' + quantidade
        o.speak(frase, interrupt=True)

