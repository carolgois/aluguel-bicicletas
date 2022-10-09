from Loja import Loja
import datetime as dt

class Cliente(object):
    def __init__(self):
        self.bikes_alugadas: int = 0
        self.loja_contratada: Loja = None

    def ve_estoque(self, loja: Loja) -> int:
        if not isinstance(loja, Loja):
            raise TypeError(f'\033[0;41mErro - Clinte - ve_estoque - O parâmetro loja é do tipo {type(loja)}\033[m')
        print(f'[Cliente] - [ver_estoque] - [Cliente pede para ver estoque da loja {loja.nome}] - [Em {dt.datetime.now()}]')
        estoque: int = loja.mostra_estoque()
        print(f'[Cliente] - [ver_estoque] - [Cliente ve estoque da loja {loja.nome}] - [Estoque atual: {estoque}] - [Em {dt.datetime.now()}]')
        return estoque
    
    def solicita_aluguel(self, loja: Loja, num_bikes: int, periodo: str) -> bool:
        if not isinstance(loja, Loja):
            raise TypeError(f'\033[0;41mErro - Cliente - solicita_aluguel - O parâmetro loja é do tipo {type(loja)}\033[m') 
        elif not isinstance(num_bikes, int):
            raise TypeError(f'\033[0;41mErro - Cliente - solicita_aluguel - O numero de bicicletas é do tipo {type(num_bikes)}. Deve ser do tipo inteiro\033[m')
        elif num_bikes <= 0:
            raise ValueError(f'\033[0;41mErro - Cliente - solicita_aluguel - O numero de bicicletas solicitadas foi {num_bikes}. Deve ser maior que zero\033[m')
        elif periodo not in ['hora', 'dia', 'semana']:
            raise Exception(f'\033[0;41mErro - Cliente - solicita_aluguel - O periodo indicado foi {periodo}. Deve ser: hora, dia ou semana\033[m')
        
        print(f'[Cliente] - [solicita_aluguel] - [loja: {loja.nome} | Numero de bicicletas solicitadas: {num_bikes} | Periodo: {periodo}] - [Em {dt.datetime.now()}]')

        if self.bikes_alugadas == 0:
            confirmacao: bool = loja.recebe_solicitacao(num_bikes, periodo)
            return confirmacao
        else:
            print(f'[Cliente] - [solicita_aluguel] - [**ALUGUEL NAO AUTORIZADO**: O cliente ja possui contrato em andamento e nao podera alugar mais bicicletas] - [Loja: {self.loja_contratada} | Numero de bicicletas alugadas: {self.bikes_alugadas} | Periodo: {self.periodo_aluguel}] - [Em {dt.datetime.now()}]')
            raise Exception(f'\033[0;41mErro - Cliente - solicita_aluguel - O cliente ja possui um contrato de aluguel com a loja {self.loja_contratada.nome}.\033[m')

    def confirma_aluguel(self, num_bikes, periodo, loja):
        print(f'[Cliente] - [confirma_aluguel] - [Solicita atualizacao dos dados do aluguel] - [Em {dt.datetime.now()}]')
        data_inicio = dt.datetime.now()
        self.atualiza_dados(num_bikes, data_inicio, periodo, loja)
    
    def atualiza_dados(self, num_bikes: int, data_inicio: dt.datetime, periodo: str, loja: Loja):
        print(f'[Cliente] - [atualiza_dados] - [Cliente fara atualizacao dos dados do aluguel] - [Numero de bicicletas alugadas: {num_bikes} | Periodo: {periodo} | Data do aluguel: {data_inicio} | Loja: {loja}] - [Em {dt.datetime.now()}]')
        self.bikes_alugadas: int = num_bikes
        self.data_aluguel: dt.datetime = data_inicio
        self.periodo_aluguel: str = periodo
        self.loja_contratada: Loja = loja
        print(f'[Cliente] - [atualiza_dados] - [Atualizacao de dados do cliente apos aluguel/devolucao das bicicletas] - [Numero de bicicletas alugadas: {self.bikes_alugadas} | Periodo: {self.periodo_aluguel} | Data do aluguel: {self.data_aluguel} | Loja: {self.loja_contratada}] - [Em {dt.datetime.now()}]')

    def devolve_bikes(self, loja: Loja):
        if loja != self.loja_contratada:
            raise Exception(f'\033[0;41mErro - Cliente - devolve_bikes - O cliente nao possui um contrato de aluguel com a loja {loja.nome}.\033[m')
            
        data_fim = dt.datetime.now()
        print(f'[Cliente] - [devolve_bikes] - [Loja: {loja.nome} | Numero de bikes alugadas: {self.bikes_alugadas} | Periodo: {self.periodo_aluguel} | Data do aluguel: {self.data_aluguel} | Data da devolucao: {data_fim}] - [Em {dt.datetime.now()}]')
        valor_total: float = loja.calcula_valor(self.data_aluguel, data_fim, self.periodo_aluguel, self.bikes_alugadas)
        self.atualiza_dados(0, None, None, None)
        