def apresentacao(greet="Bem-vindo!"):
    '''
    -> Função com finalidade de mostrar uma mensagem de boas vindas.
    :param greet: string com a mensagem desejada de boas vindas. Valor padrão: "Bem-vindo!"
    :return: nulo
    '''
    print("*" * (6+len(greet)))
    print("***"+greet+"***")
    print("*" * (6+len(greet)))

def carrega_palavra_secreta(source="palavras.txt"):
    '''
    -> Função responsável por carregar a partir de um arquivo - que por padrão é o "palavras.txt" - uma única palavra de maneira aleatória.
    :param source: arquivo de origem para a extração de palavras. Valor padrão: "palavras.txt"
    :return: uma string contendo a palavra sorteada em letras minúsculas.
    '''
    arquivo = open(source,"r")
    palavras_arquivo = []
    for linha in arquivo:
        palavras_arquivo.append(linha.strip())
    arquivo.close()
    from random import randrange
    palavra_selecionada = palavras_arquivo[randrange(0,len(palavras_arquivo)-1)].lower()
    return palavra_selecionada

def palpite_jogador(chutes):
    '''
    -> Função responsável por fazer a verificação do palpite do jogador, evitando entradas inválidas como:
        - letras já inseridas pelo usuário
        - espaços em branco
        - números
        - mais de uma letra
    :param chutes: lista contendo as letras inseridas anteriormente pelo jogador.
    :return: uma única letra
    '''
    while True:
        letra = input("Insira uma letra: ").lower().strip()
        if(chutes.count(letra) != 0):
            print(f"A letra {letra} já foi inserida! Digite uma nova letra.")
        elif(letra.isalnum() and len(letra) == 1 and not letra.isnumeric()):
            break
        else:
            print(f"Sua entrada [{letra}] é inválida! TENTE NOVAMENTE!")
    return letra

def mostrar_letras(palavra):
    '''
    -> Função dedicada para exibir quais letras foram inseridas pelo usuário ao longo do jogo.
    :param palavra: a lista contendo todas as letras já inseridas pelo usuário.
    :return: nulo.
    '''
    print("Letras inseridas até o momento: ", end="") 
    for letra in palavra:
        print(letra, end=" ")
    print()

def marca_chute_correto(letra,palavra_secreta,palavra_jogador):
    '''
    -> Função dedicada para atualizar a palavra do jogador conforme ele for adivinhando as letras da palavra secreta.
        - a função exibe ainda em qual índice (ou índices, se a letra aparecer mais de uma vez) a letra se encontra.
    :param letra: a letra inserida pelo usuário.
    :param palavra_secreta: a palavra que o usuário está tentando adivinhar.   
    :param palavra_jogador: a lista de letras que contêm as letras já acertadas pelo jogador. Letras não conhecidas são indicadas por "_".
    :return: nulo. A função somente atualiza o parâmetro palavra_jogador e realiza prints.
    '''
    index = 0
    for l in palavra_secreta:
        if(l == letra):
            print(f"A palavra secreta contém a letra {letra} na posição {index}")
            palavra_jogador[index] = letra
        index += 1

def desenha_forca(erros,chances):
    '''
    -> Função designada para desenhar a figura do enforcado de acordo com o número de erros.
        Ela também é responsável por exibir o número de chances restantes ao jogador.
    :param erros: recebe o número de erros cometidos pelo usuário até o presente momento.
    :param chances: recebe o número máximo de erros que o usuário pode cometer. Para fins do desenho do enforcado, o número padrão de chances é 7.
    :return: nulo.
    '''
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print(f"Restam {chances-erros} chances para errar.")
    print("*********************************")

#   PROGRAMA PRINCIPAL:
def jogar():
    '''
    -> Concentra toda a lógica do jogo da forca. O jogo será exibido no terminal e pode tanto ser chamado como uma função quanto jogado ao rodarmos este arquivo.
    '''
    apresentacao("Bem vindo ao jogo da Forca!")
    palavra_secreta = carrega_palavra_secreta() 
    palavra_jogador = list("_" for letra in palavra_secreta)
    erros = 0
    chances = 7
    tentativa = 1
    chutes = []

    print(f"Você possui {chances} chances para errar! Se seus palpites acabarem, você perde!")
    print("Boa sorte!\n")
    while erros < chances:
        print(f"Tentativa {tentativa}")
        letra = palpite_jogador(chutes)
        chutes.append(letra)
        mostrar_letras(chutes)
        
        if(letra not in palavra_secreta): #Outra possível solução: palavra_secreta.find(letra) == -1
            print(f"A letra {letra} não está presente na palavra!")
            erros +=1
        else:
            marca_chute_correto(letra,palavra_secreta,palavra_jogador)

        palavra_final = "".join(palavra_jogador)
        print(f"A palavra que temos até o momento é: {palavra_final}")
        desenha_forca(erros, chances)
        if(palavra_secreta == palavra_final):
            print(f"PARABÉNS! VOCÊ ADIVINHOU A PALAVRA SECRETA: {palavra_secreta}")
            break
        tentativa += 1
    
    if(erros >= chances):
        print(f"ACABARAM-SE OS PALPITES. Uma pena! A palavra secreta era: {palavra_secreta}")
    print("Fim do jogo")

#   SE O 'forca.py' NÃO ESTIVER SENDO IMPORTADO PARA OUTRO PROGRAMA, ELE IRÁ RODAR POR PADRÃO A FUNÇÃO 'jogar()'
if(__name__ == "__main__"):
    jogar()