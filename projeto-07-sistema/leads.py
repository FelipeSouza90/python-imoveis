# leads.py
# Responsável pelo cadastro e listagem de leads

from datetime import datetime
from cep import buscar_cep

# ---- BANCO DE DADOS EM MEMÓRIA ----
leads = []

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