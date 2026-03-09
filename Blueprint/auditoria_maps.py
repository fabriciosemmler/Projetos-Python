from playwright.sync_api import sync_playwright
import time

# ==========================================
# MÓDULO 1: Configuração de Alvos
# ==========================================
lista_ids = [
    "ChIJX663W_FZzpQR_p_R5-Gf-k8",
    "ChIJx2V7nS9ZzpQRyq_9m2X-k-8",
    "ChIJT97nS9ZzpQRyq_9m2X-k-8",
    "ChIJxbZHXF5ZzpQR2VAuQ6h4Ccw",
    "ChIJAe5bGqtZzpQR92aZo6Sy1ec",
    "ChIJS-R1T9TVmwARKkzGsEx69KI",
    "ChIJden528dZzpQRCQfyVCEYRXw"
]

# ==========================================
# MÓDULO 2: Motor de Extração (O Coletor)
# ==========================================
def coletar_avaliacoes(ids):
    # Inicia o navegador invisível (headless=True) para poupar processamento
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        todas_reviews = ""

        for pid in ids:
            # URL oficial do Google para abrir um local direto pelo ID
            url = f"https://www.google.com/maps/search/?api=1&query=Google&query_place_id={pid}"
            
            print(f"Acessando ID: {pid}...")
            page.goto(url)
            
            # Aguarda 5 segundos para o JavaScript do Maps carregar completamente
            time.sleep(5) 
            
            # '.wiI7pd' é a classe padrão atual do Google para os textos de avaliação
            reviews = page.query_selector_all('.wiI7pd')
            
            print(f" -> Coletadas {len(reviews)} avaliações na primeira dobra da página.")
            
            for r in reviews:
                texto = r.inner_text().strip()
                if texto: # Filtra para ignorar avaliações que só têm estrelas e nenhum texto
                    todas_reviews += texto + "\n---\n"
        
        browser.close()
        return todas_reviews

# ==========================================
# EXECUÇÃO DO FLUXO
# ==========================================
if __name__ == "__main__":
    print("Iniciando auditoria de sentimento da Semmler Automação...")
    dados_brutos = coletar_avaliacoes(lista_ids)
    
    # Exporta para um arquivo .txt limpo e leve
    nome_arquivo = "reviews_concorrentes.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(dados_brutos)
        
    print(f"\nSucesso cirúrgico! Arquivo '{nome_arquivo}' gerado e pronto para a IA.")