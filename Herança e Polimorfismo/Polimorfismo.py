# Herança é quando se herda características e métodos de uma classe
# Polimorfismo é o mesmo de herança porém ele altera as características e
# métodos herdados, o próprio nome 'polimorfismo' já é explicativo

# Exemplo de Polimorfismo

class Bebida:
    def __init__(self, sabor, capacidade, preco):
        self.sabor = sabor
        self.capacidade = preco
        self.preco = preco
    def detalhe(self):
        print('Faz bem para a saúde!')

class Suco(Bebida):
    def __init__(self, sabor, capacidade, preco):
        Bebida.__init__(self, sabor, capacidade, preco)

class Refrigerante(Bebida):
    def __init__(self, sabor, capacidade, preco):
        Bebida.__init__(self, sabor, capacidade, preco)
    # Aqui ocorre polimorfismo pois alteramos o método que foi herdado
    def detalhe(self):
        print('Faz mal para a saúde!')


delValle = Suco('morango', '1L', 5.59)
cocaCola = Refrigerante('cola', '2L', 5.59)
# As mensagens que aperecerão devem ser diferentes, pois foi feito polimorfismo
delValle.detalhe()
cocaCola.detalhe()

# Vídeo explicativo: https://www.youtube.com/watch?v=WpxagxS2trU&t=681s&index=2&list=PLDrVHdiJ4rLHeDWVHbFARCfKLPc3mEXQR
