def chatbot_semmler(mensagem_cliente):
    mensagem = str(mensagem_cliente).strip()
    
    menu_principal = (
        "Olá, seja bem-vindo à Semmler Automações.\n"
        "É um prazer ter você aqui. Como podemos ajudar a otimizar o seu negócio hoje?\n"
        "Digite o número da opção desejada:\n\n"
        "1 - Conhecer nossos serviços\n"
        "2 - Solicitar um orçamento\n"
        "3 - Suporte técnico\n"
        "4 - Acompanhar andamento do meu projeto\n"
        "5 - Horário de atendimento\n"
        "6 - Falar diretamente com um especialista"
    )

    if mensagem == "1":
        return "Nossos serviços incluem automação de processos, criação de chatbots e inteligência de mercado. Qual área mais interessa?"
    elif mensagem == "2":
        return "Para solicitar um orçamento, por favor, descreva brevemente a sua necessidade ou o processo que deseja automatizar."
    elif mensagem == "3":
        return "Entendido. Por favor, descreva o problema que você está enfrentando e nossa equipe técnica analisará imediatamente."
    elif mensagem == "4":
        return "Para consultar o andamento do seu projeto, digite o seu CNPJ ou número de contrato."
    elif mensagem == "5":
        return "Nosso horário de atendimento é de segunda a sexta, das 08:00 às 18:00."
    elif mensagem == "6":
        return "Um de nossos especialistas assumirá este atendimento em instantes. Por favor, aguarde."
    else:
        return menu_principal

# Simulação de uso do chatbot
mensagem_recebida = "Oi, bom dia!"
resposta = chatbot_semmler(mensagem_recebida)
print("Cliente: ", mensagem_recebida)
print("Bot: \n", resposta)
print("----------------------------------------")

mensagem_recebida = "3"
resposta = chatbot_semmler(mensagem_recebida)
print("Cliente: ", mensagem_recebida)
print("Bot: \n", resposta)