import re
import os
import glob
import configparser
import pdfkit
from pypdf import PdfReader

# ==========================================
# CONFIGURAÇÕES E ROTAS ABSOLUTAS
# ==========================================

# ==========================================
# CONTEÚDO DO RELATÓRIO (SISTEMA HÍBRIDO)
# ==========================================
# Variáveis de sistema (agora preenchidas automaticamente)
cliente = ""
amostragem = ""
tipo_negocio = ""

# Textos gerados pela Inteligência Artificial
insights = "• A humanização do atendimento presencial e a didática dos professores são os maiores retentores de alunos, com profissionais como Camila, Ricardo e Álvaro sendo elogiados nominalmente.<br><br>• A comunicação digital é um gargalo na concorrência, pois mensagens ignoradas no WhatsApp e esperas infinitas no telefone geram forte frustração.<br><br>• A desorganização administrativa, como atrasos de material didático e reajustes surpresa nas rematrículas, impulsiona o cancelamento repentino de contratos."
elogiado = "O fator humano é o ponto mais forte das escolas concorrentes. Os clientes valorizam professores engajados e metodologias dinâmicas que criam um ambiente acolhedor. O atendimento presencial ágil no momento da matrícula recebe muitos destaques positivos, assim como a boa infraestrutura física e a limpeza das instalações."
criticado = "A maior falha do mercado local reside na gestão administrativa e no suporte remoto. Os clientes relatam profunda frustração com o atendimento via WhatsApp e telefone, sentindo-se ignorados ao tentarem cancelar matrículas ou resolver problemas urgentes. A quebra de expectativa financeira com reajustes abusivos e a falta de organização para entrega de materiais pagos geram a maioria das avaliações destrutivas."
# ==========================================

diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
# O template fica na pasta do script (sua pasta de Ferramentas)
caminho_template = os.path.join(diretorio_raiz, "template.html")

# Rota cirúrgica para o motor gráfico (Caminho padrão de instalação no Windows)
caminho_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
configuracao = pdfkit.configuration(wkhtmltopdf=caminho_wkhtmltopdf)

