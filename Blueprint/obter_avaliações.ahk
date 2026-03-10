#Requires AutoHotkey v2.0
#SingleInstance Force

F11:: {
    ; Trava as coordenadas do mouse e do buscador de pixels para a área útil do navegador (Client)
    CoordMode("Mouse", "Client")
    CoordMode("Pixel", "Client") 

    ; 1. Abre o Google Maps
    Run("https://www.google.com.br/maps")
    Sleep(5000)
    
    ; 2. Lê o arquivo e fatia as linhas
    texto_completo := FileRead("lista_concorrentes.txt", "UTF-8")
    linhas := StrSplit(texto_completo, "`n", "`r")
    
    ; 3. O Motor de Repetição (Loop)
    For indice, escola in linhas {
        ; Ignora linhas vazias
        if (escola = "")
            continue

        ; Retoma o foco clicando fisicamente dentro da barra de pesquisa
        MouseClick("Left", 620, 210)
        Sleep(300)

        ; Seleciona o que estiver na barra e deleta
        Send("^a")
        Sleep(200)
        Send("{Delete}")
        Sleep(200)
        
        ; Cola o texto da linha atual e aperta Enter
        SendText(escola)
        Sleep(500)
        Send("{Enter}")
        
        ; Aguarda 5 segundos carregando o local
        Sleep(5000)

        ; ==========================================
        ; O Rastreador de Cor (Ctrl+F)
        ; ==========================================
        Send("^f")
        Sleep(500)
        SendText("Avaliações")
        Sleep(1000) 
        
        if PixelSearch(&achouX, &achouY, 0, 0, A_ScreenWidth, A_ScreenHeight, 0xFF9632) {
            Send("{Esc}")
            Sleep(300)
            
            ; Clica exatamente na aba Avaliações
            MouseClick("Left", achouX, achouY)
            Sleep(3000) ; Espera 3 segundos para a lista de avaliações carregar na tela

            ; ==========================================
            ; NOVIDADE 3: Motor de Rolagem (WheelDown)
            ; ==========================================
            ; Loop executa 15 vezes. Aumente esse número se quiser minerar ainda mais fundo.
            Loop 20 {
                Send("{WheelDown 8}") ; Dá 6 "giros" físicos na rodinha do mouse
                Sleep(800) ; Pausa de quase 1 segundo para o Google baixar os próximos blocos
            }

        } else {
            Send("{Esc}")
            Sleep(300)
        }
        
        ; Aguarda 5 segundos antes de ir para a próxima escola do txt
        Sleep(5000)
    }
    
    ; 4. Finalização: Fecha a aba atual do navegador (Ctrl + W)
    ; Send("^w")
}