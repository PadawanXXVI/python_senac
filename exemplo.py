class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, quantia):
        self.saldo += quantia

    def sacar(self, quantia):
        if self.saldo >= quantia:
            self.saldo -= quantia
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Saldo atual: {self.saldo}")

# Criando uma conta com saldo inicial de 500
conta1 = ContaBancaria(500)
conta2 = ContaBancaria(1000)

# Realizando um depósito de 300
conta1.depositar(300)
conta1.mostrar_saldo()  # Saída esperada: Saldo atual: 800

# Realizando um saque de 200
conta2.sacar(200)
conta2.mostrar_saldo()  # Saída esperada: Saldo atual: 600
