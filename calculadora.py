# Projeto 01 - Calculadora de Financiamento Imobiliário
# Autor: Felipe Souza
# Descrição: Calcula o valor mensal de um financiamento imobiliário


print("===== SIMULAÇÃO DE FINANCIAMENTO =====")
print("Preencha os dados abaixo:\n")

# ---- DADOS DO IMÓVEL ----
valor_imovel = float(input("Valor do imóvel: R$ "))        # Valor total do imóvel em reais
entrada = float(input('Valor de entrada: R$ '))             # Valor da entrada
prazo_anos = int(input('Prazo de financiamento (em anos): '))                # Prazo do financiamento em anos
taxa_juros_anual = float(input('Taxa de juros anual do banco (%): '))        # Taxa de juros anual em %

# ---- CÁLCULOS ----
valor_financiado = valor_imovel - entrada
prazo_meses = prazo_anos * 12
taxa_juros_mensal = taxa_juros_anual / 100 / 12

parcela = (valor_financiado * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -prazo_meses)
total_pago = parcela * prazo_meses
total_juros = total_pago - valor_financiado

# ---- RESULTADO ----
print("\n===== RESULTADO DA SIMULAÇÃO =====")
print(f"Valor do imóvel:      R$ {valor_imovel:,.2f}")
print(f"Entrada:              R$ {entrada:,.2f}")
print(f"Valor financiado:     R$ {valor_financiado:,.2f}")
print(f"Prazo:                {prazo_anos} anos ({prazo_meses} meses)")
print(f"Taxa de juros:        {taxa_juros_anual}% ao ano")
print(f"Parcela mensal:       R$ {parcela:,.2f}")
print(f"Total pago:           R$ {total_pago:,.2f}")
print(f"Total em juros:       R$ {total_juros:,.2f}")
