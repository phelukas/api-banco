import random


def saque(cliente, valor):

    if (cliente.saldo + cliente.cheque_especial) < valor:
        return False
    
    if cliente.saldo >= valor:
        cliente.saldo -= valor
        cliente.save()
        return True

    elif cliente.saldo == 0:
        cliente.cheque_especial -= valor
        cliente.save()
        return True

    elif cliente.saldo != 0 and cliente.saldo < valor:
        cliente.cheque_especial += cliente.saldo
        cliente.saldo = 0
        cliente.cheque_especial -= valor
        cliente.save()
        return True

def deposito(cliente, valor):
    cliente.saldo += valor
    cliente.save()
    return True