class Restaurante:

    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} {self.categoria} {self.ativo}'
    
    def listar(self):
        for restaurante in self.restaurantes:
            print(restaurante)

restaurante1 = Restaurante('restaurante1', 'japonesa')
restaurante2 = Restaurante('restaurante2', 'italiana')
restaurante1.listar()