import os
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

def extrair_dados():
    # ==========================================
    # NOVIDADE: Seleção Dinâmica da Pasta do Cliente
    # ==========================================
    # Inicia a janela invisível e força ela para a frente de tudo
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    # Abre o seletor pedindo a pasta principal do cliente
    pasta_cliente = filedialog.askdirectory(title="Selecione a pasta do cliente (ex: Acqua Lavanderia)")
    
    # Limpa a memória da janela
    root.destroy()
    
    # Se você cancelar a janela, aborta o script
    if not pasta_cliente:
        print("Operação cancelada.")
        return

    # Constrói os caminhos blindados baseados na pasta escolhida
    pasta_html = os.path.join(pasta_cliente, "paginas_html")
    arquivo_saida = os.path.join(pasta_cliente, "reviews_concorrentes.txt")

    print(f"Alvo selecionado: {pasta_cliente}")
    print("Iniciando a extração cirúrgica de avaliações...\n")
    
    if not os.path.exists(pasta_html):
        print(f"Erro: A subpasta 'paginas_html' não foi encontrada dentro do cliente.")
        return

    arquivos = [f for f in os.listdir(pasta_html) if f.endswith('.html')]
    total_avaliacoes = 0

    # Abre o arquivo de saída na pasta do cliente ('w' limpa o arquivo antigo)
    with open(arquivo_saida, 'w', encoding='utf-8') as f_out:
        
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_html, arquivo)
            print(f"Processando: {arquivo}", end="... ")
            
            # Lê o código-fonte do HTML salvo
            with open(caminho_completo, 'r', encoding='utf-8') as f_in:
                sopa = BeautifulSoup(f_in, 'html.parser')
                
                # Busca exata por todas as tags com a classe que mapeamos
                avaliacoes = sopa.find_all('span', class_='wiI7pd')
                
                contador_local = 0
                for avaliacao in avaliacoes:
                    # Extrai apenas o texto, ignorando outras tags internas (como emojis ou links)
                    texto = avaliacao.get_text(separator=" ", strip=True)
                    
                    # Achata o texto para garantir que fique em uma única linha no .txt final
                    texto_limpo = texto.replace('\n', ' ').replace('\r', '')
                    
                    # Salva no arquivo de texto apenas se não for uma string vazia
                    if texto_limpo:
                        f_out.write(f"{texto_limpo}\n")
                        contador_local += 1
                        total_avaliacoes += 1
                        
            print(f"[{contador_local} extraídas]")
            
    print(f"\nFinalizado! {total_avaliacoes} avaliações consolidadas no arquivo 'reviews_concorrentes.txt'.")

# Executa a função
if __name__ == "__main__":
    extrair_dados()