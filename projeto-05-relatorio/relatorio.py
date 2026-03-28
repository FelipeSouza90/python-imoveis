# Projeto 05 - Gerador de Relatório de Visitas
# Autor: Felipe Souza
# Descrição: Registra visitas do dia e salva em arquivo .txt

from datetime import datetime

print("===== GERADOR DE RELATÓRIO DE VISITAS =====\n")

# Pega a data e hora atual automaticamente
data_hoje = datetime.now().strftime("%d/%m/%Y")
hora_atual = datetime.now().strftime("%H:%M")

corretor = input("Nome do corretor: ")
quantidade = int(input("Quantas visitas realizou hoje? "))

visitas = []

for i in range(quantidade):
    print(f"\nVisita {i + 1}:")
    endereco = input("  Endereço do imóvel: ")
    cliente = input("  Nome do cliente: ")
    interesse = input("  Nível de interesse (alto/médio/baixo): ")
    observacao = input("  Observação: ")

    visita = {
        "endereco": endereco,
        "cliente": cliente,
        "interesse": interesse,
        "observacao": observacao
    }

    visitas.append(visita)

    nome_arquivo = f"relatorio_{data_hoje.replace('/', '-')}_{corretor.replace(' ', '_')}.txt"

with open(nome_arquivo, "w", encoding="utf-8") as f:
    f.write("=" * 50 + "\n")
    f.write(f"RELATÓRIO DE VISITAS\n")
    f.write(f"Data: {data_hoje} | Hora: {hora_atual}\n")
    f.write(f"Corretor: {corretor}\n")
    f.write(f"Total de visitas: {quantidade}\n")
    f.write("=" * 50 + "\n\n")

    for i, visita in enumerate(visitas):
        f.write(f"Visita {i + 1}\n")
        f.write(f"  Endereço:  {visita['endereco']}\n")
        f.write(f"  Cliente:   {visita['cliente']}\n")
        f.write(f"  Interesse: {visita['interesse']}\n")
        f.write(f"  Observação: {visita['observacao']}\n")
        f.write("\n")

    f.write("=" * 50 + "\n")
    f.write("Relatório gerado automaticamente pelo sistema.\n")

print(f"\n✅ Relatório salvo com sucesso: {nome_arquivo}")

nome_arquivo = f"relatorio_{data_hoje.replace('/', '-')}_{corretor.replace(' ', '_')}.txt"

with open(nome_arquivo, "w", encoding="utf-8") as f:
    f.write("=" * 50 + "\n")
    f.write(f"RELATÓRIO DE VISITAS\n")
    f.write(f"Data: {data_hoje} | Hora: {hora_atual}\n")
    f.write(f"Corretor: {corretor}\n")
    f.write(f"Total de visitas: {quantidade}\n")
    f.write("=" * 50 + "\n\n")

    for i, visita in enumerate(visitas):
        f.write(f"Visita {i + 1}\n")
        f.write(f"  Endereço:  {visita['endereco']}\n")
        f.write(f"  Cliente:   {visita['cliente']}\n")
        f.write(f"  Interesse: {visita['interesse']}\n")
        f.write(f"  Observação: {visita['observacao']}\n")
        f.write("\n")

    f.write("=" * 50 + "\n")
    f.write("Relatório gerado automaticamente pelo sistema.\n")

print(f"\n✅ Relatório salvo com sucesso: {nome_arquivo}")