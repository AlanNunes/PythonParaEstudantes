from No import No
class Lista:
    def __init__(self):
        self._cabeca = No(None)
    def getCabeca(self):
        return self._cabeca
    def setCabeca(self, c):
        self._cabeca = c
    def listaVazia(self):
        return self._cabeca.getProximo() == None
    def insereNoInicio(self, n):
        n.setProximo(self._cabeca.getProximo())
        self._cabeca.setProximo(n)
    def insereNoFim(self, n):
        if not self.listaVazia():
            lst = []
            atual = self._cabeca
            while atual.getProximo() != None:
                atual = atual.getProximo()
            atual.setProximo(n)
        else:
            self._cabeca.setProximo(n)
    def retiraNoInicio(self):
        if not self.listaVazia():
            atual = self._cabeca.getProximo()
            self._cabeca.setProximo(atual.getProximo())
            return atual
    def retornaLista(self):
        if not self.listaVazia():
            lst = []
            atual = self._cabeca.getProximo()
            while atual != None:
                lst.append(atual.getElemento().getValor())
                atual = atual.getProximo()
            return lst
        else:
            return None
