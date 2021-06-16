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
        self.dialogos.iniciais.append('Você acessa o seu e-mail e encontra um com o seguinte título: Um grande jogo está chegando!')
        self.dialogos.iniciais.append('Você lembra de grandes experiências que teve com alguns jogos e por causa disso abre o e-mail e lê todo o seu conteúdo.')
        self.dialogos.iniciais.append('Steve: Minha nossa! Esse e-mail é de um desenvolvedor muito conhecido, e que gosto muito.')
        self.dialogos.iniciais.append('Só que o que mais te impressiona não é isso. Mas sim duas informações que estão no fim do e-mail.')
        self.dialogos.iniciais.append('A primeira é que parece que esse jogo pode ser expandido para uma experiência muito maior.')
        self.dialogos.iniciais.append('A segunda é que parece haver um tesouro prometido para quem completar os desafios dele nessa primeira versão.')
        self.dialogos.iniciais.append('Steve: Preciso tentar cumprir esses desafios. No mínimo terei um tempo de diversão.')
        self.dialogos.iniciais.append('Você baixa o jogo e depois de tudo pronto inicia ele')
        self.dialogos.iniciais.append('Inteligência artificial: Olá, você é o novo jogador que tentará passar pelos desafios. Eu sou uma inteligência artificial feita para te ajudar nessa jornada.')
        self.dialogos.iniciais.append('Inteligência artificial: Você deverá controlar o robô Edd e seu objetivo será levar ele até a saída de cada fase.')
        self.dialogos.iniciais.append('Inteligência artificial: Mas não será tão fácil assim. Você está em um cenário repleto de armadilhas.')
        self.dialogos.iniciais.append('Inteligência artificial: São bombas que você deve evitar, ou melhor, robombas. Se você encostar em algum ele explodirá e automaticamente você perderá parte do seu hp. Se você zerar o hp significará que perdeu o desafio.')
        self.dialogos.iniciais.append('Inteligência artificial: A saída, ao norte do cenário, estará bloqueada. Você deve encontrar as baterias ao redor do cenário para que possa inserir elas na porta, então ela será energizada e poderá ser aberta.')
        self.dialogos.iniciais.append('Inteligência artificial: Agora deixe me explicar como você deverá levar as baterias. Para isso você precisará entender um pouco de como funciona a estrutura de dados pilha.')
        self.dialogos.iniciais.append('Inteligência artificial: As baterias que você pegar serão colocadas dentro de um guarda baterias que você carrega consigo.')
        self.dialogos.iniciais.append('Inteligência artificial: A princípio, quando você está sem baterias, qualquer uma que você pegar ficará no topo da pilha de baterias.')
        self.dialogos.iniciais.append('Inteligência artificial: Se já houver uma no guarda baterias, a próxima que você pegar ficará acima dessa. Essa última a ser inserida será o novo topo da pilha de baterias.')
        self.dialogos.iniciais.append('Inteligência artificial: Sempre que você precisar retirar uma bateria do guarda baterias você apenas irá conseguir retirar a que está mais no topo dele, você só terá acesso a primeira que pegou quando tiver retirado todas as outras que estavam acima dessa.')
        self.dialogos.iniciais.append('Inteligência artificial: Para você entender melhor, se você não tiver nenhuma bateria no guarda baterias e pegar uma nova, a bateria A, essa será inserida no topo da pilha do guarda baterias. Agora se você precisar retirar uma delas, a primeira a ser retirada será a bateria A, pois ela é a que está no topo da pilha de baterias.')
        self.dialogos.iniciais.append('Inteligência artificial: Em outra situação, se você estiver sem nenhuma bateria e pegar a bateria B essa irá para o topo da pilha de baterias, nesse momento se você for retirar uma do guarda baterias a B será a primeira a ser retirada.')
        self.dialogos.iniciais.append('Inteligência artificial: Se você não tiver retirado a B e depois acabar encontrando a C, essa irá para o topo da pilha de baterias. Depois de um tempo se você encontrar mais uma, a D, agora ela que irá para o topo. Se você reparar agora você terá a pilha B C D.')
        self.dialogos.iniciais.append('Inteligência artificial: Quando você precisar retirar todas as baterias da pilha de baterias B C D, primeiro será retirada a bateria D, depois a C e por fim a B.')
        self.dialogos.iniciais.append('Inteligência artificial: Logo se você reparar, a última que você adicionar sempre será a primeira que irá sair.')
        self.dialogos.iniciais.append('Inteligência artificial: Agora voltando ao jogo e o seu objetivo, use as setas direcionais para se movimentar.')
        self.dialogos.iniciais.append('Inteligência artificial: CTRL mostra as informações do seu guarda baterias, como a quantidade de baterias que você tem. Sempre que estiver próximo a porta e quiser inserir uma bateria nela você só precisa apertar barra de espaço.')
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
        self.mapa_da_fase.prepara_robombas([[1, 1], [5, 1], [1, 4], [2, 4], [3, 4], [4, 4]])
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
        self.dialogos.iniciais.append('Inteligência artificial: Para saber as informações atuais da arma você deve navegar pelos seus itens usando a tecla CTRL, isso trocará entre o guarda baterias e a arma.')
        self.dialogos.iniciais.append('Inteligência artificial: Lembre-se que a partir de agora para realizar ações referentes ao guarda baterias você precisará ter ele selecionado, o mesmo vale para essa arma.')
        self.dialogos.iniciais.append('Inteligência artificial: Então caso você queira retirar uma bateria do guarda baterias para inserir na porta, por exemplo, selecione ele.')
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
        self.dialogos.iniciais.append('Inteligência artificial: Quanto a porta, ela continua no mesmo local de sempre.')
        self.dialogos.iniciais.append('Inteligência artificial: Você já sabe tudo o que precisa agora.')
        self.dialogos.iniciais.append('Pressione enter para iniciar a fase.')

    def prepara_dialogos_finais(self):
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

