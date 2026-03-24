# Projeto 02 - Analisador de Perfil do Comprador
# Autor: Felipe Souza
# Descrição: Analisa se o cliente tem perfil aprovado para financiamento


print("===== ANALISADOR DE PERFIL DO COMPRADOR =====")
print("Preencha os dados abaixo:\n")

renda_mensal = float(input("Renda mensal do cliente (R$): "))
valor_imovel = float(input("Valor do imóvel (R$): "))
entrada = float(input("Valor da entrada (R$): "))
prazo_anos = int(input("Prazo do financiamento (anos): "))
taxa_juros_anual = float(input("Taxa de juros anual (%): "))

# ---- CÁLCULOS ----
valor_financiado = valor_imovel - entrada
prazo_meses = prazo_anos * 12
taxa_juros_mensal = taxa_juros_anual / 100 / 12

parcela = (valor_financiado * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -prazo_meses)

# ---- ANÁLISE DE PERFIL ----
limite_parcela = renda_mensal * 0.30

if parcela <= limite_parcela:
    print("\n✅ CLIENTE APROVADO!")
    print(f"Parcela:          R$ {parcela:,.2f}")
    print(f"Limite (30%):     R$ {limite_parcela:,.2f}")
    print(f"Renda mensal:     R$ {renda_mensal:,.2f}")
else:
    print("\n❌ CLIENTE REPROVADO!")
    print(f"Parcela:          R$ {parcela:,.2f}")
    print(f"Limite (30%):     R$ {limite_parcela:,.2f}")
    print(f"Renda mensal:     R$ {renda_mensal:,.2f}")
    print(f"Renda necessária: R$ {parcela / 0.30:,.2f}")