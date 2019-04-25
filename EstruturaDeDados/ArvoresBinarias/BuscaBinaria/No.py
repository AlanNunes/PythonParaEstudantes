from Elemento import Elemento
class No:
    def __init__(self):
        self._elemento = Elemento(None)
        self.filhoEsquerda = None
        self.filhoDireita = None
    def getFilhoEsquerda(self):
        return self.filhoEsquerda
    def setFilhoEsquerda(self, n):
        self.filhoEsquerda = n
    def setfilhoDireita(self, n):
        self.filhoDireita = n
    def getFilhoDireita(self):
        return self._filhoDireita
    def getElemento(self):
        return self._elemento
    def setElemento(self, e):
        self._elemento = e
