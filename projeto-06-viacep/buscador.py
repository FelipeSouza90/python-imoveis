# Projeto 06 - Buscador de Endereço por CEP
# Autor: Felipe Souza
# Descrição: Busca endereço completo via CEP usando a API do ViaCEP

import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" not in dados:
            return dados
        else:
            return None
    else:
        return None

def exibir_endereco(dados):
    print("\n===== ENDEREÇO ENCONTRADO =====")
    print(f"CEP:          {dados['cep']}")
    print(f"Logradouro:   {dados['logradouro']}")
    print(f"Complemento:  {dados['complemento']}")
    print(f"Bairro:       {dados['bairro']}")
    print(f"Cidade:       {dados['localidade']}")
    print(f"Estado:       {dados['uf']}")

# ---- PROGRAMA PRINCIPAL ----
print("===== BUSCADOR DE ENDEREÇO POR CEP =====\n")

cep = input("Digite o CEP (somente números): ")
cep = cep.replace("-", "")

dados = buscar_cep(cep)

if dados:
    exibir_endereco(dados)
else:
    print("\n❌ CEP não encontrado. Verifique e tente novamente.")