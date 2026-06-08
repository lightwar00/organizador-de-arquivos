import os
import getpass

from config import criar_pastas
from config import organizar_arquivos

# Para pegar o nome do usuário do computador e dar as boas vindas!
nome_usuario = getpass.getuser()
print(f"Olá, {nome_usuario}! Seja bem-vindo.")

# Caso dê erro ou digite algo alem do solicitado
while True:
    print("\n=== ASSISTENTE DE ORGANIZAÇÃO ===")
    print("1 - Organizar programas")  
    print("2 - Sair do Programa")
    print("=====================================")
    
    opcao = input("Escolha uma opção (1 ou 2): ")
    
    if opcao == "1":
        print("\n[Iniciando organização de Programas...]")
        
        pasta_downloads_exclusiva = os.path.join("C:\\Users", nome_usuario, "Downloads")
        
        criar_pastas(pasta_downloads_exclusiva)
        organizar_arquivos(pasta_downloads_exclusiva)        
    elif opcao == "2":
        print(f"\nEncerrando a atividade... Até logo!")
        break  
    else:
        print(f"\nOpção inválida! Por favor, digite 1 ou 2.")
