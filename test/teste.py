import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

#Importa as classes Pessoa e Moto
from pessoa import Pessoa
from moto import Moto

motorista1 = Pessoa("Sr. Carlos", 50.0)    #Cria uma instancia de Pessoa, motorista1
passageiro1 = Pessoa("Carolina", 15.50)    #Cria uma instancia de Pessoa, passageiro1

moto = Moto()    #Inicia a moto
moto.setDriver(motorista1)    #Adiciona um motorista
moto.setPass(passageiro1)    #Adiciona um passageiro

moto.drive(8)    #Dirige por 8km
moto.drive(3)    #Dirige por mais 3km

moto.leavePass()    #Passageiro pega o beco

moto.show()    #Mostra o estado da moto