# Projeto 03 - Organizador de Carteira de Imóveis
# Autor: Felipe Souza
# Descrição: Cadastra a lista de imóveis da carteira do corretor

print("===== ORGANIZADOR DE CARTEIRA DE IMÓVEIS =====\n")

# Começa com a carteira vazia
imoveis = []

# Pergunta quantos imóveis o corretor quer cadastrar
quantidade = int(input("Quantos imóveis deseja cadastrar? "))

print("\nCadastre os imóveis abaixo:")

for i in range(quantidade):
    print(f"\nImóvel {i + 1}:")
    endereco = input("  Endereço: ")
    tipo = input("  Tipo (apto/casa/studio): ")
    valor = float(input("  Valor (R$): "))

    imovel = {
        "endereco": endereco,
        "tipo": tipo,
        "valor": valor
    }

    imoveis.append(imovel)

print("\n===== CARTEIRA DE IMÓVEIS =====")
print(f"Total de imóveis cadastrados: {len(imoveis)}\n")

for i, imovel in enumerate(imoveis):
    print(f"Imóvel {i + 1}")
    print(f"  Endereço: {imovel['endereco']}")
    print(f"  Tipo:     {imovel['tipo']}")
    print(f"  Valor:    R$ {imovel['valor']:,.2f}")
    print()

    valor_total = 0
for imovel in imoveis:
    valor_total += imovel["valor"]

print(f"Valor total da carteira: R$ {valor_total:,.2f}")