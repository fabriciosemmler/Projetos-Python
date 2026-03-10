#Requires AutoHotkey v2.0
#SingleInstance Force

; Usa o mesmo modo Client que já adotamos para manter a consistência
CoordMode("Mouse", "Client")
CoordMode("Pixel", "Client")

^F12:: {
    ; 1. Captura a coordenada exata de onde a ponta do seu mouse está agora
    MouseGetPos(&eixoX, &eixoY)
    
    ; 2. Lê a cor do pixel exato sob o mouse (no formato Hexadecimal)
    cor_capturada := PixelGetColor(eixoX, eixoY)
    
    ; 3. Copia a cor automaticamente para você não precisar digitar
    A_Clipboard := cor_capturada
    
    ; 4. Exibe o resultado na tela
    MsgBox("Alvo travado!`n`nCor: " cor_capturada "`nCoordenadas: X=" eixoX " Y=" eixoY "`n`nJá copiado para a área de transferência.")
}