class PrimeiraFase:
    def __init__(self):
        from dialogo import Dialogo
        from mapa import Mapa
        self.mapa_da_fase = Mapa(5, 6)
        self.dialogos = Dialogo()
        self.prepara_dialogos_iniciais()
        self.prepara_dialogos_finais()

    def prepara_dialogos_iniciais(self):
        self.dialogos.iniciais.append('Steve: Minha vida anda um pouco monótona ultimamente. Muito poucas coisas tem acontecido.')
        self.dialogos.iniciais.append('Steve: Nos últimos meses eu nem vi o tempo passar.')
        self.dialogos.iniciais.append('Steve: Talvez eu precise pensar mais naquela ideia de ter um companheiro, uma gatinha talvez. Se chamaria Isa.')
        self.dialogos.iniciais.append('Steve: Vou refletir um pouco mais a respeito disso. Agora preciso fazer outras coisas.')
        self.dialogos.iniciais.append('...')
        self.dialogos.iniciais.append('Você acessa o seu e-mail e encontra um com o seguinte título: Um grande jogo está chegando!')
        self.dialogos.iniciais.append('Você lembra de grandes experiências que teve com alguns jogos e por causa disso abre o e-mail e lê todo o seu conteúdo.')
        self.dialogos.iniciais.append('Steve: Minha nossa! Esse e-mail é de um desenvolvedor muito conhecido, e que gosto muito.')
        self.dialogos.iniciais.append('Só que o que mais te impressiona não é isso. Mas sim duas informações que estão no fim do e-mail.')
        self.dialogos.iniciais.append('A primeira é que parece que esse jogo pode ser expandido para uma experiência muito maior.')
        self.dialogos.iniciais.append('A segunda é que parece haver um tesouro prometido para quem completar os desafios dele nessa primeira versão.')
        self.dialogos.iniciais.append('Steve: Preciso tentar cumprir esses desafios. No mínimo terei um tempo de diversão.')
        self.dialogos.iniciais.append('Você baixa o jogo e depois de tudo pronto inicia ele')
        self.dialogos.iniciais.append('...')
        self.dialogos.iniciais.append('Inteligência artificial: Olá, você é o novo jogador que tentará passar pelos desafios. Eu sou uma inteligência artificial feita para te ajudar nessa jornada.')
        self.dialogos.iniciais.append('Inteligência artificial: Você deverá controlar o robô Edd e seu objetivo será levar ele até a saída de cada fase.')
        self.dialogos.iniciais.append('Inteligência artificial: Mas não será tão fácil assim. Você está em um cenário repleto de armadilhas.')
        self.dialogos.iniciais.append('Inteligência artificial: São bombas que você deve evitar, ou melhor, robombas. Se você encostar em algum ele explodirá e automaticamente você perderá parte do seu hp. Se você zerar o hp significará que perdeu o desafio.')
        self.dialogos.iniciais.append('Inteligência artificial: Todas as saídas estarão bloqueadas. Você deve encontrar as pilhas ao redor do cenário para que a chave que você carrega possa abrir a porta de saída.')
        self.dialogos.iniciais.append('Inteligência artificial: Agora deixe me explicar como funcionarão as pilhas, tanto em estrutura de dados quanto na sua chave eletrônica de pilhas.')
        self.dialogos.iniciais.append('...')
        self.dialogos.iniciais.append('Inteligência artificial: Lembrando que você sempre poderá revisitar os conhecimentos sobre a estrutura de dados pilha dentro do menu de ajuda das estruturas de dados. Tanto no menu inicial quanto no menu de pausa, ao apertar esc.')
        self.dialogos.iniciais.append('Inteligência artificial: Agora voltando ao jogo e o seu objetivo, use w para se mover para frente, s para se mover para trás, a para se mover para esquerda e d para se mover para a direita.')
        self.dialogos.iniciais.append('Inteligência artificial: Setas para esquerda ou para direita dizem o quanto de pilha você tem. Quando tiver as 3 que precisa é só apertar seta para cima que a chave será ativada.')
        self.dialogos.iniciais.append('Inteligência artificial: Então basta seguir até a porta e estando na sua frente aperte enter para abrir ela.')
        self.dialogos.iniciais.append('Inteligência artificial: Boa sorte!')

    def prepara_dialogos_finais(self):
        self.dialogos.finais.append('Inteligência artificial: Bom trabalho!')
        self.dialogos.finais.append('Inteligência artificial: Mas não pense que as próximas fases serão fáceis como essa. O grande desafio apenas começou.')
        self.dialogos.finais.append('Inteligência artificial: Lembre-se que sempre que precisar você poderá conferir o conhecimento de como funciona pilhas lá no menu de ajuda das estruturas de dados.')
        self.dialogos.finais.append('Inteligência artificial: Boa sorte na próxima fase.')

