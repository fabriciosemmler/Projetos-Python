import re
import os
from bs4 import BeautifulSoup

def filtrar_por_volume(html_entrada, html_saida, minimo_vagas=20):
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho_in = os.path.join(diretorio, html_entrada)
    caminho_out = os.path.join(diretorio, html_saida)

    if not os.path.exists(caminho_in):
        print(f"Erro: O arquivo {html_entrada} não foi encontrado.")
        return

    with open(caminho_in, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    vagas_selecionadas = []
    # No seu vagas_filtradas.html, as vagas estão dentro de blocos 'div' ou 'article'
    blocos = soup.find_all(['div', 'article'], class_='ca')

    for bloco in blocos:
        texto = bloco.get_text()
        
        # Regex: procura números seguidos de "vaga" ou "vagas"
        # Ex: "50 vagas", "120 vaga"
        matches = re.findall(r'(\d+)\s*vagas?', texto, re.IGNORECASE)
        
        # Converte para inteiro e verifica se algum valor supera o limite
        contagens = [int(n) for n in matches]
        
        if any(n > minimo_vagas for n in contagens):
            vagas_selecionadas.append(str(bloco))

    # Gera o novo arquivo filtrado
    html_final = f"""<!DOCTYPE html>
    <html lang="pt-BR">
    <head><meta charset="utf-8"><title>Oportunidades > {minimo_vagas} Vagas</title></head>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h2>Vagas com alta densidade (+ de {minimo_vagas} postos)</h2>
        <hr>
        {'<br><hr>'.join(vagas_selecionadas) or '<p>Nenhuma vaga com esse volume foi encontrada.</p>'}
    </body>
    </html>"""

    with open(caminho_out, 'w', encoding='utf-8') as f:
        f.write(html_final)
        
    print(f"Sucesso! {len(vagas_selecionadas)} vagas de alto volume salvas em '{html_saida}'.")

if __name__ == '__main__':
    # Ele pega o que o primeiro script gerou e refina
    filtrar_por_volume('vagas_filtradas.html', 'vagas_volume.html')