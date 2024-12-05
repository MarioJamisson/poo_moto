#Importa a classe Pessoa 
from pessoa import Pessoa

#Cria a classe que representará a moto
class Moto:
  def __init__(self):
    self.__motorista = None    #Motorista iniciará nulo(sem ninguém)
    self.__passageiro = None    #Passageiro iniciará nulo(sem ninguém)
    self.__custo = 0    #O custo iniciará em zero, pois não houve corrida
    
#Metodo para adicionar um motorista na moto
  def setDriver(self, motorista: Pessoa):
    if not self.__motorista:    #Se não tiver motorista
      self.__motorista = motorista    #Adiciona um
      print(f"{motorista.nome} é o motorista")
      
    else:    
      print("A moto ja tem motorista")    #Mensagem se já tiver motorista
      
#Define quem será o passageiro
  def setPass(self, passageiro: Pessoa):
    if not self.__motorista:
      print("Impossivel ser passageiro sem motorista")    #Mensagem exibida caso não haja motorista
      return
    if not self.__passageiro:    #Se não tiver passageiro
      self.__passageiro = passageiro    #Adiciona um
      self.__custo = 0
      print(f"O passageiro {passageiro.nome} entrou na moto")
    else:
      print("A moto ja tem um pasageiro")    #Mensagem exibida caso ja tenha passageiro

#Metodo que faz a moto andar   
  def drive(self, km: int):
    if not self.__motorista or not self.__passageiro:
      #Não eh possivel dirigir sem motorista nem passageiro
      print("A moto precisa de um passageiro e um motorista")
      return 
    self.__custo += km    #Como cada km vale um real, ele vai adicionando no custo
    print(f"A moto percorreu {km} km. Custo da corrida é de R${self.__custo}")
 
#Passageiro sai da moto   
  def leavePass(self):
    if not self.__passageiro:    #Se não houver passageiro
      print("Não há passageiro na moto para descer")
      return 
    
    #Calcula o quano o passageiro tem que pagar
    valorPago = self.__passageiro.paga(self.__custo)
    
    if valorPago < self.__custo:    #Se o passageiro não pagar tudo 
      diferenca = self.__custo - valorPago    #Calcula a diferença
      print(f"Faltam R${diferenca} de diferença")
      self.__motorista.receba(valorPago)    #Motorista recebe o valor pago
      print(f"O Uber pagou o restante {diferenca} ao motorista")
      self.__motorista.receba(diferenca)    #O Uber paga a diferença
      
    else:
      #Passageiro paga o dinheiro certo
      self.__motorista.receba(valorPago)
      print(f"O passageiro {self.__passageiro.nome} pagou {valorPago} ao motorista")
    
    #Reseta a moto
    self.__passageiro = None
    self.__custo = 0
    print("O passageiro desceu da moto")
    
  
  #Exibe as informaões da moto
  def show(self):
    #Checa se tem motorista e passageiro
    motorista_nome = self.__motorista.nome if self.__motorista else "Ninguém"
    passageiro_nome = self.__passageiro.nome if self.__passageiro else "Ninguém"
    #Printa as informações
    print(f"Motorista: {motorista_nome}, Passageiro: {passageiro_nome}, Custo atual: R${self.__custo}")
