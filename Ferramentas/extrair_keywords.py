import os
import re
from collections import Counter

def descobrir_palavras_chave(arquivo_entrada, arquivo_saida, top_n=3):
    # 1. Filtro de ruído cirúrgico (Stop Words)
    # Palavras que não agregam valor ao nome do negócio
    stop_words = {"de", "da", "do", "das", "dos", "e", "em", "na", "no", 
                  "ltda", "me", "cia", "o", "a", "os", "as", "com", "para"}

    try:
        # 2. Leitura com proteção de caracteres (UTF-8 evita erros de acento)
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            texto = f.read().lower()

        # 3. Limpeza: Extrai apenas letras (incluindo acentos), ignora números e traços
        palavras = re.findall(r'\b[a-zà-ú]+\b', texto)
        
        # 4. Refino: Mantém apenas palavras úteis maiores que 2 letras
        palavras_uteis = [p for p in palavras if p not in stop_words and len(p) > 2]

        # 5. O Motor Matemático (Counter é nativo e extremamente rápido)
        contagem = Counter(palavras_uteis)
        
        # 6. Extrai as vencedoras
        top_palavras = [palavra for palavra, freq in contagem.most_common(top_n)]

        # 7. Salva o resultado em um arquivo de texto limpo para o AHK ler depois
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(", ".join(top_palavras))

    except FileNotFoundError:
        # Se o arquivo não existir, criamos um arquivo vazio para não quebrar o AHK
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write("")

if __name__ == "__main__":
    try:
        # --- AJUSTE CIRÚRGICO ---
        # Descobre o diretório exato onde este script .py está salvo
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        caminho_memoria = os.path.join(diretorio_script, "memoria_pasta.txt")
        
        # Lê o caminho da pasta do cliente salvo pelo AHK (agora usando o caminho absoluto)
        with open(caminho_memoria, "r", encoding="utf-8") as f:
            pasta_cliente = f.read().strip()
        
        # Constrói os caminhos absolutos de forma segura (independente de ter barra no final ou não)
        caminho_entrada = os.path.join(pasta_cliente, "lista_concorrentes.txt")
        caminho_saida = os.path.join(pasta_cliente, "palavras_chave.txt")
        
        # Executa o motor na pasta correta
        descobrir_palavras_chave(caminho_entrada, caminho_saida, top_n=3)
        
    except FileNotFoundError:
        print("Arquivo memoria_pasta.txt não encontrado. Execute o script AHK primeiro.")