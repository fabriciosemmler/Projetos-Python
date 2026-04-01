#Requires AutoHotkey v2.0
#SingleInstance Force

; ---------------------------------------------------------
; MÓDULO OSD (Exibição em tela leve e cirúrgica)
; ---------------------------------------------------------
MostrarVolume() {
    ; Captura o volume atual da placa de som e arredonda para um número inteiro limpo
    VolumeAtual := Round(SoundGetVolume())
    
    ; Exibe um balãozinho flutuante
    ToolTip("Volume: " VolumeAtual "%")
    
    ; O timer com valor negativo (-1500) apaga o balão automaticamente após 1.5 segundos
    SetTimer(EsconderToolTip, -1500)
}

EsconderToolTip() {
    ToolTip() ; Enviar o comando vazio destrói o balão da memória
}

; ---------------------------------------------------------
; MÓDULO CONTROLE (DualShock 4 - Ajuste exato de 1%)
; L2 = Joy7 | R2 = Joy8 | Botão X = Joy2
; ---------------------------------------------------------

Joy7::
Joy8::
Joy2:: 
{
    ; L2 + X para abaixar o volume em 1 ponto
    if GetKeyState("Joy7") and GetKeyState("Joy2") {
        SoundSetVolume("-1")
        MostrarVolume() ; Invoca o feedback visual instantaneamente
        KeyWait("Joy2") ; Trava cirúrgica
    }
    
    ; R2 + X para aumentar o volume em 1 ponto
    if GetKeyState("Joy8") and GetKeyState("Joy2") {
        SoundSetVolume("+1")
        MostrarVolume() ; Invoca o feedback visual instantaneamente
        KeyWait("Joy2") 
    }
}