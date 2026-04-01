#Requires AutoHotkey v2.0
#SingleInstance Force

; ---------------------------------------------------------
; MÓDULO RAIO-X (Diagnóstico do Controle)
; ---------------------------------------------------------
SetTimer RaioXControle, 50

RaioXControle() {
    texto := ""
    
    ; Varre os 16 botões físicos possíveis
    Loop 16 { 
        if GetKeyState("Joy" A_Index) {
            texto .= "Apertando Botão: Joy" A_Index "`n"
        }
    }
    
    ; Varre os eixos analógicos (Caso a Steam esteja emulando gatilhos Xbox)
    if IsNumber(GetKeyState("JoyZ")) and (GetKeyState("JoyZ") > 70) {
        texto .= "Apertando Gatilho Esquerdo (Eixo Z)`n"
    }
    if IsNumber(GetKeyState("JoyR")) and (GetKeyState("JoyR") > 70) {
        texto .= "Apertando Gatilho Direito (Eixo R)`n"
    }
        
    ToolTip texto
}