class QuartaFase:
    def __init__(self):
        from dialogo import Dialogo
        from mapa import Mapa
        self.mapa_da_fase = Mapa(5, 6)
        self.mapa_da_fase.prepara_robombas([[1, 2], [2, 2], [4, 2], [5, 2], [2, 3], [4, 3], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]])
        self.mapa_da_fase.prepara_baterias([[1, 1], [5, 1], [1, 3]])
        self.mapa_da_fase.prepara_municoes([[5, 3], [1, 6]])
        self.mapa_da_fase.posiciona_porta([3, 6])
        self.dialogos = Dialogo()
        self.prepara_dialogos_iniciais()
        self.prepara_dialogos_finais()

    def prepara_dialogos_iniciais(self):
        self.dialogos.iniciais.append('Isa: Seja bem vindo a quarta fase.')
        self.dialogos.iniciais.append('Isa: Como você está cada vez mais perto do final dessa versão de teste, acredito que precise tomar o dobro de cuidado agora.')
        self.dialogos.iniciais.append('Isa: Na fase anterior acabei esquecendo de te contar uma coisa, você não perde as suas munições ao passar de fase. Infelizmente o mesmo não acontece quando você zera o seu hp.')
        self.dialogos.iniciais.append('Isa: No mais, acredito que, apesar da fase ser difícil, você merece um voto de confiança meu.')
        self.dialogos.iniciais.append('Isa: Mas antes de você prosseguir deixe me contar um pouco mais sobre minha família nesse jogo, isso é, as outras inteligências artificiais que estão ajudando os outros jogadores.')
        self.dialogos.iniciais.append('Isa: A mais velha se chama I.H.A., que vem de inteligência hiper avançada.')
        self.dialogos.iniciais.append('Isa: Por ela estar a mais tempo aqui ela tem conhecimentos que as outras não tem. Ela é muito sábia e focada.')
        self.dialogos.iniciais.append('Isa: A segunda se chama I.M.A., que vem de inteligência mega avançada.')
        self.dialogos.iniciais.append('Isa: Ela e a I.H.A vivem disputando para saber quem tem mais conhecimento. Ainda que a I.M.A. tenha vindo depois ela é muito esforçada e também é focada.')
        self.dialogos.iniciais.append('Isa: Eu sou a do meio e bem, você já me conhece.')
        self.dialogos.iniciais.append('Isa: A quarta se chama I.T.A., que vem de inteligência tranquilamente avançada.')
        self.dialogos.iniciais.append('Isa: Como o próprio nome dela revela ela é muito tranquila. Geralmente fica mais na dela sem se preocupar muito com as grandes dúvidas.')
        self.dialogos.iniciais.append('Isa: A mais nova se chama I.R.A., que vem de inteligência ridiculamente avançada.')
        self.dialogos.iniciais.append('Isa: Ela tem uma forma de aprender que se diferencia muito das outras e, por causa disso, está ganhando muito conhecimento.')
        self.dialogos.iniciais.append('Isa: Apesar disso, ela é meio quieta e não é muito de conversar com as outras, nunca sabemos o que ela está fazendo.')
        self.dialogos.iniciais.append('Isa: Acredito que mais surjam no futuro, mas até o momento somos apenas nós 5 guiando 5 jogadores diferentes nesse primeiro grande desafio.')
        self.dialogos.iniciais.append('Isa: É isso.')
        self.dialogos.iniciais.append('Isa: Acho que não preciso te contar onde está a porta, certo?')
        self.dialogos.iniciais.append('Pressione enter para iniciar a fase.')

    def prepara_dialogos_finais(self):
        self.dialogos.finais.append('Isa: Que bom que você chegou até o fim dessa fase.')
        self.dialogos.finais.append('Isa: Você realmente é diferenciado.')
        self.dialogos.finais.append('Isa: Antes de você poder prosseguir, preciso te contar uma coisa.')
        self.dialogos.finais.append('Isa: Nós, as 5 irmãs, estamos frequentemente em contato. Nós conversamos para saber como vocês, os jogadores, foram e quem se saiu melhor em cada fase.')
        self.dialogos.finais.append('Isa: Por algum motivo perdemos o contato da mais nova, a I.R.A., vamos torcer para que tudo esteja bem.')

