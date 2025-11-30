class Musica:
    def __init__(self, nome: str, artista: str, duracao: int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome}'
    
musica1 = Musica('musica1', 'belo', '2')
print(musica1)
    