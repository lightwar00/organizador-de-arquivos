import os
import shutil

# 1. Função para criar as pastas de destino
def criar_pastas(caminho_download):
    caminho_usuario = os.path.dirname(caminho_download)
    
    pastas_destino = {
        #"DOCUMENTOS": os.path.join(caminho_usuario, "Documents", "Meus_Documentos_Python"),
        #"IMAGENS": os.path.join(caminho_usuario, "Pictures", "Minhas_Imagens_Python"),
        #"MUSICAS": os.path.join(caminho_usuario, "Music", "Minhas_Musicas_Python"),
        #"PROGRAMAS_COMPACTADOS": os.path.join(caminho_downloads, "Meus_Programas_Python"),
        "OUTROS": os.path.join(caminho_download)
    }
    
    for nome_pasta, caminho_completo in pastas_destino.items():
        if not os.path.exists(caminho_completo):
            os.makedirs(caminho_completo)


# 2. Função para analisar as pastas e guardar os arquivos
def organizar_arquivos(caminho_downloads):
    extensoes = {
        "DOCUMENTOS": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt"],
        "IMAGENS": [".png", ".jpg", ".jpeg", ".gif"],
        "MUSICAS": [".mp3", ".wav", ".flac"],
        "PROGRAMAS_COMPACTADOS": [".exe", ".zip", ".rar", ".7z"]
    }

    caminho_usuario = os.path.dirname(caminho_downloads)
    
    pastas_destino = {
        #"DOCUMENTOS": os.path.join(caminho_usuario, "Documents", "Meus_Documentos_Python"),
        #"IMAGENS": os.path.join(caminho_usuario, "Pictures", "Minhas_Imagens_Python"),
        #"MUSICAS": os.path.join(caminho_usuario, "Music", "Minhas_Musicas_Python"),
        #"PROGRAMAS_COMPACTADOS": os.path.join(caminho_downloads, "Meus_Programas_Python"),
        "OUTROS": os.path.join(caminho_downloads)
    }

    for arquivo in os.listdir(caminho_downloads):
        caminho_original = os.path.join(caminho_downloads, arquivo)
        if os.path.isdir(caminho_original):
            continue

        _, extensao = os.path.splitext(arquivo.lower())
        moveu = False

        # Rodar o dicionário de extensões
        for pasta_destino, lista_extensoes in extensoes.items():
            if extensao in lista_extensoes:
                caminho_destino = pastas_destino[pasta_destino]
                try:
                    shutil.move(caminho_original, caminho_destino)
                    print(f"Arquivo {arquivo} movido para {pasta_destino}!")
                except Exception as e:
                    print(f"Erro ao mover {arquivo}: {e}")
                moveu = True
                break

        # Se não achou na lista, vai para a pasta OUTROS
        if not moveu:
            caminho_outros = pastas_destino["OUTROS"]
            try:
                shutil.move(caminho_original, caminho_outros)
                print(f"Arquivo {arquivo} movido para OUTROS!")
            except Exception as e:
                print(f"Erro ao mover {arquivo}: {e}")
