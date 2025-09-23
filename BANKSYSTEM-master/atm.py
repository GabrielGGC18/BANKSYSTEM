from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

# Dados simulados
contas = {
    "546421": {'pin': '751312', 'saldo': 2000.0},
    "120983": {'pin': '566312', 'saldo': 50000.0},
    "052.731.071-99": {'pin': '999999', 'saldo': 1000.0}  # Conta de destino adicionada
}

# Autenticação
def autenticar():
    numero = entry_conta.get()
    pin = entry_pin.get()
    dados = contas.get(numero)
    if dados and dados['pin'] == pin:
        messagebox.showinfo("Sucesso", "Logado com sucesso 😎")
        abrir_menu(numero)
    else:
        messagebox.showerror("Erro", "Conta ou PIN incorretos 😞")

# Menu com Abas
def abrir_menu(conta):
    janela_menu = Toplevel(root)
    janela_menu.title("Menu do Caixa")
    janela_menu.geometry("450x300")

    notebook = ttk.Notebook(janela_menu)
    notebook.pack(expand=True, fill='both')

    # Aba Saldo
    aba_saldo = Frame(notebook)
    notebook.add(aba_saldo, text="Saldo")

    def ver_saldo():
        saldo = contas[conta]['saldo']
        messagebox.showinfo("Saldo", f"Saldo atual: R${saldo:.2f}")

    Button(aba_saldo, text="Ver Saldo", command=ver_saldo).pack(pady=20)

    # Aba Depósito
    aba_deposito = Frame(notebook)
    notebook.add(aba_deposito, text="Depósito")

    Label(aba_deposito, text="Valor do Depósito:").pack()
    entry_deposito = Entry(aba_deposito)
    entry_deposito.pack()

    def depositar():
        valor = float(entry_deposito.get())
        contas[conta]['saldo'] += valor
        messagebox.showinfo("Depósito", "Depósito realizado com sucesso!")

    Button(aba_deposito, text="Depositar", command=depositar).pack(pady=10)

    # Aba Saque
    aba_saque = Frame(notebook)
    notebook.add(aba_saque, text="Saque")

    Label(aba_saque, text="Valor do Saque:").pack()
    entry_saque = Entry(aba_saque)
    entry_saque.pack()

    def sacar():
        valor = float(entry_saque.get())
        if valor <= contas[conta]['saldo']:
            contas[conta]['saldo'] -= valor
            messagebox.showinfo("Saque", "Saque realizado com sucesso 😎")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente 😞")

    Button(aba_saque, text="Sacar", command=sacar).pack(pady=10)

    # Aba Pix
    aba_pix = Frame(notebook)
    notebook.add(aba_pix, text="Pix")

    Label(aba_pix, text="Conta destino:").pack()
    entry_destino = Entry(aba_pix)
    entry_destino.pack()
    entry_destino.insert(0, "052.731.071-99")  # Preenche automaticamente com a conta de destino

    Label(aba_pix, text="Valor do Pix:").pack()
    entry_valor_pix = Entry(aba_pix)
    entry_valor_pix.pack()

    def pix():
        destino = entry_destino.get()
        valor = float(entry_valor_pix.get())
        if destino not in contas:
            messagebox.showerror("Erro", "Conta de destino não encontrada 😞")
            return
        if valor <= contas[conta]['saldo']:
            contas[conta]['saldo'] -= valor
            contas[destino]['saldo'] += valor
            messagebox.showinfo("Pix", f"Pix de R${valor:.2f} enviado para {destino} 😎")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente 😞")

    Button(aba_pix, text="Enviar Pix", command=pix).pack(pady=10)

    # Aba Cartão de Crédito
    aba_credito = Frame(notebook)
    notebook.add(aba_credito, text="Cartão de Crédito")

    Label(aba_credito, text="Limite do Cartão:").pack()
    entry_limite = Entry(aba_credito)
    entry_limite.pack()

    def cartao_credito():
        limite = float(entry_limite.get())
        messagebox.showinfo("Crédito", f"Cartão com limite de R${limite:.2f} ativado!")

    Button(aba_credito, text="Ativar Cartão", command=cartao_credito).pack(pady=10)

# Tela de carregamento
def tela_carregamento():
    loading = Toplevel()
    loading.title("Carregando...")
    loading.geometry("300x150")
    Label(loading, text="Iniciando sistema...", font=("Arial", 12)).pack(pady=10)
    progress = ttk.Progressbar(loading, orient=HORIZONTAL, length=250, mode='determinate')
    progress.pack(pady=10)

    def carregar():
        for i in range(101):
            progress['value'] = i
            loading.update_idletasks()
            loading.after(15)
        loading.destroy()

    Button(loading, text="Iniciar", command=carregar).pack(pady=10)

# Janela principal
root = Tk()
root.title("Caixa Eletrônico")
root.geometry("400x250")

Label(root, text="Número da Conta:").pack()
entry_conta = Entry(root)
entry_conta.pack()

Label(root, text="PIN:").pack()
entry_pin = Entry(root, show="*")
entry_pin.pack()

Button(root, text="Entrar", command=autenticar).pack(pady=10)
Button(root, text="Tela de Carregamento", command=tela_carregamento).pack(pady=5)

root.mainloop()
