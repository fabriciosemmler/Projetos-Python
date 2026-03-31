#Requires AutoHotkey v2.0
#SingleInstance Force

; Monitor para os gatilhos analógicos (Modo Xbox/Steam)
SetTimer MonitorarGatilhosXbox, 100

; ---------------------------------------------------------
; MÓDULO CONTROLE (DualShock 4)
; L1 = Joy5 | R1 = Joy6
; L2 = Joy7 | R2 = Joy8
; ---------------------------------------------------------

; L1 + R1 para abaixar o volume
Joy5::
Joy6:: 
{
    ; Checa se os dois botões estão pressionados juntos
    while GetKeyState("Joy5") and GetKeyState("Joy6") {
        Send("{Volume_Down}")
        Sleep(100) ; Intervalo de 100ms para a barra de volume descer suavemente
    }
}

; L2 + R2 para aumentar o volume
Joy7::
Joy8:: 
{
    while GetKeyState("Joy7") and GetKeyState("Joy8") {
        Send("{Volume_Up}")
        Sleep(100) 
    }
}

; ---------------------------------------------------------
; MÓDULO XINPUT (Gatilhos Xbox via Steam)
; LT = Eixo Z | RT = Eixo R
; ---------------------------------------------------------
MonitorarGatilhosXbox() {
    ; Lê a posição dos eixos analógicos
    EixoZ := GetKeyState("JoyZ")
    EixoR := GetKeyState("JoyR")
    
    ; TRAVA DE SEGURANÇA: Blinda o código para só calcular se o controle estiver ativo e enviando números
    if IsNumber(EixoZ) and IsNumber(EixoR) {
        ; O repouso costuma ser 0 ou 50. Se ambos passarem de 70, entende-se como gatilho apertado.
        if (EixoZ > 70) and (EixoR > 70) {
            Send("{Volume_Up}")
        }
    }
}