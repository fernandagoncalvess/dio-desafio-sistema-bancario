menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

while True:
        opcao = input(menu)

        if opcao == "1":
              deposito = float(input("Digite o valor do deposito: "))
              if deposito < 0:
                     print("ERRO: Apenas valores positivos")
              else:
                     saldo = saldo+deposito
              extrato_deposito =f"""
                            ____________________________

                            Depósito ------- R$ {deposito}
                            Saldo ---------- R$ {saldo}
                            ____________________________
                            """
              extrato = extrato +""+extrato_deposito

        elif opcao == "2":
               numero_saques = numero_saques +1
               if numero_saques > 3:
                      print("ERRO: Limite de saque diário atingido!")

               elif saldo == 0:
                      print("ERRO: Saldo insuficiente")
               else:
                      saque = float(input("Digite o valor do saque: "))
                      if saque > limite:
                            print("ERRO: O limite do valor de cada saque é R$500,00")
                      else:
                            saldo = saldo - saque
                      extrato_saque =f"""
                            ____________________________

                            Saque ---------- R$ {saque}
                            Saldo ---------- R$ {saldo}
                            ____________________________
                            """
                      extrato = extrato +""+extrato_saque
        
        elif opcao == "3":
               print(extrato+f"""
                            ____________________________

                            Saldo total ------ R$ {saldo}
                            ____________________________
                            """)
            
        elif opcao == "4":
               break
        
        else:
               print("Operação inválida, por favor selecione novamente a operação desejada")

    