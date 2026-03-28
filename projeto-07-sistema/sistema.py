# Projeto 07 - Sistema de Gestão de Leads Imobiliários
# Autor: Felipe Souza
# Descrição: Sistema completo para cadastrar, analisar e gerenciar leads

import requests
from datetime import datetime

# ---- BANCO DE DADOS EM MEMÓRIA ----
leads = []

def buscar_cep(cep):
    cep = cep.replace("-", "")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                return dados
    except:
        pass
    return None

def cadastrar_lead():
    print("\n===== CADASTRAR NOVO LEAD =====")
    nome = input("Nome do lead: ")
    telefone = input("Telefone: ")
    cep = input("CEP do imóvel de interesse: ")
    renda = float(input("Renda mensal (R$): "))
    valor_imovel = float(input("Valor do imóvel de interesse (R$): "))
    entrada = float(input("Valor da entrada (R$): "))
    prazo_anos = int(input("Prazo do financiamento (anos): "))
    taxa_juros = float(input("Taxa de juros anual (%): "))

    print("\n🔍 Buscando endereço...")
    dados_cep = buscar_cep(cep)

    if dados_cep:
        endereco = f"{dados_cep['logradouro']}, {dados_cep['bairro']}, {dados_cep['localidade']} - {dados_cep['uf']}"
        print(f"✅ Endereço encontrado: {endereco}")
    else:
        endereco = cep
        print("⚠️ CEP não encontrado. Salvando somente o CEP.")

    valor_financiado = valor_imovel - entrada
    prazo_meses = prazo_anos * 12
    taxa_mensal = taxa_juros / 100 / 12
    parcela = (valor_financiado * taxa_mensal) / (1 - (1 + taxa_mensal) ** -prazo_meses)
    limite_parcela = renda * 0.30

    if parcela <= limite_parcela:
        perfil = "✅ APROVADO"
    else:
        perfil = "❌ REPROVADO"

    lead = {
        "nome": nome,
        "telefone": telefone,
        "endereco": endereco,
        "renda": renda,
        "valor_imovel": valor_imovel,
        "parcela": parcela,
        "perfil": perfil,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    leads.append(lead)
    print(f"\n{perfil} — Lead cadastrado com sucesso!")

def listar_leads():
    print("\n===== LEADS CADASTRADOS =====")

    if len(leads) == 0:
        print("Nenhum lead cadastrado ainda.")
        return

    for i, lead in enumerate(leads):
        print(f"\nLead {i + 1}")
        print(f"  Nome:        {lead['nome']}")
        print(f"  Telefone:    {lead['telefone']}")
        print(f"  Endereço:    {lead['endereco']}")
        print(f"  Renda:       R$ {lead['renda']:,.2f}")
        print(f"  Imóvel:      R$ {lead['valor_imovel']:,.2f}")
        print(f"  Parcela:     R$ {lead['parcela']:,.2f}")
        print(f"  Perfil:      {lead['perfil']}")
        print(f"  Cadastrado:  {lead['data']}")

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

def menu():
    while True:
        print("\n===== SISTEMA DE GESTÃO DE LEADS =====")
        print("1. Cadastrar novo lead")
        print("2. Listar todos os leads")
        print("3. Salvar relatório")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_lead()
        elif opcao == "2":
            listar_leads()
        elif opcao == "3":
            salvar_relatorio()
        elif opcao == "4":
            print("\n👋 Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")

# ---- INICIA O PROGRAMA ----
menu()