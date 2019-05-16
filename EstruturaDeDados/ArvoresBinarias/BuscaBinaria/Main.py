from Elemento import Elemento
from No import No
from ArvoreBuscaBinaria import ArvoreBuscaBinaria
import os
import msvcrt as m

def menu():
    os.system('cls')
    print('1 - inserir \n')
    print('2 - remover \n')
    print('3 - pré ordem \n')
    print('4 - em ordem \n')
    print('5 - Busca valor \n')
    print('6 - Conta quantos nós existem na árvore \n')
    print('7 - Conta a altura de um nó \n')
    print('0 - termina \n')
    opcao = int(input('Digite uma opção: '))
    return opcao

arvoreBinaria = ArvoreBuscaBinaria()
opcao = 1
while opcao != 0:
    if opcao == 1:
        valor = int(input('Digite um valor: '))
        arvoreBinaria.insereNo(valor)
    elif opcao == 2:
        valor = int(input('Digite um valor: '))
        arvoreBinaria.remove(valor)
    elif opcao == 3:
        arvoreBinaria.preOrdem(arvoreBinaria.getRaiz())
        m.getch() #Espera o usuário teclar algo
    elif opcao == 4:
        arvoreBinaria.emOrdem(arvoreBinaria.getRaiz())
        m.getch() #Espera o usuário teclar algo
    elif opcao == 5:
        valor = int(input('Digite um valor: '))
        resultado = arvoreBinaria.buscaValor(arvoreBinaria.getRaiz(), valor)
        print(resultado)
        m.getch() #Espera o usuário teclar algo
    elif opcao == 6:
        resultado = arvoreBinaria.getQuantidadeNos(arvoreBinaria.getRaiz())
        print(resultado)
        m.getch() #Espera o usuário teclar algo
    elif opcao == 7:
        valor = int(input('Digite um valor: '))
        resultado = arvoreBinaria.alturaNo(arvoreBinaria.getRaiz(), valor)
        print(resultado)
        m.getch() #Espera o usuário teclar algo
    opcao = menu()
