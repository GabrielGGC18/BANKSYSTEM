#  """INICIALIZAÇÃO DO CAIXA ELETRÔNICO"""
#        contas: mapeia nº da conta -> {pin, saldo}
#       usuarios: mapeia login -> dados do usuário
#      cadastrados: conjunto de logins aprovados
#     nao_cadastrados: conjuntos de logins pendentes/rejeitados
#   Imports das Bibliotecas e Abrir a OPEN_WINDOW

from dataclasses import dataclass, field
from tkinter import *
import tkinter.ttk as ttk 

master = Tk()
master.geometry("720x640")
master.title("main window")


def open_new_window():
    new_window = Toplevel("master")
    new_window.title("New window")
    new_window.geometry("720x640")

    Label(new_window, text = "This is a new window").pack(pady=20)  

Label(master, text = "This is the main window").pack(pady=10)
Button(master, text = " Open new window", command=open_new_window).pack(pady=10)

master.mainloop()

@dataclass
class conta: 
    numero: str
    pin_hash: str
    saldo: float = 0.0
    historico: list = field(default_factory= list)
    
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
    print('4- pix')
    print('5- Sair')
    return input("Escolha uma opção: ")

def ver_saldo():
    print(f"Saldo atual da conta: R${contas['conta']['saldo']:}.2f")

def depositar(conta):
    valor = float(input("Valor do depósito: "))
    contas[conta]['saldo'] += valor
    print("Depósito realizado com sucesso!/n")

def sacar(conta):
    valor = float(input("Valor do Saque: ")) 
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
            pix(conta)
        
        elif opcao == '5':
             print("Obrigado por usar o caixa eletrônico! ")
        else:
            print("Opção inválida!  /n")
            break 
if __name__ == "__main__":
    main()

def pix(conta_origem):
    destino = input("Número da conta de destino: ")
    if destino not in contas: 
        print("Conta de destino não encontrada 😞")
        return 
    valor = float(input ("Valor de Transferência PIX: "))
    if valor <= contas[conta_origem]['saldo']:
        contas[conta_origem]['saldo'] -= valor
        contas[destino]['saldo'] += valor
        print("Pix de valor R${2.f} realizado para conta {destino} 😎 ")
    else:
        print("Saldo insuficiente😞 ")

def cartao_credito(limite):
    destino = input("Limite do cartão de crédito")