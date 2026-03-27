# Projeto 04 - Simulador de Proposta e Contraproposta
# Autor: Felipe Souza
# Descrição: Simula negociação entre comprador e vendedor

def calcular_diferenca(valor_pedido, valor_ofertado):
    diferenca = valor_pedido - valor_ofertado
    percentual = (diferenca / valor_pedido) * 100
    return diferenca, percentual

def sugerir_contraproposta(valor_pedido, valor_ofertado):
    meio_termo = (valor_pedido + valor_ofertado) / 2
    proposta_vendedor = valor_pedido * 0.97
    proposta_comprador = valor_ofertado * 1.03
    return meio_termo, proposta_vendedor, proposta_comprador

def exibir_relatorio(valor_pedido, valor_ofertado):
    diferenca, percentual = calcular_diferenca(valor_pedido, valor_ofertado)
    meio_termo, proposta_vendedor, proposta_comprador = sugerir_contraproposta(valor_pedido, valor_ofertado)

    print("\n===== RELATÓRIO DE NEGOCIAÇÃO =====")
    print(f"Valor pedido pelo vendedor:  R$ {valor_pedido:,.2f}")
    print(f"Valor ofertado pelo comprador: R$ {valor_ofertado:,.2f}")
    print(f"Diferença:                   R$ {diferenca:,.2f} ({percentual:.1f}%)")
    print("\n--- SUGESTÕES DE NEGOCIAÇÃO ---")
    print(f"Meio termo:                  R$ {meio_termo:,.2f}")
    print(f"Vendedor cede 3%:            R$ {proposta_vendedor:,.2f}")
    print(f"Comprador sobe 3%:           R$ {proposta_comprador:,.2f}")

    # ---- PROGRAMA PRINCIPAL ----
print("===== SIMULADOR DE PROPOSTA E CONTRAPROPOSTA =====")
print("Informe os valores da negociação:\n")

valor_pedido = float(input("Valor pedido pelo vendedor (R$): "))
valor_ofertado = float(input("Valor ofertado pelo comprador (R$): "))

if valor_ofertado >= valor_pedido:
    print("\n✅ Não há necessidade de negociação!")
    print(f"O comprador ofertou R$ {valor_ofertado:,.2f} para um imóvel de R$ {valor_pedido:,.2f}")
else:
    exibir_relatorio(valor_pedido, valor_ofertado)