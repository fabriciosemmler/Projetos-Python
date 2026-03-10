#Requires AutoHotkey v2.0
#SingleInstance Force

F11:: {
    ; 1. Abre o Google Maps no seu navegador padrão
    Run("https://www.google.com.br/maps")
    Sleep(5000)
    
    ; 2. Seleciona tudo e deleta (Limpa a barra)
    Send("^a")
    Sleep(200)
    Send("{Delete}")
    Sleep(200)
    
    ; 3. Lê o arquivo e fatia as linhas (Método AHK v2)
    ; O "UTF-8" garante que nomes com acento não quebrem
    texto_completo := FileRead("lista_concorrentes.txt", "UTF-8")
    linhas := StrSplit(texto_completo, "`n", "`r")
    primeira_escola := linhas[1]
    
    ; 4. Cola o texto e aperta Enter
    SendText(primeira_escola)
    Sleep(500)
    Send("{Enter}")
}