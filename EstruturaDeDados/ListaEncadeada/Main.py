from Elemento import Elemento
from No import No
from Lista import Lista

l = Lista()
n = int(input('Digite um valor inteiro'))
while n > 0:
    x = n%2
    e = Elemento()
    e.setValor(x)
    no = No()
    no.setElemento(e)
    l.insereNoInicio(no)
    n = int(n/2)
while not l.listaVazia():
    print(l.retiraNoInicio())
