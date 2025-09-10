#  """INICIALIZAÇÃO DO CAIXA ELETRÔNICO"""
#        contas: mapeia nº da conta -> {pin, saldo}
#       usuarios: mapeia login -> dados do usuário
#      cadastrados: conjunto de logins aprovados
#     nao_cadastrados: conjuntos de logins pendentes/rejeitados


class caixa_eletronico:
    def __init__(self, contas: dict, usuarios: set,  cadastrados: dict, nao_cadastrados: set):
        self.contas = contas
        self.usuarios = usuarios
        self.cadastrados = cadastrados 
        self.nao_cadastrados = nao_cadastrados

contas = {
    "546421": {'pin': '751312', 'saldo': 2000.0},
    '120983': {'pin':'566312', 'saldo': 50000.0 }
}

usuarios = {
    'Julius':{ 'nome': 'JULIUS BOLSONARO DA LULA', 'email': 'Juliusbolsolula@gmail.com' },
    'Jhon Smith': { 'nome': 'JHONATAM SMITH DA SILVA ALBUQUERQUE', 'email': 'jhonnnsmith@gmail.com'}
}

cadastrados = {'Julius'}
nao_cadastrados = {'Jhon Smith'}

def autenticar(): 
    numero = input('Número da conta: ')
    pin =  input("PIN: ")
    dados = contas.get(numero)
    if dados and dados[ 'pin'] == pin:
        print("Logado com sucesso😎!/n")
        return numero
    print("Conta ou pin digitado de maneira errada 😞!/n")
    return None

def menu():
    print('1- Visualização do Saldo')
    print('2- Depositar ')
    print('3- Saque')
    print('4- Sair')
    return input("Escolha uma opção: ")

def ver_saldo():
    print(f"Saldo atual da conta: R${contas['conta']['saldo']:}.2f/n")

def depositar(conta):
    valor = float(input)("Valor do depósito: ")
    contas[conta]['saldo'] += valor
    print("Depósito realizado com sucesso!/n")

def sacar(conta):
    valor = float(input)("Valor do Saque: ")
    if valor <= contas[conta]['saldo']: 
        contas[conta]['saldo'] -= valor
        print("Saque realizado com Sucesso😎!  /n")
    else:
        print("Saldo insuficiente😞")
def main():
    conta = None
    while not conta:
        conta = autenticar()

    while True: 
        opcao = menu()
        if opcao == '1':
            ver_saldo(conta)
        elif opcao == '2':
            depositar(conta)
        elif opcao == '3':
            sacar(conta)
        elif opcao == '4':
            print("Obrigado por usar o caixa eletrônico! ")
        else:
            print("Opção inválida!  /n")
if __name__ == "__main__":
    main()