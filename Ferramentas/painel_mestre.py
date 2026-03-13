import os
import tkinter as tk
from tkinter import messagebox

# ==========================================
# CONFIGURAÇÕES DE ROTA
# ==========================================
diretorio_ferramentas = os.path.dirname(os.path.abspath(__file__))
caminho_memoria = os.path.join(diretorio_ferramentas, "memoria_pasta.txt")

# ==========================================
# FUNÇÕES DA INTERFACE (Apenas o Esqueleto por enquanto)
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

def acao_gerar_pdf():
    messagebox.showinfo("Aviso", "Aqui vamos plugar o gerar_relatorios.py")

# ==========================================
# CONSTRUÇÃO DO PAINEL (Interface minimalista)
# ==========================================
root = tk.Tk()
root.title("Inteligência de Mercado - Painel Mestre")
root.geometry("400x350")
root.resizable(False, False)
root.configure(padx=20, pady=20, bg="#f0f0f0")

# Título Principal
tk.Label(root, text="Esteira de Automação", font=("Segoe UI", 16, "bold"), bg="#f0f0f0").pack(pady=(0, 10))

# Status do Cliente (Painel Inteligente)
var_status = tk.StringVar()
atualizar_status()
label_status = tk.Label(root, textvariable=var_status, font=("Segoe UI", 10, "italic"), fg="#0052cc", bg="#f0f0f0")
label_status.pack(pady=(0, 20))

# Botões de Ação (A esteira de montagem)
largura_botao = 30
tk.Button(root, text="1. Iniciar Novo Projeto", font=("Segoe UI", 10), width=largura_botao, command=acao_iniciar).pack(pady=5)
tk.Button(root, text="2. Abrir Pasta do Cliente (TXTs)", font=("Segoe UI", 10), width=largura_botao, command=acao_abrir_pasta).pack(pady=5)
tk.Button(root, text="3. Armar Motor de Coleta (AHK)", font=("Segoe UI", 10), width=largura_botao, command=acao_ligar_ahk).pack(pady=5)
tk.Button(root, text="4. Emitir Relatório (PDF)", font=("Segoe UI", 10, "bold"), width=largura_botao, bg="#4CAF50", fg="white", command=acao_gerar_pdf).pack(pady=15)

# Botão para atualizar a memória manualmente, caso precise
tk.Button(root, text="↻ Atualizar Status", font=("Segoe UI", 8), bd=0, bg="#f0f0f0", fg="gray", command=atualizar_status).pack(side="bottom")

root.mainloop()