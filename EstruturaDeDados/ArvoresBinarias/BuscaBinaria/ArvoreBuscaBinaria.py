from Elemento import Elemento
from No import No

class ArvoreBuscaBinaria:
    def __init__(self):
        self._raiz = None

    def getRaiz(self):
        return self._raiz

    def setRaiz(self, n):
        self._raiz = n

    def arvoreVazia(self):
        return self._raiz == None

    def criaNo(self, v):#ele deve ser inteiro
        no = No()
        no.getElemento().setValor(v)
        return no

    def insereNo(self, v):
        if self.arvoreVazia():
            self.setRaiz(self.criaNo(v))
        else:
            self.insere(None, self.getRaiz(), v)

    def insere(self, pai, atual, v):
        if(atual != None):
            if(v < atual.getElemento().getValor()):
                self.insere(atual, atual.getFilhoEsquerda(), v)
            else:
                self.insere(atual, atual.getFilhoDireita(), v)
        else:
            x = self.criaNo(v)
            if(v < pai.getElemento().getValor()):
                pai.setFilhoEsquerda(x)
            else:
                pai.setfilhoDireita(x)

    def preOrdem(self, no): #raíz
            if(no != None):
                print(no.getElemento().getValor())
                self.preOrdem(no.getFilhoEsquerda())
                self.preOrdem(no.getFilhoDireita())

    def emOrdem(self, no): #raíz
            if(no != None):
                self.emOrdem(no.getFilhoEsquerda())
                print(no.getElemento().getValor())
                self.emOrdem(no.getFilhoDireita())

    def buscaValor(self, pai, valor):
        if pai != None:
            if pai.getElemento().getValor() == valor:
                return True
            else:
                if valor < pai.getElemento().getValor():
                    return self.buscaValor(pai.getFilhoEsquerda(), valor)
                else:
                    return self.buscaValor(pai.getFilhoDireita(), valor)
        return False 

    # Retorna a quantidade de nós na árvore
    def getQuantidadeNos(self, n):
        if n != None:
            x = self.getQuantidadeNos(n.getFilhoEsquerda())
            y = self.getQuantidadeNos(n.getFilhoDireita())
            return x + y + 1
        return 0
    
    def getAlturaNo(self, n):
        if n != None:
            x = self.getQuantidadeNos(n.getFilhoEsquerda())
            y = self.getQuantidadeNos(n.getFilhoDireita())
            return x + y + 1
        return 0

    def alturaNo(self, n, v):
        if(self.buscaValor(n,v)):
            return self.achaElemento(n, v, 0)
        else:
            return -1  

    def achaElemento(self, n, v, e):
        if n != None:
            if e == 0 and v == n.getElemento().getValor():
                e = 1
            x = self.achaElemento(n.getFilhoEsquerda(), v, e)    
            y = self.achaElemento(n.getFilhoDireita(), v, e)
            return (x if x > y else y) + e
        return 0
    
    def nivelElemento(self, n, v):
        if n != None:
            if v == n.getElemento().getValor():
                return 0
            elif n.getElemento().getValor() > v:
                return self.nivelElemento(n.getFilhoEsquerda(), v) + 1
            else:
                return self.nivelElemento(n.getFilhoDireita(), v) + 1
    def removeArveres(self, n):
        if n != None:
            self.removeArveres(n.getFilhoEsquerda())
            self.removeArveres(n.getFilhoDireita())
            n.setFilhoEsquerda(None)
            n.setfilhoDireita(None)
    def inverteArveres(self, n):
        if n != None:
            self.removeArveres(n.getFilhoEsquerda())
            self.removeArveres(n.getFilhoDireita())
            x = n.getFilhoDireita()
            n.setfilhoDireita(n.getFilhoEsquerda())
            n.setFilhoEsquerda(x.getFilhoDireita())
    def nivelaNivel(self, n):
        f = []
        f.append(a)
        while len(f) > 0:
            n = f.pop(0)
            print(n.getElemento().getValor())
            if n.getFilhoEsquerda() != None:
                f.append(n.getFilhoEsquerda())
            if n.getFilhoDireita() != None:
                f.append(n.getFilhoDireita())
