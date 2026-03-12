#Requires AutoHotkey v2.0
#SingleInstance Force
global pasta_cliente := ""

; ==========================================
; FASE 1: Preparação e Prompt (Atalho: F19)
; ==========================================
F19:: {
    global pasta_cliente
    
    ; 1. Abre a janela nativa para selecionar a PASTA do cliente
    pasta_cliente := DirSelect("", 0, "Selecione a pasta do cliente para salvar a lista")
    
    if (pasta_cliente = "") {
        return ; Aborta silenciosamente
    }

    ; 2. Pede o ramo de atuação
    tela_ramo := InputBox("Qual o ramo do cliente? (Ex: Lavanderia automatizada)", "Gerador de Prompt", "w450 h130")
    
    if (tela_ramo.Result = "Cancel" or tela_ramo.Value = "") {
        return 
    }
    
    ramo_cliente := tela_ramo.Value

    ; 3. Monta o prompt cirúrgico com a variável injetada
    prompt := "Meu cliente é uma " ramo_cliente ". Faça uma lista de concorrentes operacionais em São Paulo, SP (mais de 10 concorrentes).`nRegra de ouro: Para que a automação encontre o local exato no Google Maps sem ambiguidade, você deve incluir obrigatoriamente o BAIRRO de cada unidade.`n`nO resultado deve ser apenas o texto, com um concorrente em cada linha, no seguinte formato:`n[Nome da Empresa] [Bairro] São Paulo SP`n`nExemplo:`nOMO Lavanderia Self-Service Vila Mariana São Paulo SP`nLavanderia 60 Minutos Pinheiros São Paulo SP"

    ; 4. Joga o prompt pronto para a memória (Área de Transferência)
    A_Clipboard := prompt
    
    ; 5. Abre o Gemini no navegador, na conversa Semmler Automações
    Run("https://gemini.google.com/app/2267c167a9509945")
    
    ; 6. Aviso de instrução
    MsgBox("Prompt copiado para a memória!`n`n1. Cole (Ctrl+V) no Gemini e dê Enter.`n2. Quando a IA terminar de escrever, clique no botão 'Copiar' da resposta.`n3. Pressione F12 para salvar o arquivo na pasta do cliente.", "Passo 1 Concluído", "Iconi")
}

; ==========================================
; FASE 2: Captura e Salvamento (Atalho: Ctrl + F19)
; ==========================================
^F19:: {
    global pasta_cliente
    
    ; Trava de segurança: Verifica se o F10 foi usado antes
    if (pasta_cliente = "") {
        MsgBox("Nenhuma pasta selecionada. Use o F10 primeiro para iniciar o processo.", "Aviso de Segurança", "IconX")
        return
    }

    ; 1. Pega o texto que você copiou do Gemini
    texto_limpo := A_Clipboard
    
    ; 2. Limpeza cirúrgica: Remove blocos de código markdown se a IA os gerar
    ; Como a crase é caractere de escape no AHK, precisamos dobrá-las (6 crases geram 3 reais)
    texto_limpo := StrReplace(texto_limpo, "``````text", "")
    texto_limpo := StrReplace(texto_limpo, "``````", "")
    texto_limpo := Trim(texto_limpo) ; Tira espaços em branco sobrando nas pontas

    ; 3. Monta o caminho exato do arquivo
    caminho_txt := pasta_cliente "\lista_concorrentes.txt"
    
    ; Prevenção: Se já existir uma lista velha, deleta
    if FileExist(caminho_txt) {
        FileDelete(caminho_txt)
    }
        
    ; 4. Cria o arquivo injetando o texto limpo (em UTF-8 para não quebrar acentos)
    FileAppend(texto_limpo, caminho_txt, "UTF-8")
    
    ; 5. Finalização
    SoundBeep(750, 500)
    MsgBox("Sucesso! 'lista_concorrentes.txt' salvo blindado na pasta do cliente.", "Passo 2 Concluído", "Iconi")
    
    ; Limpa a memória da pasta para o próximo uso
    pasta_cliente := ""
}