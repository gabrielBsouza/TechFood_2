import this
import hamburgao
import reservaHorario
import menu

def coletar():

    print(str(hamburgao.Quantidade()))

def Menu():
    print('Escolha uma das opções abaixo:\n' +
        "\n1. Efetuar Reserva " +
        "\n2. Cancelar e escolher outro produto " +
        "\n3. Cancelar e fechar o programa ")
    this.opcao = int(input())
def operacao():
    while this.opcao != 3:
        Menu()
        # realizar operações
        if this.opcao == 1:
            reservaHorario.escolhaHorario()
        elif this.opcao == 2:
            menu.Menu()
        elif this.opcao == 3:
            print('Fechando... agradecemos sua presença aqui!')
        else:
            print('Opcao escolhida inválida! Tente novamente com as opções fornecidas.')