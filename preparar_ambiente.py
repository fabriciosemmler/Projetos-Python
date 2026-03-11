import os
import tkinter as tk
from tkinter import filedialog

# Inicia o Tkinter e esconde a janela base
root = tk.Tk()
root.withdraw()

# Força a janela do Tkinter a ficar sobre todas as outras
root.attributes('-topmost', True) 

# Abre o seletor de pastas amarrado à janela forçada para a frente
pasta_destino = filedialog.askdirectory(title="Selecione a pasta do cliente", parent=root)

if pasta_destino:
    caminho_txt = os.path.join(pasta_destino, "lista_concorrentes.txt")
    
    # Cria o arquivo em branco
    with open(caminho_txt, 'w', encoding='utf-8') as f:
        pass 
        
# Limpa a memória e encerra o processo
root.destroy()