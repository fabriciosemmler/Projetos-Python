import asyncio
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager

async def raio_x_midia():
    manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()
    sessoes = manager.get_sessions()
    
    print("\n🔍 RAIO-X DO ÁUDIO DO WINDOWS:")
    print("-" * 50)
    
    if not sessoes:
        print("O Windows afirma categoricamente que não há NADA no painel de mídia.")
    
    for sessao in sessoes:
        app = sessao.source_app_user_model_id
        try:
            info = await sessao.try_get_media_properties_async()
            titulo = info.title if info.title else "Sem título"
            artista = info.artist if info.artist else "Sem artista"
            print(f"📻 Aplicativo: {app}")
            print(f"   Tocando   : {artista} - {titulo}\n")
        except:
            print(f"📻 Aplicativo: {app} (Não foi possível ler os detalhes)\n")
            
    print("-" * 50)

if __name__ == "__main__":
    asyncio.run(raio_x_midia())