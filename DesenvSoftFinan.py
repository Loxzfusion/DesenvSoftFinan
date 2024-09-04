# Definição do menu do sistema bancário

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

# Variáveis de controle

saldo = 0.0
limite_saque = 500.0
extrato = []
numero_saques = 0
limite_diario = 3

def exibir_extrato():
    """Função para exibir o extrato bancário"""
    print("\n================ Extrato ================")
    
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    
    print("==========================================")
    
def depositar(valor):
    """Função para realizar depósitos."""
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    """Função para realizar saques."""
    global saldo, numero_saques
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite_saque:
        print("Operação falhou! O valor do saque excede o limite de R$ 500,00.")
    elif numero_saques >= limite_diario:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

# Loop

while True:
    opcao = input(menu).lower()
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)
    
    elif opcao == "3":
        exibir_extrato()
        
    elif opcao == "4":
        print("Obrigado por utilizar o sistema. Até logo!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

        
