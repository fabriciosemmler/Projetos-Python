import os
import tkinter as tk
from tkinter import messagebox
import webbrowser

# ==========================================
# CONFIGURAÇÕES DE ROTA
# ==========================================
diretorio_ferramentas = os.path.dirname(os.path.abspath(__file__))
caminho_memoria = os.path.join(diretorio_ferramentas, "memoria_pasta.txt")

# ==========================================
# FUNÇÕES DA INTERFACE (Esqueleto com ações)
# ==========================================
def atualizar_status():
    """Lê a memória para saber quem é o cliente atual e atualiza o painel"""
    try:
        with open(caminho_memoria, "r", encoding="utf-8") as f:
            pasta_atual = f.read().strip()
            # Extrai apenas o nome final da pasta para ficar bonito na tela
            nome_cliente = os.path.basename(pasta_atual)
            if nome_cliente:
                var_status.set(f"Alvo Atual: {nome_cliente}")
            else:
                var_status.set("Alvo Atual: Nenhum projeto ativo")
    except FileNotFoundError:
        var_status.set("Alvo Atual: Nenhum projeto ativo")

def acao_iniciar():
    messagebox.showinfo("Aviso", "Aqui vamos plugar o iniciar_projeto.py")

def acao_abrir_pasta():
    messagebox.showinfo("Aviso", "Aqui vamos plugar o atalho da pasta")

def acao_ligar_ahk():
    messagebox.showinfo("Aviso", "Aqui vamos plugar o obter_html.ahk")

def acao_abrir_gemini():
    # Bônus de engenharia: O botão já abre o navegador no Gemini para você
    webbrowser.open("https://gemini.google.com/app/2267c167a9509945")

def acao_gerar_pdf():
    messagebox.showinfo("Aviso", "Aqui vamos plugar o gerar_relatorios.py")

# ==========================================
# CONSTRUÇÃO DO PAINEL (Interface minimalista)
# ==========================================
root = tk.Tk()
root.title("Semmler Micro-Automações - Painel Mestre")

# --- Centralização Cirúrgica da Janela ---
# Aumentamos a altura para 580 para acomodar o novo passo perfeitamente
largura_janela = 480
altura_janela = 580
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

pos_x = int((largura_tela / 2) - (largura_janela / 2))
pos_y = int((altura_tela / 2) - (altura_janela / 2))

root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
# -----------------------------------------

root.resizable(False, False)
root.configure(padx=20, pady=15, bg="#f0f0f0")

# Título Principal
tk.Label(root, text="Esteira de Automação", font=("Segoe UI", 16, "bold"), bg="#f0f0f0").pack(pady=(0, 5))

# Status do Cliente (Painel Inteligente)
var_status = tk.StringVar()
atualizar_status()
label_status = tk.Label(root, textvariable=var_status, font=("Segoe UI", 10, "italic"), fg="#0052cc", bg="#f0f0f0")
label_status.pack(pady=(0, 15))

# ==========================================
# BOTÕES E INSTRUÇÕES
# ==========================================
largura_botao = 40
fonte_instrucao = ("Segoe UI", 8, "italic")
cor_instrucao = "#555555"

# Passo 1
tk.Button(root, text="1. Iniciar Novo Projeto", font=("Segoe UI", 10), width=largura_botao, command=acao_iniciar).pack(pady=(5, 5))

# Passo 2 + Instrução
tk.Button(root, text="2. Abrir Pasta do Cliente", font=("Segoe UI", 10), width=largura_botao, command=acao_abrir_pasta).pack(pady=(15, 0))
tk.Label(root, text="↳ Copiar URLs do Google Maps para o lista_concorrentes.txt", font=fonte_instrucao, fg=cor_instrucao, bg="#f0f0f0").pack(pady=(0, 5))

# Passo 3
tk.Button(root, text="3. Armar Motor de Coleta (AHK)", font=("Segoe UI", 10), width=largura_botao, command=acao_ligar_ahk).pack(pady=(15, 5))
# A ação humana de apertar F11 é intuitiva, mantemos limpo.

# Passo 4 + Instruções
tk.Button(root, text="4. Extração de Inteligência (Gemini)", font=("Segoe UI", 10), width=largura_botao, command=acao_abrir_gemini).pack(pady=(15, 0))
tk.Label(root, text="↳ Fazer upload do reviews_concorrentes.txt e apertar Ctrl + F18", font=fonte_instrucao, fg=cor_instrucao, bg="#f0f0f0").pack(pady=(0, 0))
tk.Label(root, text="↳ Copiar o rascunho, limpar c/ Ctrl + Alt + L e enviar p/ redatora", font=fonte_instrucao, fg=cor_instrucao, bg="#f0f0f0").pack(pady=(0, 0))
tk.Label(root, text="↳ Colar o texto aprovado no redacao_final.txt", font=fonte_instrucao, fg=cor_instrucao, bg="#f0f0f0").pack(pady=(0, 5))

# Passo 5
tk.Button(root, text="5. Emitir Relatório (PDF e Whatsapp)", font=("Segoe UI", 10, "bold"), width=largura_botao, bg="#4CAF50", fg="white", command=acao_gerar_pdf).pack(pady=(20, 5))

# Botão para atualizar a memória manualmente
tk.Button(root, text="↻ Atualizar Status", font=("Segoe UI", 8), bd=0, bg="#f0f0f0", fg="gray", command=atualizar_status).pack(side="bottom")

root.mainloop()