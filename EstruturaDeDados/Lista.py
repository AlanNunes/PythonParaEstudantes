from No import No
class Lista:
    def __init__(self):
        self._cabeca = No()
    def getCabeca(self):
        return self._cabeca
    def setCabeca(self, c):
        self._cabeca = c
    def listaVazia(self):
        return self._cabeca.getProximo() == None
    def insereNoInicio(self, n):
        n.setProximo(self._cabeca.getProximo())
        self._cabeca.setProximo(n)
    def retiraNoInicio(self):
        if not self.listaVazia():
            atual = self._cabeca.getProximo()
            self._cabeca.setProximo(atual.getProximo())
            return atual
