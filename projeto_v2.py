import textwrap

def menu():    
       menu = """

       [1] Depositar
       [2] Sacar
       [3] Extrato
       [4] Cadastrar usuário
       [5] Criar conta
       [6] Listar contas
       [7] Sair

       """     
       return input(textwrap.dedent(menu) + "Digite a opção desejada: ")


def deposito(saldo, valor, extrato, /):
       if valor < 0:
                     print("ERRO: Valor inválido!")
       else:
              saldo = saldo+valor
              extrato_deposito =f"""
                             ____________________________

                             Depósito ------- R$ {valor:.2f}
                             Saldo ---------- R$ {saldo:.2f}
                             ____________________________
                            """
              extrato = extrato +""+extrato_deposito
       return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques):
       numero_saques = numero_saques +1
       if numero_saques > 3:
              print("ERRO: Limite de saque diário atingido!")

       elif saldo == 0:
              print("ERRO: Saldo insuficiente")
       else:
              if valor > limite:
                     print("ERRO: O limite do valor de cada saque é R$500,00")
              else:
                     saldo = saldo - valor
                     extrato_saque =f"""
                             ____________________________

                             Saque ---------- R$ {valor:.2f}
                             Saldo ---------- R$ {saldo:.2f}
                             ____________________________
                                   """
                     extrato = extrato +""+extrato_saque
              return saldo, extrato
       

def exibir_extrato(saldo, /,*, extrato):
       extrato = extrato +  f"""
                             ____________________________

                             Saldo total ------ R$ {saldo:.2f}
                             ____________________________
                                   """
       
       print("Não foram realizadas movimentações." if not extrato else extrato)


def cadastrar_usuario(usuarios):
       cpf = input("Informe o CPF (apenas números):")
       usuario = filtrar_usuario(cpf, usuarios)

       if usuario:
              print("\n Este usuário já existe")
       
       else:
              nome = input("Informe o nome completo: ")
              data_nascimento = input("Informe a data de nascimento no formato (dd-mm-aaaa): ")
              endereco = input("Informe o endereço no seguinte formato (logradopuro, nro - bairro - cidade/sigla estado): ")
              usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
              print("Usuário criado com sucesso! ")

def cadastrar_conta(agencia, numero_conta, usuarios):
       cpf = input("Informe o CPF do usuário: ")
       usuario = filtrar_usuario(cpf, usuarios)

       if usuario:
              print("\n Conta criada com sucesso!")
              return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
       else:
              print("Usuário não encontrado!")


def filtrar_usuario(cpf, usuarios):
       usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
       return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
       for conta in contas:
              linha = f"""\
              Agência: {conta['agencia']}
              Número conta: {conta['numero_conta']}
              Titular: {conta['usuario']['nome']}
              """    
       
              print("=" * 50)
              print(textwrap.dedent(linha))


def main():
       AGENCIA = "0001"

       saldo = 0
       valor_limite_de_saque = 500
       extrato = ""
       numero_saques = 0
       usuarios = []
       contas = []


       while True:
              opcao = menu()
              
              if opcao == "1":
                    valor = float(input("Digite o valor do depósito: "))
                    saldo, extrato =  deposito(saldo, valor, extrato)

              elif opcao == "2":
                     valor = float(input("Digite o valor de saque: "))
                    
                     saldo, extrato = saque(
                           saldo = saldo,
                           valor = valor,
                           extrato = extrato,
                           limite = valor_limite_de_saque,
                           numero_saques = numero_saques
                    )
              
              elif opcao == "3":
                     exibir_extrato(saldo, extrato = extrato)

              elif opcao == "4":
                     cadastrar_usuario(usuarios)

              elif opcao == "5":
                     numero_conta = len(contas) + 1
                     conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

                     if conta:
                            contas.append(conta)

              elif opcao == "6":
                     listar_contas(contas)
              
              elif opcao == "7":
                     print("Sessão encerrada!")
                     break
              
              else:
                     print("Operação inválida, por favor selecione novamente a operação desejada")

if __name__ == "__main__":
       main()