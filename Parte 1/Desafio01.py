menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def formatar_valor(valor: float) -> str:
    """Formata valores monetários com 2 casas decimais"""
    return f"R$ {valor:.2f}"

while True:
    try:
        opcao = input(menu).strip().lower()
        
        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                if valor <= 0:
                    print("Operação falhou! O valor deve ser positivo.")
                    continue
                
                saldo += valor
                extrato.append(f"Depósito: {formatar_valor(valor)}")
                print(f"Depósito de {formatar_valor(valor)} realizado com sucesso!")
                
            except ValueError:
                print("Operação falhou! Valor inválido.")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                
                if valor <= 0:
                    print("Operação falhou! O valor deve ser positivo.")
                elif valor > saldo:
                    print("Operação falhou! Saldo insuficiente.")
                elif valor > limite:
                    print(f"Operação falhou! O limite por saque é {formatar_valor(limite)}.")
                elif numero_saques >= LIMITE_SAQUES:
                    print(f"Operação falhou! Limite de {LIMITE_SAQUES} saques diários atingido.")
                else:
                    saldo -= valor
                    extrato.append(f"Saque: {formatar_valor(valor)}")
                    numero_saques += 1
                    print(f"Saque de {formatar_valor(valor)} realizado com sucesso!")
                    
            except ValueError:
                print("Operação falhou! Valor inválido.")

        elif opcao == "e":
            print("\n" + "=" * 40)
            print("EXTRATO".center(40))
            print("=" * 40)
            
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print("\n".join(extrato))
            
            print(f"\nSaldo atual: {formatar_valor(saldo)}")
            print("=" * 40)

        elif opcao == "q":
            print("Obrigado por usar nosso sistema!")
            break

        else:
            print("Operação inválida! Por favor selecione uma opção válida.")
            
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        break