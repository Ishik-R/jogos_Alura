import forca
import adivinhacao

def apresentacao(greet="Bem-vindo!"):
    '''
    -> Função com finalidade de mostrar uma mensagem de boas vindas.
    :param greet: string com a mensagem desejada de boas vindas. Valor padrão: "Bem-vindo!"
    :return: nulo
    '''
    print("*" * (6+len(greet)))
    print("***"+greet+"***")
    print("*" * (6+len(greet)))

def escolhe_jogo():
    '''
    -> Concentra o acesso aos jogos disponíveis. Lembrando que:
        - estão disponíveis somente dois jogos: forca e adivinhação. O acesso a futuros jogos depende de modificações na estrutura do programa.
        - os jogos devem ser acessados por meio de seus identificadores: '1' para Forca e '2' para a Adivinhacao
    '''
    apresentacao("Escolha o seu jogo digitando o número desejado!")

    print("(1) Forca")
    print("(2) Adivinhação")
    while True:
        try:
            jogo = int(input("Qual jogo? "))
            print()
        except:
            print("ENTRADA INVÁLIDA! Por favor, tente novamente")
        else:
            if(jogo == 1):
                print("Iniciando: forca")
                forca.jogar()
                break
            elif(jogo == 2):
                print("Iniciando: adivinhação")
                adivinhacao.jogar()
                break
            else:
                print("Insira uma entrada válida!")

if(__name__ == "__main__"):
    escolhe_jogo()
