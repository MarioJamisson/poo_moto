# Simulação de Moto com Corridas e Pagamentos

Este projeto é uma simulação simples de uma moto que realiza corridas com um motorista e um passageiro. Ele gerencia as interações entre as pessoas e a moto, calculando custos e pagamentos.

---

## 🛠️ **Funcionalidades**

- Adicionar um **motorista** e um **passageiro** à moto.
- Simular corridas percorrendo distâncias em quilômetros.
- Calcular o custo acumulado da corrida (R$1 por km).
- Gerenciar o pagamento pelo passageiro ao motorista:
  - Se o passageiro não tiver dinheiro suficiente, o "Uber" cobre a diferença.
- Mostrar o estado atual da moto, incluindo:
  - Motorista.
  - Passageiro.
  - Custo atual da corrida.

---

## 🗂️ **Estrutura do Código**

O projeto possui duas classes principais:

### **1. Classe `Pessoa`**
Representa uma pessoa (motorista ou passageiro) com:
- **Atributos:**
  - `nome` (string): Nome da pessoa.
  - `dinheiro` (float): Quantidade de dinheiro disponível.
- **Métodos:**
  - `pagar(valor)`: Faz a pessoa pagar um valor. Retorna quanto foi pago.
  - `receber(valor)`: Adiciona dinheiro ao saldo da pessoa.

### **2. Classe `Moto`**
Representa a moto que realiza as corridas com:
- **Atributos:**
  - `motorista`: Armazena o motorista da moto (um objeto `Pessoa`).
  - `passageiro`: Armazena o passageiro da moto (um objeto `Pessoa`).
  - `custo`: Registra o custo acumulado da corrida.
- **Métodos:**
  - `setDriver(motorista)`: Define o motorista da moto.
  - `setPass(passageiro)`: Define o passageiro da moto.
  - `drive(km)`: Simula uma corrida por uma distância em quilômetros.
  - `leavePass()`: Remove o passageiro da moto e realiza o pagamento da corrida.
  - `show()`: Exibe o estado atual da moto.

---

## 🖥️ **Como Executar**

1. Certifique-se de ter o Python instalado na sua máquina (versão 3.7 ou superior).
2. Clone este repositório ou copie os arquivos para o seu ambiente.
3. Crie um arquivo `teste.py` para simular o uso do programa:
   ```python
   from moto import Pessoa, Moto

   # Criação das pessoas
   motorista = Pessoa("Carlos", 100)
   passageiro = Pessoa("Ana", 50)

   # Criação da moto
   moto = Moto()

   # Definir motorista e passageiro
   moto.setDriver(motorista)
   moto.setPass(passageiro)

   # Simular corrida
   moto.drive(30)  # Moto dirige 30 km

   # Mostrar estado atual
   moto.show()

   # Passageiro desce e paga
   moto.leavePass()

   # Mostrar estado final
   moto.show()
4. Excecute o script
   ```python
   python teste.py

## 🚀 **Exemplo de saída**
   ```python
   Carlos agora é o motorista.
   Ana entrou na moto.
   A moto percorreu 30 km. Custo atual da corrida: R$30
   Motorista: Carlos, Passageiro: Ana, Custo atual: R$30
   Ana pagou R$30 ao motorista.
   O passageiro desceu da moto.
   Motorista: Carlos, Passageiro: Ninguém, Custo atual: R$0

## 📋 **Regras e restrições**
- Um passageiro não pode subir na moto sem que haja um motorista.
- Não é possível adicionar mais de um passageiro.
- Não é possível dirigir sem motorista e passageiro presentes.

## 📚 **Aprendizados e conceitos**
- Encapsulamento: Uso de atributos privados e métodos para manipulação segura.
- Reutilização: Classes Pessoa e Moto podem ser usadas ou adaptadas para outros cenários.
- Validação: Verificação de condições para manter estados válidos (ex.: não dirigir sem passageiro).
- Interação entre objetos: O motorista e passageiro interagem através da moto.

## 🧑‍💻 **Contribuição**
Sinta-se à vontade para sugerir melhorias, abrir issues ou enviar pull requests! 😊

## 📝 **Licença**
Este projeto está licenciado sob a licença MIT.