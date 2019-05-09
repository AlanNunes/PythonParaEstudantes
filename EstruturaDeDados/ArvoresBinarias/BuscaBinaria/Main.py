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
    opcao = menu()
