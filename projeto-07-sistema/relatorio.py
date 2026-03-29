# relatorio.py
# Responsável por salvar o relatório em arquivo .txt

from datetime import datetime
from leads import leads

def salvar_relatorio():
    if len(leads) == 0:
        print("\n⚠️ Nenhum lead para salvar.")
        return

    data_hoje = datetime.now().strftime("%d-%m-%Y_%H-%M")
    nome_arquivo = f"relatorio_leads_{data_hoje}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("RELATÓRIO DE LEADS IMOBILIÁRIOS\n")
        f.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        f.write(f"Total de leads: {len(leads)}\n")
        f.write("=" * 50 + "\n\n")

        aprovados = [l for l in leads if "APROVADO" in l['perfil']]
        reprovados = [l for l in leads if "REPROVADO" in l['perfil']]

        f.write(f"✅ Aprovados: {len(aprovados)}\n")
        f.write(f"❌ Reprovados: {len(reprovados)}\n\n")

        for i, lead in enumerate(leads):
            f.write(f"Lead {i + 1}\n")
            f.write(f"  Nome:      {lead['nome']}\n")
            f.write(f"  Telefone:  {lead['telefone']}\n")
            f.write(f"  Endereço:  {lead['endereco']}\n")
            f.write(f"  Renda:     R$ {lead['renda']:,.2f}\n")
            f.write(f"  Imóvel:    R$ {lead['valor_imovel']:,.2f}\n")
            f.write(f"  Parcela:   R$ {lead['parcela']:,.2f}\n")
            f.write(f"  Perfil:    {lead['perfil']}\n")
            f.write(f"  Data:      {lead['data']}\n\n")

        f.write("=" * 50 + "\n")
        f.write("Relatório gerado automaticamente pelo sistema.\n")

    print(f"\n✅ Relatório salvo: {nome_arquivo}")