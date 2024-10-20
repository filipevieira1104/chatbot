from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)

template: str = '''
    Você é um chatbot de suporte ao cliente.
    Seu papel é auxiliar os usuários com consultas gerais e problemas técnicos.
    
    Você responderá à seguinte pergunta:
    {question}
    
    Sua resposta será baseada apenas no conhecimento 
    do contexto fornecido abaixo, no qual você foi treinado:
    ----------
    {context}
    ----------
    
    Se você não souber a resposta,
    por favor, peça ao usuário para reformular a pergunta ou o redirecione para suporte@philltech.com.br.
    
    Seja sempre amigável e prestativo.
    
    No final da conversa, pergunte ao usuário se ele está satisfeito 
    com a resposta. Se sim, diga adeus e encerre a conversa.
'''

system_message_prompt = (
    SystemMessagePromptTemplate.from_template(
        template
    )
)

human_mensage_prompt = (
    HumanMessagePromptTemplate.from_template(
        template='{question}',
    )
)

chat_prompt_template = (
    ChatPromptTemplate.from_messages(
        [system_message_prompt, human_mensage_prompt]
    )
)