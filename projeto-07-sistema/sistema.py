# sistema.py
# Arquivo principal — menu de navegação

from leads import cadastrar_lead, listar_leads
from relatorio import salvar_relatorio

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