def gerar_relatorio(pasta_alvo):
    global cliente, amostragem, tipo_negocio 

    # ==========================================
    # NOVIDADE: Leitura Dinâmica do INI
    # ==========================================
    print("Lendo as diretrizes do projeto...")
    arquivos_ini = glob.glob(os.path.join(pasta_alvo, "projeto*.ini"))
    if arquivos_ini:
        config = configparser.ConfigParser()
        config.read(arquivos_ini[0], encoding='utf-8')
        if config.has_section("PROJETO"):
            # A função .get() com fallback garante que o script não quebre se a chave mudar
            cliente = config.get("PROJETO", "nome", fallback=config.get("PROJETO", "cliente", fallback="Cliente_Sem_Nome"))
            tipo_negocio = config.get("PROJETO", "ramo", fallback=config.get("PROJETO", "tipo_negocio", fallback="ramo não informado"))
    else:
        print("Aviso: 'projeto*.ini' não encontrado na pasta do cliente.")
        cliente = "Cliente_Desconhecido"
        tipo_negocio = "ramo não informado"

    # ==========================================
    # ROTAS DIRECIONADAS PARA A PASTA DO CLIENTE
    # ==========================================
    caminho_pdf = os.path.join(pasta_alvo, f"Relatorio_{cliente}.pdf")
    caminho_txt = os.path.join(pasta_alvo, "reviews_concorrentes.txt")
    caminho_whatsapp = os.path.join(pasta_alvo, f"Relatorio_{cliente}_WhatsApp.txt")

    print("Lendo o arquivo de avaliações...")
    if os.path.exists(caminho_txt):
        with open(caminho_txt, 'r', encoding='utf-8') as f:
            amostragem = str(len(f.readlines()))
    else:
        amostragem = "0"
        print("Aviso: 'reviews_concorrentes.txt' não encontrado na pasta do cliente.")

    # Força tudo para minúsculo e remove espaços em branco nas pontas
    tipo_negocio = tipo_negocio.lower().strip()

    print("Lendo o molde HTML...")
    
    if not os.path.exists(caminho_template):
        print("Erro: O arquivo 'template.html' não foi encontrado na pasta de ferramentas.")
        return

    with open(caminho_template, 'r', encoding='utf-8') as f:
        html_base = f.read()

    print("Injetando os dados da inteligência...")
    
    # ==========================================
    # FILTRO CIRÚRGICO: Limpa as citações da IA
    # ==========================================
    gatilho = "ci" + "te:"
    padrao_citacao = r'\s*\[' + gatilho + r'.*?\]'
    
    insights_limpo = re.sub(padrao_citacao, '', insights)
    elogiado_limpo = re.sub(padrao_citacao, '', elogiado)
    criticado_limpo = re.sub(padrao_citacao, '', criticado)

    # ==========================================
    # GERAÇÃO DO RELATÓRIO PARA WHATSAPP
    # ==========================================
    print("Gerando versão otimizada para WhatsApp...")
    
    # Converte as quebras de linha do HTML para texto puro
    insights_wa = insights_limpo.replace("<br>", "\n")
    elogiado_wa = elogiado_limpo.replace("<br>", "\n")
    criticado_wa = criticado_limpo.replace("<br>", "\n")
    
    texto_whatsapp = f"""*Relatório de Inteligência de Mercado*
*Cliente:* {cliente}
*Amostragem:* {amostragem} avaliações extraídas.

*Insights Estratégicos*
{insights_wa}

*Tópico Mais Elogiado*
{elogiado_wa}

*Tópico Mais Criticado*
{criticado_wa}

_Tecnologia e Automação por Semmler Automações_"""

    # Salva o texto pronto na pasta do cliente
    with open(caminho_whatsapp, 'w', encoding='utf-8') as f:
        f.write(texto_whatsapp)

    # Opções de engenharia para o PDF
    opcoes = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'encoding': "UTF-8",
        'enable-local-file-access': None
    }

    # ==========================================
    # MOTOR ADAPTATIVO: Testa os tamanhos de fonte
    # ==========================================
    tamanhos_teste = [22, 21, 20, 19, 18, 17, 16, 15, 14]
    
    for tamanho in tamanhos_teste:
        print(f"Testando renderização com fonte de {tamanho}px...")
        
        # Substituição em cascata a cada nova tentativa
        html_final = html_base.replace("{{CLIENTE}}", cliente)
        html_final = html_final.replace("{{AMOSTRAGEM}}", amostragem)
        html_final = html_final.replace("{{TIPO_NEGOCIO}}", tipo_negocio)
        html_final = html_final.replace("{{INSIGHTS}}", insights_limpo)
        html_final = html_final.replace("{{ELOGIADO}}", elogiado_limpo)
        html_final = html_final.replace("{{CRITICADO}}", criticado_limpo)
        
        # Substitui apenas a linha que tem a assinatura alvo-dinamico
        html_final = html_final.replace("font-size: 18px; /* alvo-dinamico */", f"font-size: {tamanho}px; /* alvo-dinamico */")

        try:
            # Gera o PDF (vai sobrescrever se já existir)
            pdfkit.from_string(html_final, caminho_pdf, configuration=configuracao, options=opcoes)
            
            # Lê o arquivo que acabou de ser criado para conferir as páginas
            leitor = PdfReader(caminho_pdf)
            numero_paginas = len(leitor.pages)
            
            if numero_paginas == 1:
                print(f"\nSucesso absoluto! Relatório de 1 página gerado com fonte {tamanho}px em '{pasta_alvo}'.")
                break # Interrompe o loop, pois o objetivo foi alcançado
            else:
                print(f"O relatório gerou {numero_paginas} páginas. Reduzindo para o próximo tamanho...")
                
        except Exception as e:
            print(f"\nErro ao gerar o PDF: {e}")
            break # Se der erro no motor wkhtmltopdf, para tudo para não ficar travado

# ==========================================
# GATILHO DE EXECUÇÃO AUTOMÁTICO
# ==========================================
if __name__ == "__main__":
    caminho_memoria = os.path.join(diretorio_raiz, "memoria_pasta.txt")
    
    try:
        # Lê o caminho da pasta do cliente salvo na memória
        with open(caminho_memoria, "r", encoding="utf-8") as f:
            pasta_selecionada = f.read().strip()
        
        # Se a pasta existir no disco, dispara o motor
        if os.path.exists(pasta_selecionada):
            print(f"Iniciando a geração do relatório para a pasta:\n{pasta_selecionada}\n")
            gerar_relatorio(pasta_selecionada)
        else:
            print(f"Erro: A pasta do cliente registrada não existe no computador: {pasta_selecionada}")
            
    except FileNotFoundError:
        print("Erro: Arquivo 'memoria_pasta.txt' não encontrado. Você precisa rodar as etapas anteriores primeiro.")