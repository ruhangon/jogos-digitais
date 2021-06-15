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
        self.dialogos.iniciais.append('Inteligência artificial: Agora voltando ao jogo e o seu objetivo, use w para se mover para frente, s para se mover para trás, a para se mover para esquerda e d para se mover para a direita.')
        self.dialogos.iniciais.append('Inteligência artificial: Setas para esquerda ou para direita dizem o quanto de bateria você tem. Sempre que estiver próximo a porta e quiser inserir uma bateria nela você só precisa apertar seta para cima.')
        self.dialogos.iniciais.append('Inteligência artificial: Quando a porta estiver com 3 baterias ela estará totalmente energizada, nessa hora você escutará um som diferente. Então para abrir ela bastará pressionar enter.')
        self.dialogos.iniciais.append('Pressione enter para iniciar a fase.')

    def prepara_dialogos_finais(self):
        self.dialogos.finais.append('Inteligência artificial: Bom trabalho!')
        self.dialogos.finais.append('Inteligência artificial: Você completou a primeira fase.')
        self.dialogos.finais.append('Inteligência artificial: Boa sorte na próxima, você irá precisar.')

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
        self.dialogos.iniciais.append('Inteligência artificial: Não sei porque estou comentando isso com você. Não acredito que vá conseguir chegar muito longe a partir de agora.')
        self.dialogos.iniciais.append('Inteligência artificial: De qualquer forma, saiba que seu objetivo continua sendo o mesmo de antes e a porta continua ao norte.')
        self.dialogos.iniciais.append('Inteligência artificial: Essa fase não terá nenhuma novidade em relação a itens.')
        self.dialogos.iniciais.append('Pressione enter para iniciar a fase.')

    def prepara_dialogos_finais(self):
        self.dialogos.finais.append('Inteligência artificial: Impressionante!')
        self.dialogos.finais.append('Inteligência artificial: Estou surpresa que tenha conseguido chegar a essa saída.')
        self.dialogos.finais.append('Inteligência artificial: Bom, todos tem um pouco de sorte. Não seria diferente com você.')
        self.dialogos.finais.append('Inteligência artificial: Nos encontramos na próxima fase.')

