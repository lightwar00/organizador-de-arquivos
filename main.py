import os
import getpass

from config import criar_pastas
from config import organizar_arquivos

#para pegar o nome do usuário do computador e dar as boas vindas!
nome_usuario = getpass.getuser()
print(f"Olá, {nome_usuario}! Seja bem-vindo.")

# O loop 'while True' faz o menu ficar aparecendo repetidamente
while True:
    print("\n=== ASSISTENTE DE ORGANIZAÇÃO ===")
    print("1 - Organizar programas")  
    print("2 - Sair do Programa")
    print("=====================================")
    
    # Captura a escolha do usuário
    opcao = input("Escolha uma opção (1 ou 2): ")
    
    # Testando as opções com if/elif/else
    if opcao == "1":
        print("\n[Iniciando organização de Programas...]")
        
        # 1. Montamos o caminho direto e exclusivo do Downloads: C:\Users\computador\Downloads
        pasta_downloads_exclusiva = os.path.join("C:\\Users", nome_usuario, "Downloads")
        
        # 2. Passamos ESSE caminho do Downloads para as funções trabalharem apenas nele!
        criar_pastas(pasta_downloads_exclusiva)
        organizar_arquivos(pasta_downloads_exclusiva)        
    elif opcao == "2":
        print(f"\nEncerrando a atividade... Até logo!")
        break  # O comando 'break' quebra o 'while True' e fecha o programa de vez!
        
    else:
        print(f"\nOpção inválida! Por favor, digite 1 ou 2.")