# cep.py
# Responsável pela busca de endereço via API ViaCEP

import requests

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