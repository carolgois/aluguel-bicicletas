from Cliente import Cliente
from Loja import Loja
import datetime as dt

cliente1 = Cliente()
cliente2 = Cliente()
cliente3 = Cliente()

loja1 = Loja('Alfa', 12)
loja2 = Loja('Beta', 20)
loja3 = Loja('Gama', 15)

cliente = cliente1
loja = loja1
num_bikes = 5
periodo = 'dia'


estoque = cliente.ve_estoque(loja)
confirmacao = cliente.solicita_aluguel(loja, num_bikes, periodo)
if confirmacao:
    cliente.confirma_aluguel(num_bikes, periodo, loja)
cliente.data_aluguel -= dt.timedelta(days=7)
cliente.devolve_bikes(loja)
