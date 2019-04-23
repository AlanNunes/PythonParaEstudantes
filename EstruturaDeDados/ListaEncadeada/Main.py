from Elemento import Elemento
from No import No
from Lista import Lista

lista = Lista()
while True:
    valor = int(input('Digite um valor inteiro, ou -1 para sair.'))
    if valor == -1:
        break
    e = Elemento(valor)
    no = No(e)
    lista.insereNoFim(no)
print(lista.retornaLista())
