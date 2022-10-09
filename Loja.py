import datetime as dt

class Loja(object):

    def __init__(self, nome: str, estoque: int):
        if not isinstance(estoque, int):
            raise TypeError(f'\033[0;41mErro - Loja - __init__ - O estoque é do tipo {type(estoque)}. Deve ser do tipo inteiro\033[m')
        self.nome = nome
        self.estoque: int = estoque
    
    def mostra_estoque(self) -> int:
        print(f'[Loja] - [mostra_estoque] - [Estoque atual: {self.estoque}] - [Em {dt.datetime.now()}]')
        return self.estoque
    
    def recebe_solicitacao(self, num_bikes: int, periodo: str) -> bool:
        print(f'[Loja] - [recebe_solicitacao] - [Numero de bicicletas solicitadas: {num_bikes} | Estoque: {self.estoque}] - [Em {dt.datetime.now()}]')

        if num_bikes <= self.estoque:
            print(f'[Loja] - [recebe_solicitacao] - [ALUGUEL CONFIRMADO] - [Em {dt.datetime.now()}]')
            estoque = self.atualiza_estoque(num_bikes)
            return True
        else:
            print(f'[Loja] - [recebe_solicitacao] - [**ALUGUEL NAO REALIZADO**: a loja {self.nome} nao possui {num_bikes} bicicletas em estoque] - [Em {dt.datetime.now()}]')
            raise ValueError(f'\033[0;41mErro - Loja - recebe_solicitacao - O numero de bicicletas solicitadas ({num_bikes}) é maior que o estoque da loja {self.nome}\033[m')
    
    def atualiza_estoque(self, num_bikes: int) -> int:
        print(f'[Loja] - [atualiza_estoque] - [Loja deve atualizar o estoque] - [Numero de bicicletas alugadas/devolvidas: {num_bikes}] - [Em {dt.datetime.now()}]')
        self.estoque -= num_bikes
        print(f'[Loja] - [atualiza_estoque] - [Estoque atualizado: {self.estoque}] - [Em {dt.datetime.now()}]')
        return self.estoque

    def calcula_valor(self, data_inicio: dt.datetime, data_fim: dt.datetime, periodo: str, num_bikes: int) -> float:
        print(f'[Loja] - [calcula_valor] - [Dados do cliente: Numero de bicicletas alugadas: {num_bikes} | Periodo: {periodo} | Data do aluguel: {data_inicio} | Data da devolucao: {data_fim} ] - [Em {dt.datetime.now()}]')
        tempo_uso = (data_fim - data_inicio).total_seconds()

        if periodo == 'hora':
            valor: float = 5.00
            tempo: float = round(tempo_uso/3600, 2)  #tempo em horas
        elif periodo == 'dia':
            valor: float = 25.00
            tempo: float = round(tempo_uso/86400, 2)  #tempo em dias
        elif periodo == 'semana':
            valor: float = 100.00
            tempo: float = round(tempo_uso/604800, 2)  #tempo em semanas

        total = round((valor * tempo * num_bikes), 2)
        print(f'[Loja] - [calcula_valor] - [Loja calcula o valor do aluguel] - [Valor total do aluguel: R${total:.2f} | Valor do periodo escolhido: R${valor:.2f} | Tempo de permanencia com as bicicletas: {tempo:.2f} {periodo}(s) | Numero de bicicletas alugadas: {num_bikes}] - [Em {dt.datetime.now()}]')

        if num_bikes >= 3:  # desconto para aluguel de 3 ou mais bicicletas
            total = round((total * 0.7),2)
            print(f'[Loja] - [calcula_valor] - [Loja calcula o valor do aluguel com desconto para 3 ou mais bicicletas] - [Valor total do aluguel com desconto: R${total:.2f}] - [Em {dt.datetime.now()}]')

        bikes_devolvidas = (num_bikes) * (-1)
        self.atualiza_estoque(bikes_devolvidas)
        
        return total