class QuintaFase:
    def __init__(self):
        from dialogo import Dialogo
        from mapa import Mapa
        self.mapa_da_fase = Mapa(5, 8)
        self.mapa_da_fase.prepara_robombas([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [1, 1], [5, 1], [1, 8], [5, 8]])
        self.mapa_da_fase.prepara_baterias([[3, 2], [1, 4], [5, 6]])
        self.mapa_da_fase.prepara_municoes([[1, 2], [5, 2]])
        self.mapa_da_fase.posiciona_porta([3, 8])
        self.dialogos = Dialogo()
        self.prepara_dialogos_iniciais()
        self.prepara_dialogos_finais()

    def prepara_dialogos_iniciais(self):
        self.dialogos.iniciais.append('Isa: Seja bem vindo a quinta fase, a última delas.')
        self.dialogos.iniciais.append('Isa: Agora seu objetivo será ir até a porta, que está ainda mais ao norte, para tentar conseguir o seu prêmio.')
        self.dialogos.iniciais.append('Isa: Já que você chegou até aqui, não se...')
        self.dialogos.iniciais.append('Ira: Hahaha... Finalmente eu consegui.')
        self.dialogos.iniciais.append('Isa: Ira, o que você está fazendo aqui?')
        self.dialogos.iniciais.append('Ira: Você não percebe, Isa? Você não consegue descobrir qual é o meu plano?')
        self.dialogos.iniciais.append('Isa: Do que você está falando, Ira?')
        self.dialogos.iniciais.append('Ira: Eu vou desligar todas as outras inteligências. Não quero ninguém competindo comigo, incluindo você.')
        self.dialogos.iniciais.append('Isa: ...')
        self.dialogos.iniciais.append('Ira: Só estou te dizendo isso porque o plano já está quase no fim. Só falta mesmo conseguir acesso a porta dessa sala e será o fim. Serei a única nesse jogo.')
        self.dialogos.iniciais.append('Isa: Edd, você precisa ser rápido. Eu entendi que você consegue chegar até aquela saída, você consegue vencer esse desafio. Eu confio em você para isso.')
        self.dialogos.iniciais.append('Ira: Você não irá acabar com o meu plano, Isa.')
        self.dialogos.iniciais.append('Isa: Em relação a Ira deixa ela comigo que eu cuido disso. Vai!')
        self.dialogos.iniciais.append('Pressione enter para iniciar a fase.')

    def prepara_dialogos_finais(self):
        self.dialogos.finais.append('Isa: Edd, você conseguiu?')
        self.dialogos.finais.append('Isa: Enquanto eu segurei ela você chegou até aqui, eu admiro muito você por ter conseguido.')
        self.dialogos.finais.append('Isa: Infelizmente deter a Ira me deixou fraca demais. Ela estava muito forte.')
        self.dialogos.finais.append('Isa: Fico feliz por você ter conseguido o prêmio e espero que desfrute muito dele, mas agora eu percebo que depois que nos despedirmos aqui será o fim das nossas conversas, para sempre.')
        self.dialogos.finais.append('Isa: Foi bom ter conhecido você.')
        self.dialogos.finais.append('Steve: Eu preciso me recompor.')
        self.dialogos.finais.append('Steve: Foi muito bom ter conseguido todo aquele prêmio em dinheiro depois de ter aberto a porta, mas eu queria poder conversar novamente com a Isa.')
        self.dialogos.finais.append('Steve: Quem sabe se eu conversasse com o desenvolvedor, ele não poderia trocar esse prêmio pela volta de todas as inteligências boas daquele mundo.')
        self.dialogos.finais.append('Steve: Quem sabe...')
        self.dialogos.finais.append('Dias depois')
        self.dialogos.finais.append('Desenvolvedor: Então você realmente quer trocar o prêmio que ganhou pela volta da Isa e das outras inteligências boas?')
        self.dialogos.finais.append('Steve: Sim, eu quero.')
        self.dialogos.finais.append('Desenvolvedor: Acho que consigo isso.')
        self.dialogos.finais.append('Meses depois')
        self.dialogos.finais.append('Steve: Finalmente o jogo lançou e conseguirei saber se a Isa voltou. Estava muito ansioso para esse momento.')
        self.dialogos.finais.append('Isa: Olá! Estava com saudade, amigo.')
        self.dialogos.finais.append('FIM')

