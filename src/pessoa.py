#Cria a classe pessoa, que pode ser um passageiro ou um motorista
class Pessoa:
  def __init__(self,nome, dinheiro: float):
    #atributos privados
    self.__nome = nome    #Nome da pessoa
    self.__dinheiro = dinheiro    #Dinheiro da pessoa
  
  #Propriedade para acessar o nome da pessoa 
  @property
  def nome(self):
    return self.__nome
  
  #Propriedade para acessar o dinheiro da pessoa
  @property
  def dinheiro(self):
    return self.__dinheiro
  
  #Metodo para realizar o pagamento
  def paga(self, valor: float):
    #Se o pagamento for maior que dinheiro disponivel
    if valor > self.__dinheiro:
      pago = self.__dinheiro    #Paga todo dinheiro que tiver
      self.__dinheiro = 0    #Fica sem dinheiro
      return pago    #Retorna quanto foi pago
    else:
      self.__dinheiro -= valor    #Diminui o valor do dinheiro
      return valor    #Retorna o quanto foi pago
    
  #Metodo para receber o pagamento
  def receba(self, valor: float):
    self.__dinheiro += valor    #Adiciona o valor recebido à carteira
    
    
    