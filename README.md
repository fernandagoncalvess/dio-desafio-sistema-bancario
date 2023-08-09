# DIO Desafio Sistema Bancário - versão 1💰
#### Neste projeto foi implementado um sistema bancário com 3 operações essenciais que são depósito, saque e extrato. Durante o desafio foi possível aplicar os conhecimentos adquiridos no curso de programação em Python fornecido pela DIO.

## Sobre as operações básicas 
### Depósito
Será possível depositar valores positivos para a conta bancária. A versão 1 do projeto trabalha apenas com 1 usuário, assim não é preciso identificação, número da agência e número da conta. Todos os depósitos foram armazenados em uma variável e exibidos na operação de extrato. 

### Saque
É permitido apenas 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo na conta, o sistema vai exibir uma mensagem informando que não é possível sacar dinheiro por falta de saldo. Todos os saques são armazenados em uma variável e exibidos na operação de extrato.

### Extrato
Lista todos os depósitos e saques realizados na conta. Ao final da listagem, é exibido o saldo atual da conta.

<br>

# DIO Desafio Sistema Bancário - versão 2💰

#### Nesta versão do projeto, o sistema bancário foi otimizado com funções Python. Saque, depóstio e extrato foram separados em funções. 
### Novas funcionalidades
#### Além das funções das operações básicas, foram adicionadas três novas funções:
### Criar usuário 
Onde é cadastrado um usuário por vez e armazenado em uma lista.
### Criar conta 
Onde cria contas para algum usuário que foi cadastrado, um usuário pode ter mais de uma conta.
### Listar contas 
Esta função possibilita a visualização de uma lista contendo todas as contas existentes e a quais usuários elas pertencem.