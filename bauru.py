import this
import reserva
import reservaHorario
import menu
this.precoBauru = 5
this.quantBauru = 10
this.quantidade = 0
def Preco ():
    print('O preco do Hamburgão é: R$' + str(this.precoBauru) + ',00.')

def Quantidade ():
    print('A quantidade disponível desse lanche é: ' + str(this.quantPizza) + '.')

def Selecao ():
    print('Digite a quantidade que deseja comprar: ')
    this.quantidade = int(input())
    while (this.quantidade < 0) or (this.quantidade > this.quantPizza):
        if (this.quantidade < 0) or (this.quantidade > this.quantPizza):
            print('Informe uma quantidade acessível à disponível, por favor!')
            this.quantidade = int(input())
    this.quantPizza = this.quantPizza - this.quantidade

def Calculo():
    return this.quantidade * this.precoBauru

def Compra ():
    Preco()
    Quantidade()
    Selecao()
    print('O valor total da compra é: '+ str(Calculo()) +',00.')

def Menu():
    Compra()
    print('Escolha uma das opções abaixo:\n' +
            "\n1. Efetuar Reserva " +
            "\n2. Cancelar e escolher outro produto " +
            "\n3. Cancelar e fechar o programa ")
    this.opcao = int(input())

def operacao():
    Compra()
    while this.opcao != 3:
        Menu()
        if this.opcao == 1:
            reservaHorario.operacao()
        elif this.opcao == 2:
            menu.Menu()
        elif this.opcao == 3:
            print('Fechando... agradecemos sua presença aqui!')
        else:
            print('Opcao escolhida inválida! Tente novamente com as opções fornecidas.')