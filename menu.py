import this
import hamburgao


this.opcao = 0
def Menu ():
    print('Escolha uma das opções abaixo:\n'+
          '\n1. Hamburgão R$5,00'+
          '\n2. Fechar Programa')
    this.opcao = int(input())

def operacao():
    #Mostrar o menu em tela
    while this.opcao != 2:
        Menu()
        #realizar operações
        if this.opcao == 1:
            #operacao para 1.
            hamburgao.Compra()
        elif this.opcao == 2:
            print('Fechando... agradecemos sua presença aqui!')
        else:

            print('Opcao escolhida inválida! Tente novamente com as opções fornecidas.')



