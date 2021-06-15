class GuardaBaterias:
    def __init__(self):
        self.nome = 'Guarda baterias'
        self.baterias = []

    def insere(self):
        self.baterias.append(True)

    def retira(self):
        if (len(self.baterias) > 0):
            bat = self.baterias.pop()
            return bat

    def mostra_informacoes(self):
        from accessible_output2.outputs.auto import Auto
        o = Auto()
        item = 'Item = ' + self.nome
        quantidade = 'Quantidade de baterias = ' + str(len(self.baterias))
        frase = 'Edd: ' + item + '. ' + quantidade
        o.speak(frase, interrupt=True)

