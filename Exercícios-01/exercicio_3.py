'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Exercício proposto para receber dados fictícios para simular uma fatura
'''

nome = input("Digite o nome do cliente: ")
dia = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

print(f"Olá, {nome}")
print(f"A sua fatura com vencimento em {dia} de {mes} no valor de R$ {valor} está fechada.")