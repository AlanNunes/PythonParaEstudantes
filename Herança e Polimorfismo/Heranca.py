# Herança é quando se herda características e métodos de uma classe
# Polimorfismo é o mesmo de herança porém ele altera as características e
# métodos herdados, o próprio nome 'polimorfismo' já é explicativo

# Exemplo de Herança
class Bebida:
    def __init__(self, sabor, capacidade, preco):
        self.sabor = sabor
        self.capacidade = preco
        self.preco = preco

class Suco(Bebida):
    def __init__(self, sabor, capacidade, preco):
        Bebida.__init__(self, sabor, capacidade, preco)

class Refrigerante(Bebida):
    def __init__(self, sabor, capacidade, preco):
        Bebida.__init__(self, sabor, capacidade, preco)


delValle = Suco('morango', '1L', 5.59)
cocaCola = Refrigerante('Cola', '2L', 5.50)

print(delValle.sabor)
print(cocaCola.sabor)

# Vídeo explicativo: https://www.youtube.com/watch?v=WpxagxS2trU&t=681s&index=2&list=PLDrVHdiJ4rLHeDWVHbFARCfKLPc3mEXQR
