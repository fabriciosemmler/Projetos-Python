import re
import os
from bs4 import BeautifulSoup

def filtrar_vagas(html_entrada, html_saida):
    with open(html_entrada, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    vagas_filtradas = []
    
    # O PCI Concursos agrupa cada vaga em containers com a classe 'ca'
    blocos = soup.find_all(['div', 'article'], class_='ca')
    
    for bloco in blocos:
        texto = bloco.get_text()
        
        # Captura padrões como "R$ 5.000,00" ou "R$ 8000,00"
        padrao = r'R\$\s*([\d\.]+(?:,\d{2}))'
        valores_str = re.findall(padrao, texto)
        
        # Converte os valores encontrados para float (remove ponto de milhar, ajusta vírgula decimal)
        valores = [float(v.replace('.', '').replace(',', '.')) for v in valores_str]
        
        # Se qualquer salário mencionado no bloco da vaga estiver dentro do alvo, ela é aprovada
        if any(5000 <= v <= 10000 for v in valores):
            vagas_filtradas.append(str(bloco))

    # Monta a estrutura HTML mínima e limpa para o arquivo de saída
    html_final = f"""<!DOCTYPE html>
    <html lang="pt-BR">
    <head><meta charset="utf-8"><title>Vagas Filtradas</title></head>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h2>Vagas Encontradas (R$ 5.000 a R$ 10.000)</h2>
        <hr>
        {'<br><hr>'.join(vagas_filtradas) or '<p>Nenhuma vaga atende ao critério.</p>'}
    </body>
    </html>"""

    with open(html_saida, 'w', encoding='utf-8') as f:
        f.write(html_final)
        
    print(f"Execução concluída. {len(vagas_filtradas)} vagas salvas em '{html_saida}'.")

if __name__ == '__main__':
    # Identifica a pasta exata onde este script de Python está salvo
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    
    # Cria os caminhos absolutos para os arquivos
    arquivo_entrada = os.path.join(diretorio_script, 'pci.html')
    arquivo_saida = os.path.join(diretorio_script, 'vagas_filtradas.html')
    
    filtrar_vagas(arquivo_entrada, arquivo_saida)