# Solicitação de entrada do usuário


Salario = float(input("Qual o salário de vocês? "))

energia = float(input("Quantos reais pretende deixar para Energia? "))
agua = float(input("Quantos reais pretende deixar para Água? "))
internet = float(input("Quantos reais pretende deixar para Internet? "))
faculdade = float(input("Quantos reais pretende deixar para Faculdade? "))
Impostos = float(input("Quantos reais pretende deixar para Impostos? "))
lazer = float(input("Quantos reais pretende deixar para lazer? "))
emergências = float(input("Quantos reais pretende deixar para emergência? "))
etc = float(input("Quantos reais pretende deixar para outros gastos? "))

# Cálculo do dinheiro necessário
dinheiro_necessario = energia + agua + internet + faculdade + Impostos + lazer + emergências + etc
dinheiro_faltando = dinheiro_necessario - Salario

# Verificação se o salário é suficiente
if Salario < dinheiro_necessario:
    print(f"Vocês precisam de {dinheiro_necessario:.2f} e estão faltando {dinheiro_faltando:.2f}")
else:
    print("VAMBOORA!")

teste = input("   ")