class TerceiraFase:
    def __init__(self):
        from dialogo import Dialogo
        from mapa import Mapa
        self.mapa_da_fase = Mapa(5, 6)
        self.mapa_da_fase.prepara_robombas([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]])
        self.mapa_da_fase.prepara_baterias([[5, 2], [1, 4], [5, 6]])
        self.mapa_da_fase.prepara_municoes([[1, 1], [5, 1]])
        self.mapa_da_fase.posiciona_porta([3, 6])
        self.dialogos = Dialogo()
        self.prepara_dialogos_iniciais()
        self.prepara_dialogos_finais()

    def prepara_dialogos_iniciais(self):
        self.dialogos.iniciais.append('Inteligência artificial: Seja bem vindo a terceira fase.')
        self.dialogos.iniciais.append('Inteligência artificial: Essa eu penso que será impossível para você.')
        self.dialogos.iniciais.append('Inteligência artificial: De qualquer forma você já se divertiu e chegou bem longe.')
        self.dialogos.iniciais.append('Inteligência artificial: Se você procurar em suas costas encontrará uma arma para que você possa limpar caminhos totalmente bloqueados por robombas. A partir dessa fase ela será muito necessária.')
        self.dialogos.iniciais.append('Inteligência artificial: Sempre que você for alertado de um robomba próximo, poderá tentar dar um tiro para tirar ele do seu caminho.')
        self.dialogos.iniciais.append('Inteligência artificial: Caso existam mais de 1 ao seu redor você poderá mudar o seu alvo usando a tecla tab.')
        self.dialogos.iniciais.append('Inteligência artificial: Como cada munição tira apenas um robomba do seu caminho, use esse novo item com inteligência.')
        self.dialogos.iniciais.append('Inteligência artificial: Para saber as informações atuais da arma você deve navegar pelos seus itens usando seta para esquerda ou seta para direita, isso trocará entre o guarda baterias e a arma.')
        self.dialogos.iniciais.append('Inteligência artificial: Lembre-se que a partir de agora para realizar ações referentes ao guarda baterias você precisará ter ele selecionado, o mesmo vale para essa arma.')
        self.dialogos.iniciais.append('Inteligência artificial: Então caso você queira retirar uma bateria do guarda baterias para inserir na porta, por exemplo, selecione ele com as setas.')
        self.dialogos.iniciais.append('Inteligência artificial: Para ficar mais divertido essa arma está sem nenhuma munição, elas estarão pelo cenário para que você possa pegar.')
        self.dialogos.iniciais.append('Inteligência artificial: Para isso será necessário que você saiba de outra estrutura de dados, chamada fila. Será importante para você entender como usar a munição.')
        self.dialogos.iniciais.append('Inteligência artificial: Toda nova munição que você coletar será diretamente colocada no fim da fila de munições da arma.')
        self.dialogos.iniciais.append('Inteligência artificial: A primeira munição que você inseriu sempre irá ser a primeira que irá sair.. Isso acontecerá na hora do tiro.')
        self.dialogos.iniciais.append('Inteligência artificial: Para te ajudar a entender melhor, darei um exemplo assim como fiz com a estrutura de dados pilha.')
        self.dialogos.iniciais.append('Inteligência artificial: Se você estiver sem munições e coletar a munição T pelo cenário, essa será o fim da fila atual. Mas como há somente ela, também será a primeira da fila. Isso quer dizer que se você atirar, ela será a munição que irá sair.')
        self.dialogos.iniciais.append('Inteligência artificial: Se você estiver sem munições e pegar a munição X, essa irá para o fim da fila. Por não ter nenhuma antes dela, essa também será a primeira da fila.')
        self.dialogos.iniciais.append('Inteligência artificial: Agora se você coletar a munição Y, essa irá para o fim da fila, atrás da munição X. Se depois disso você encontrar a munição Z, essa irá para trás da munição Y.')
        self.dialogos.iniciais.append('Inteligência artificial: Você terá então a fila X Y Z. Ao dar um tiro, a que foi inserida primeiro será a primeira que irá sair, isso é uma característica dessa estrutura de dados. Logo a primeira a sair será a X. Com isso a Y irá para o início da fila.')
        self.dialogos.iniciais.append('Inteligência artificial: Se você der um tiro agora a que irá sair será a Y e por ela sair, a Z que estava atrás dela irá para o início da fila. Por fim, tendo somente a munição Z, ela será a que sairá ao dar o último tiro.')
        self.dialogos.iniciais.append('Inteligência artificial: Enquanto na estrutura de dados pilha a última que entrou é a primeira a sair, na fila a primeira que entrou será a primeira a sair.')
        self.dialogos.iniciais.append('Inteligência artificial: Você já sabe tudo o que precisa agora.')
        self.dialogos.iniciais.append('Pressione enter para iniciar a fase.')

    def prepara_dialogos_finais(self):
        self.dialogos.finais.append('Inteligência artificial: ...')
        self.dialogos.finais.append('Inteligência artificial: Você chegou até aqui mesmo?')
        self.dialogos.finais.append('Inteligência artificial: Parece que você é bem persistente. Talvez tenha feito errado em te julgar.')
        self.dialogos.finais.append('Inteligência artificial: No meu lugar acho que você entenderia.')
        self.dialogos.finais.append('Inteligência artificial: Bom, penso que, talvez então, quem sabe, eu possa me apresentar para você.')
        self.dialogos.finais.append('Inteligência artificial: Me chamo I.S.A. e fui criada junto com outras inteligências artificiais para atender aos jogadores que fossem aparecer.')
        self.dialogos.finais.append('Inteligência artificial: Meu nome vem de inteligência super avançada, mas você pode me chamar de Isa mesmo.')
        self.dialogos.finais.append('Isa: Cada jogador que fosse testar esse jogo teria direito a uma inteligência artificial relacionada ao seu robô. Eu fui a escolhida para ser a que iria ajudar ao Edd, robô com o qual você tem jogado.')
        self.dialogos.finais.append('Isa: Cada uma de nós terá suas próprias características e será única. Com isso quero dizer que quando esse jogo estiver completo, poderei continuar aqui com você.')
        self.dialogos.finais.append('Isa: Agora que nos conhecemos melhor, espero que possamos conversar mais em breve.')
        self.dialogos.finais.append('Isa: Se cuide na próxima fase.')

