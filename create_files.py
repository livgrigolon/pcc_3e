import os

# Defina a pasta onde os arquivos serão criados
pasta = "python_work/chapter_04"

# Loop para criar os arquivos
for i in range(1, 16):
    nome_arquivo = f"4.{i}.py"
    caminho = os.path.join(pasta, nome_arquivo)
    
    # Cria o arquivo vazio (ou escreve algo dentro se quiser)
    # with open(caminho, "w", encoding="utf-8") as f:
        # f.write(f"# Arquivo {nome_arquivo}\n")
    
    # Cria o arquivo vazio
    open(caminho, "a").close()
    
print("Arquivos criados com sucesso!")