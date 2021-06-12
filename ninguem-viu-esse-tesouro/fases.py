class PrimeiraFase:
    def __init__(self):
        from dialogo import Dialogo
        from mapa import Mapa
        self.mapa_da_fase = Mapa(5, 6)
        self.mapa_da_fase.prepara_robombas([[3, 3], [2, 5], [4, 5]])
        self.mapa_da_fase.prepara_baterias([[3, 2], [3, 4], [5, 1]])
        self.mapa_da_fase.posiciona_porta([3, 6])
        self.dialogos = Dialogo()
        self.prepara_dialogos_iniciais()
        self.prepara_dialogos_finais()

    def prepara_dialogos_iniciais(self):
        self.dialogos.iniciais.append('Pressione enter para avançar nos diálogos, seta para cima ou seta para baixo repete o diálogo atual. Você pode pressionar esc para pular eles e ir direto para a fase.')
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
        self.dialogos.iniciais.append('Inteligência artificial: A saída, ao norte do cenário, estará bloqueada. Você deve encontrar as baterias ao redor do cenário para que possa inserir elas na porta, então ela será energizada e poderá ser aberta.')
        self.dialogos.iniciais.append('Inteligência artificial: Agora deixe me explicar como você deverá levar as baterias. Para isso você precisará entender um pouco de como funciona a estrutura de dados pilha.')
        self.dialogos.iniciais.append('Inteligência artificial: As baterias que você pegar serão colocadas dentro de um guarda baterias que você carrega consigo.')
        self.dialogos.iniciais.append('Inteligência artificial: A princípio, quando você está sem baterias, qualquer uma que você pegar ficará no topo da pilha de baterias.')
        self.dialogos.iniciais.append('Inteligência artificial: Se já houver uma no guarda cápsulas, a próxima que você pegar ficará acima dessa. Essa última a ser inserida será o novo topo da pilha de baterias.')
        self.dialogos.iniciais.append('Inteligência artificial: Sempre que você precisar retirar uma bateria do guarda baterias você apenas irá conseguir retirar a que está mais no topo dele, você só terá acesso a primeira que pegou quando tiver retirado todas as outras que estavam acima dessa.')
        self.dialogos.iniciais.append('Inteligência artificial: Para você entender melhor, se você não tiver nenhuma bateria no guarda baterias e pegar uma nova, a bateria A, essa será inserida no topo da pilha do guarda baterias. Agora se você precisar retirar uma delas, a primeira a ser retirada será a bateria A, pois ela é a que está no topo da pilha de baterias.')
        self.dialogos.iniciais.append('Inteligência artificial: Em outra situação, se você estiver sem nenhuma bateria e pegar a bateria B essa irá para o topo da pilha de baterias, nesse momento se você for retirar uma do guarda baterias a B será a primeira a ser retirada.')
        self.dialogos.iniciais.append('Inteligência artificial: Se você não tiver retirado a B e depois acabar encontrando a C, essa irá para o topo da pilha de baterias. Depois de um tempo se você encontrar mais uma, a D, agora ela que irá para o topo. Se você reparar agora você terá a pilha B C D.')
        self.dialogos.iniciais.append('Inteligência artificial: Quando você precisar retirar todas as baterias da pilha de baterias B C D, primeiro será retirada a bateria D, depois a C e por fim a B.')
        self.dialogos.iniciais.append('Inteligência artificial: Logo se você reparar, a última que você adicionar sempre será a primeira que irá sair.')
        self.dialogos.iniciais.append('Inteligência artificial: Você sempre poderá revisitar os conhecimentos sobre a estrutura de dados pilha acessando o menu de pausa. Para isso você só precisa pressionar esc enquanto está jogando.')
        self.dialogos.iniciais.append('Inteligência artificial: Agora voltando ao jogo e o seu objetivo, use w para se mover para frente, s para se mover para trás, a para se mover para esquerda e d para se mover para a direita.')
        self.dialogos.iniciais.append('Inteligência artificial: Setas para esquerda ou para direita dizem o quanto de bateria você tem. Sempre que estiver próximo a porta e quiser inserir uma bateria nela você só precisa apertar seta para cima.')
        self.dialogos.iniciais.append('Inteligência artificial: Quando a porta estiver com 3 baterias ela estará totalmente energizada, nessa hora você escutará um som diferente. Então para abrir ela bastará pressionar enter.')
        self.dialogos.iniciais.append('Pressione enter para iniciar a fase.')

    def prepara_dialogos_finais(self):
        self.dialogos.finais.append('Inteligência artificial: Bom trabalho!')
        self.dialogos.finais.append('Inteligência artificial: Você completou a primeira fase.')
        self.dialogos.finais.append('Inteligência artificial: Lembre-se que sempre que precisar você poderá conferir o conhecimento de como funciona pilhas lá no menu de ajuda das estruturas de dados.')
        self.dialogos.finais.append('Inteligência artificial: Boa sorte na próxima fase.')

class SegundaFase:
    def __init__(self):
        from dialogo import Dialogo
        from mapa import Mapa
        self.mapa_da_fase = Mapa(5, 6)
        self.mapa_da_fase.prepara_robombas([[1, 4], [2, 4], [3,4], [4, 4]])
        self.mapa_da_fase.prepara_baterias([[1, 3], [5, 4], [1, 5]])
        self.mapa_da_fase.posiciona_porta([3, 6])
        self.dialogos = Dialogo()
        self.prepara_dialogos_iniciais()
        self.prepara_dialogos_finais()

    def prepara_dialogos_iniciais(self):
        self.dialogos.iniciais.append('Inteligência artificial: Seja bem vindo a segunda fase.')
        self.dialogos.iniciais.append('Inteligência artificial: Agora que estamos nos conhecendo melhor, posso dizer para você que a primeira fase foi apenas uma brincadeira.')
        self.dialogos.iniciais.append('Inteligência artificial: A cada nova fase os desafios ficarão mais difíceis e você precisará tomar mais cuidado.')
        self.dialogos.iniciais.append('Inteligência artificial: Não sei porque estou comentando isso com você. Não acredito que vá conseguir chegar muito longe.')
        self.dialogos.iniciais.append('Inteligência artificial: De qualquer forma, saiba que seu objetivo continua sendo o mesmo de antes e a porta continua ao norte.')
        self.dialogos.iniciais.append('Inteligência artificial: Essa fase não terá nenhuma novidade em relação a itens.')
        self.dialogos.iniciais.append('Pressione enter para iniciar a fase.')

    def prepara_dialogos_finais(self):
        self.dialogos.finais.append('Inteligência artificial: Impressionante!')
        self.dialogos.finais.append('Inteligência artificial: Estou surpresa que tenha conseguido chegar a essa saída.')
        self.dialogos.finais.append('Inteligência artificial: Bom, todos tem um pouco de sorte. Não seria diferente com você.')
        self.dialogos.finais.append('Inteligência artificial: Nos encontramos na próxima fase.')

