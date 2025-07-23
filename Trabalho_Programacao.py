from datetime import datetime
import time


# Inicializando o dicionário com as informações das contas.
#O dicionário tem o número da conta como chave e, como valor, outro dicionário com nome, senha, saldo e um extrato vazio.

#Dicionário de contas
contas = {
    24056: {"nome": "Rafael Chagas",
            "senha": "senha245",
            "saldo": 3000.0,
            "dia": 1,
            "extrato": []},
    73490: {"nome": "João Otávio",
            "senha": "abcdef19",
            "saldo": 800.0,
            "dia": 1,
            "extrato": []}
}

#Dicionário de Operações
Operações = {
    "1": "1. Consultar Saldo",
    "2": "2. Realizar Saque",
    "3": "3. Fazer Depósito",
    "4": "4. Conferir Extrato",
    "5": "5. Alterar Senha",
    "6": "6. Encerrar Sessão"
}

print("Bem-vindo ao Caixa Automático!")
while True:
    try:
        a = int(input("Digite o número da sua conta: "))
    except ValueError:
        print("Por favor, digite apenas números. Tente novamente.")
        continue

    if a in contas:
        tentativas = 3  # Define o número de tentativas para a senha
        while tentativas > 0:
            b = input("Olá, " + contas[a]["nome"] + ", digite sua senha: ")
            if b == contas[a]["senha"]:
                print("Carregando informações...")
                time.sleep(3)
                print("Seja bem-vindo(a), " + contas[a]["nome"] + "!")
                while True:
                    for value in Operações.values():
                        print(value)
                    c = input("Digite o número da operação: ")
                    
                    # Consulta de saldo
                    if c == "1":
                        print("Seu saldo é: R$ " + str(contas[a]['saldo']))
                    
                    # Saque
                    elif c == "2":
                        valor_saque = float(input("Digite o valor para saque: "))
                        if valor_saque <= contas[a]['saldo']:
                            contas[a]['saldo'] -= valor_saque
                            data_formatada = datetime.now().strftime("%m/%Y %H:%M:%S")
                            contas[a]['extrato'].append("Saque: R$ " + str(valor_saque) + " | Saldo após operação: R$ " + str(contas[a]['saldo']) + " | Data: " + data_formatada + " | Dia: " + str(contas[a]["dia"]))
                            print("Saque de R$ " + str(valor_saque) + " realizado com sucesso!")
                            print("Seu novo saldo é: R$ " + str(contas[a]['saldo']))
                        else:
                            print("Saldo insuficiente.")
                    
                    # Depósito
                    elif c == "3":
                        valor_deposito = float(input("Digite o valor para depósito: "))
                        contas[a]['saldo'] += valor_deposito
                        data_formatada = datetime.now().strftime("%m/%Y %H:%M:%S")
                        contas[a]['extrato'].append("Depósito: R$ " + str(valor_deposito) + " | Saldo após operação: R$ " + str(contas[a]['saldo']) + " | Data: " + data_formatada + " | Dia: " + str(contas[a]["dia"]))
                        print("Depósito de R$ " + str(valor_deposito) + " realizado com sucesso!")
                        print("Seu novo saldo é: R$ " + str(contas[a]['saldo']))
                    
                    # Extrato
                    elif c == "4":
                        print("Carregando extrato,aguarde alguns segundos...")
                        time.sleep(4)
                        print("Seu extrato é:")
                        if len(contas[a]["extrato"]) == 0:
                            print("Nenhuma transação realizada.")
                        else:
                            for item in contas[a]["extrato"]:
                                print(item)
                    
                    # Alterar senha
                    elif c == "5":
                        tentativas_senha = 3
                        while tentativas_senha > 0:
                            senha_atual = input("Digite sua senha atual para confirmar a alteração: ")
                            if senha_atual == contas[a]["senha"]:
                                nova_senha = input("Digite a nova senha: ")
                                contas[a]["senha"] = nova_senha
                                print("Senha alterada com sucesso!")
                                break  # Sai do loop de alteração de senha
                            else:
                                tentativas_senha -= 1
                                if tentativas_senha > 0:
                                    print(f"Senha incorreta. Você tem {tentativas_senha} tentativa(s) restante(s).")
                                else:
                                    print("Você errou a senha 3 vezes. Encerrando a sessão.")
                                    break  # Encerra o loop caso erre 3 vezes
                        continue  # Volta ao menu de operações após alteração da senha

                    
                    # Encerrar sessão
                    elif c == "6":
                        print("Sessão encerrada. Obrigado por utilizar o Caixa Automático!")
                        contas[a]["dia"] += 1  # Aumenta o dia a cada sessão encerrada
                        break
                    
                    # Operação inválida
                    else:
                        print("Operação inválida. Tente novamente.")
                    
                    # Perguntar se o usuário deseja fazer nova operação
                    while True:
                        nova_operacao = input("Deseja fazer uma nova operação? (s/n): ")
                        if nova_operacao in ['s', 'S']:
                            break  
                        elif nova_operacao in ['n', 'N']:
                            print("Sessão encerrada. Obrigado por utilizar o Caixa Automático!")
                            contas[a]["dia"] += 1  # Aumenta o dia também se o usuário optar por sair
                            break
                        else:
                            print("Resposta inválida. Por favor, digite apenas 's' para sim ou 'n' para não.")
                    if nova_operacao in ['n', 'N']:
                        break  # Encerra o loop de operações e encerra a sessão

                if c == "6" or nova_operacao in ['n', 'N']:
                    break  # Encerra o programa ao sair ou escolher "n"
            else:
                tentativas -= 1
                if tentativas > 0:
                    print(f"Senha incorreta. Você tem {tentativas} tentativa(s) restante(s).")
                else:
                    print("Você errou a senha 3 vezes. Encerrando o programa.")
                    break  # Encerra o programa ao errar a senha 3 vezes
        break  # Sai do loop da conta se errar 3 vezes
    else:
        print("Essa conta não existe. Tente novamente.")

