class GuardaBaterias:
    def __init__(self):
        self.nome = 'Guarda baterias'
        self.baterias = []

    def insere(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        self.baterias.append(True)
        frase = 'Edd: Uma bateria foi adicionada ao topo da pilha do guarda baterias e será energizada.'
        o.speak(frase, interrupt=True)

    def retira(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        if (len(self.baterias) > 0):
            bat = self.baterias.pop()
            frase = 'Edd: A bateria energizada do topo da pilha do guarda baterias foi retirada.'
            o.speak(frase, interrupt=False)
            return bat

    def mostra_informacoes(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        item = 'Item = ' + self.nome
        quantidade = 'Quantidade = ' + str(len(self.baterias))
        frase = 'Edd: ' + item + '. ' + quantidade
        o.speak(frase, interrupt=True)

