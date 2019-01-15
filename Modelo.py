class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return (f'Nome: {self.nome}  Likes: {self.likes}')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return (f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}')


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return (f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}')

class Playlist:

    def __init__(self,nome,programas):
        self.nome = nome
        #super().__init__(programas)
        self.__programas = programas

    @property
    def listagem(self):
        return self.__programas

    @property
    def tamanho(self):
        return len(self.__programas)

    def __getitem__(self,item):
        return self.__programas[item]

    def __len__(self):
        return len(self.__programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

demolidor = Serie('Demolidor',2016,2)


vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes_e_series =  [vingadores,atlanta,demolidor]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)


for programa in filmes_e_series:
    print(programa)
