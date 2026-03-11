import os
import keyboard
import tkinter as tk
from tkinter import filedialog

def inicializar_pasta_cliente():
    # Inicia o Tkinter e esconde a janela base
    root = tk.Tk()
    root.withdraw()
    
    # O truque cirúrgico: Força a janela do Tkinter a ficar sobre todas as outras
    root.attributes('-topmost', True) 
    
    print("Janela aberta. Aguardando seleção da pasta...")
    
    # Abre o seletor de pastas amarrado à janela forçada para a frente
    pasta_destino = filedialog.askdirectory(title="Selecione a pasta do cliente", parent=root)
    
    if pasta_destino:
        caminho_txt = os.path.join(pasta_destino, "lista_concorrentes.txt")
        
        # Cria o arquivo em branco
        with open(caminho_txt, 'w', encoding='utf-8') as f:
            pass 
            
        print(f"Sucesso! 'lista_concorrentes.txt' criado em: {pasta_destino}")
    else:
        print("Operação cancelada.")
        
    # Limpa a memória para o próximo uso
    root.destroy()

# ==========================================
# MOTOR DO ATALHO (Fica escutando em segundo plano)
# ==========================================
print("Monitorando... Pressione Ctrl + Alt + L para escolher a pasta do cliente.")
print("Pressione 'Esc' a qualquer momento para desligar este script.")

keyboard.add_hotkey('ctrl+alt+l', inicializar_pasta_cliente)
keyboard.wait('esc')