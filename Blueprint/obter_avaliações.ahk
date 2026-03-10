#Requires AutoHotkey v2.0
#SingleInstance Force

F11:: {
    ; Trava as coordenadas do mouse e do buscador de pixels para a área útil do navegador (Client)
    CoordMode("Mouse", "Client")
    CoordMode("Pixel", "Client") ; <--- NOVIDADE 1

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
        ; NOVIDADE 2: O Rastreador de Cor (Ctrl+F)
        ; ==========================================
        Send("^f")
        Sleep(500)
        
        ; Digita a palavra para forçar o navegador a pintar de laranja
        SendText("Avaliações")
        Sleep(1000) ; Espera o navegador rolar (se precisar) e pintar a tela
        
        ; Procura o pixel laranja (0xFF9632) a partir do ponto 0,0 até o final da tela
        if PixelSearch(&achouX, &achouY, 0, 0, A_ScreenWidth, A_ScreenHeight, 0xFF9632) {
            ; Guardou a coordenada. Aperta Esc para sair do modo de busca
            Send("{Esc}")
            Sleep(300)
            
            ; Clica exatamente onde achou a cor
            MouseClick("Left", achouX, achouY)
        } else {
            ; Se a cor não for encontrada, aperta Esc para limpar a barra de busca e não travar o loop
            Send("{Esc}")
            Sleep(300)
        }
        
        ; Aguarda 5 segundos entre as escolas, como solicitado
        Sleep(5000)
    }
    
    ; 4. Finalização: Fecha a aba atual do navegador (Ctrl + W)
    Send("^w")
}