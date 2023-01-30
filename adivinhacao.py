def apresentacao(greet="Bem-vindo!"):
    '''
    -> Função com finalidade de mostrar uma mensagem de boas vindas.
    :param greet: string com a mensagem desejada de boas vindas. Valor padrão: "Bem-vindo!"
    :return: nulo
    '''
    print("*" * (6+len(greet)))
    print("***"+greet+"***")
    print("*" * (6+len(greet)))

def selecionar_dificuldade():
    '''
    -> Função responsável por determinar o número de tentativas disponíveis para o jogador. Existem três opções de dificuldade:
        - (1) Fácil: 20 tentativas
        - (2) Médio: 10 tentativas
        - (3) Difícil: 5 tentativas
        Esta função também garante que o input seja um int válido dentre as opções possíveis (1, 2 ou 3).
    :return: o número de tentativas para a variável de controle dentro da nossa função jogar().
    '''
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    
    while True:
        try:
            nivel = int(input("Defina o nível: "))
        except:
            print("ENTRADA INVÁLIDA. Tente novamente!")
        else:
            if 0 < nivel < 4:
                break
            else:
                print("Este nível não existe. Insira o número correspondente a dificuldade desejada!")

    if(nivel == 1):
        return 20
    elif(nivel == 2):
        return 10
    elif(nivel == 3):
        return 5

def chutar():
    '''
    -> Função responsável por atualizar a variável 'chute', que recebe o palpite do usuário. Ela garante que:
        - a entrada seja um int 
        - a entrada esteja entre 0 e 100
    :return: entrada válida (um inteiro entre 0 e 100).
    '''
    while True:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))
            if(1 <= chute and chute < 100):
                print("Você digitou {}".format(chute))
                return chute
            else:    
                print("Você deve digitar um número entre 1 e 100!")
        except:
            print("HOUVE UM ERRO NA ENTRADA. Tente novamente!")

def calcula_pontos(pontos,numero_secreto,chute):
    '''
    -> Realiza o cálculo de pontuação do jogador. A pontuação do jogador é calculada do seguinte modo:
        - o jogador inicia a partida com 1000 pontos.
        - a cada erro, o jogador perde um número de pontos equivalente a diferença (valor absoluto) entre o chute inserido e o número secreto.
        - portanto, quanto maior a pontuação final, melhor o desempenho do jogador.
    :param pontos: a pontuação inicial do jogador, antes do cálculo.
    :param numero_secreto: o número que o jogador está tentando adivinhar.
    :param chute: o número que o jogador palpitou como número secreto.
    :return: a pontuação após o cálculo.
    '''
    return pontos - abs(numero_secreto - chute)

def jogar():
    '''
    -> Concentra toda a lógica do jogo de advinhação. O jogo será exibido no terminal e pode tanto ser chamado como uma função quanto jogado ao rodarmos este arquivo.
    '''
    from random import randrange

    apresentacao("Bem vindo ao jogo de Adivinhação!")

    numero_secreto = randrange(1,101)
    total_de_tentativas = selecionar_dificuldade()
    pontos = 1000
    
    for rodada in range(1, total_de_tentativas + 1):
        print("~"*20)
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = chutar()

        if(chute == numero_secreto):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(chute > numero_secreto):
                print("O seu chute foi maior do que o número secreto.")
            elif(chute < numero_secreto):
                print("O seu chute foi menor do que o número secreto.")
            pontos = calcula_pontos(pontos,numero_secreto,chute)

    print()
    if(chute != numero_secreto):
        print("Que pena, você não conseguiu adivinhar o número secreto, que era {}".format(numero_secreto))
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
