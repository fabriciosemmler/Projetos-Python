import tkinter as tk
import threading
import asyncio
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager

def exibir_aviso_grande(texto):
    def criar_gui():
        root = tk.Tk()
        root.overrideredirect(True) # -Caption
        root.attributes("-topmost", True) # +AlwaysOnTop
        root.attributes("-toolwindow", True) # +ToolWindow
        root.configure(bg='#1f1f1f')
        
        largura, altura = 600, 80
        screen_w = root.winfo_screenwidth()
        root.geometry(f"{largura}x{altura}+{(screen_w - largura) // 2}+50")
        
        label = tk.Label(root, text=texto, font=("Segoe UI", 24, "bold"), 
                         fg="#00FFFF", bg="#1f1f1f", wraplength=550)
        label.pack(expand=True)
        
        root.after(3000, root.destroy)
        root.mainloop()
    
    threading.Thread(target=criar_gui, daemon=True).start()

DEEZER_ID = "com.deezer.deezer-desktop"

async def obter_sessao():
    manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()
    sessoes = manager.get_sessions()
    return next((s for s in sessoes if s.source_app_user_model_id == DEEZER_ID), None)

async def executar_contagem():
    sessao = await obter_sessao()
    if not sessao:
        print("❌ Deezer não detectado.")
        return

    # --- FASE 1: MONITORAMENTO DAS TROCAS ---
    info = await sessao.try_get_media_properties_async()
    musica_atual = f"{info.artist} - {info.title}"
    exibir_aviso_grande(f"▶️ [1/3] {musica_atual}")

    contador = 0
    while contador < 2:
        await asyncio.sleep(2)
        try:
            info = await sessao.try_get_media_properties_async()
            nova = f"{info.artist} - {info.title}"
            if nova != musica_atual:
                contador += 1
                musica_atual = nova
                exibir_aviso_grande(f"🔄 [{contador + 1}/3] {musica_atual}")
        except:
            continue

    # --- FASE 2: VIGÍLIA ATIVA (A 3ª MÚSICA) ---
    print("⏳ Iniciando Vigília Ativa na 3ª música...")
    
    while True:
        await asyncio.sleep(2) # Espia o relógio a cada 2 segundos
        try:
            timeline = sessao.get_timeline_properties()
            
            total = timeline.end_time.total_seconds()
            atual = timeline.position.total_seconds()
            restante = total - atual

            # Se a música estiver quase acabando (menos de 4 segundos)
            if restante <= 4:
                # Se ainda houver um fôlego, faz o ajuste fino final
                if restante > 0.5:
                    await asyncio.sleep(restante - 0.3)
                
                # O Bote: Pausa exatamente no fim
                await sessao.try_toggle_play_pause_async()
                exibir_aviso_grande("⏸️ 3 Músicas! Pausado.")
                break
                
            print(f"DEBUG: Falta {restante:.1f}s") # Ative se quiser ver o log
        except:
            continue

if __name__ == "__main__":
    asyncio.run(executar_contagem())