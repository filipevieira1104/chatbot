
# PhillTech AI Assistente

## Descrição

O **PhillTech AI Assistente** é um chatbot inteligente desenvolvido para fornecer suporte ao cliente, respondendo perguntas sobre produtos, políticas de devolução, promoções, e outros tópicos relevantes da **PhillTech Eletronics**. Usando tecnologias avançadas de **Processamento de Linguagem Natural (NLP)** e **busca semântica**, o assistente busca as respostas mais relevantes a partir de documentos previamente carregados e estruturados. 

Este projeto foi construído com **Python**, utilizando **FastAPI** para a criação de APIs e integração com o modelo de linguagem **Cohere** para gerar respostas baseadas no contexto das perguntas dos usuários.

## Funcionalidades

- **Busca Semântica**: O assistente utiliza busca semântica nos documentos carregados para fornecer respostas baseadas no conteúdo.
- **Upload de Documentos**: Suporta o upload de novos documentos que podem ser processados e utilizados para gerar respostas futuras.
- **Processamento de Linguagem Natural**: O sistema usa a API da **Cohere** para criar embeddings e processar as perguntas dos usuários de forma inteligente.
- **Respostas Baseadas em Contexto**: O chatbot compreende o contexto da pergunta e oferece respostas detalhadas, amigáveis e precisas.
  
## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do projeto.
- **FastAPI**: Framework para criação de APIs rápidas e assíncronas.
- **Uvicorn**: Servidor ASGI utilizado para rodar o FastAPI.
- **LangChain**: Biblioteca que facilita a integração com modelos de linguagem e manipulação de documentos.
- **Cohere**: API de Processamento de Linguagem Natural utilizada para gerar embeddings e processar as consultas dos usuários.
- **Chroma (Vectorstore)**: Ferramenta para armazenar e buscar vetores dos documentos.

## Estrutura do Projeto

- **`documents.py`**: Carrega e processa documentos, dividindo-os em partes menores (chunks) e armazenando no vetorstore **Chroma**.
- **`main.py`**: Configura a API com FastAPI, definindo os endpoints para processar as perguntas dos usuários e adicionar novos documentos.
- **`model.py`**: Integra o modelo de linguagem **Cohere** ao pipeline de resposta.
- **`prompting.py`**: Define os templates de conversação que guiam o comportamento do assistente.
  
## Endpoints

### **POST** `/message`

- **Descrição**: Endpoint principal para enviar perguntas ao assistente.
- **Corpo da Requisição (JSON)**:
  ```json
  {
    "question": "Qual é o programa de fidelidade da PhillTech?"
  }
  ```
- **Resposta (Exemplo)**:
  ```json
  {
    "response": "A PhillTech Eletronics oferece o programa de fidelidade EcoRewards..."
  }
  ```

### **POST** `/add_document`

- **Descrição**: Endpoint para adicionar novos documentos ao assistente.
- **Corpo da Requisição**:
  - Arquivo `.txt` que será carregado e processado.
- **Resposta**:
  ```json
  {
    "filename": "nome_do_arquivo.txt"
  }
  ```

## Como Rodar o Projeto Localmente

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seuusuario/philltech-ai-assistente.git
   ```

2. **Instale as Dependências**:
   ```bash
   cd philltech-ai-assistente
   python -m venv venv
   source venv/bin/activate   # Para Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure a Chave da API Cohere**:
   - Crie um arquivo `.env` e adicione sua chave da API **Cohere**:
     ```
     COHERE_API_KEY=your_cohere_api_key
     ```

4. **Execute a Aplicação**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a API**:
   - Acesse a aplicação rodando localmente em [http://127.0.0.1:8000](http://127.0.0.1:8000).

6. **Testar com Postman ou cURL**:
   - Use o **Postman** ou **cURL** para testar os endpoints fornecidos.

## Estrutura do Projeto

```bash
├── docs/                     # Documentos de exemplo usados pelo assistente
├── main.py                   # Configura a API e gerencia os endpoints
├── documents.py              # Carrega e processa os documentos para busca semântica
├── model.py                  # Integração com o modelo de linguagem Cohere
├── prompting.py              # Templates de conversação do chatbot
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do projeto
```

## Exemplo de Uso

1. **Fazer uma Pergunta ao Assistente**:
   - Envie uma pergunta sobre as políticas ou serviços da PhillTech.
   - Exemplo:
     ```json
     {
       "question": "Quais são as políticas de devolução da PhillTech?"
     }
     ```
   - O assistente buscará nos documentos relevantes e responderá com detalhes.

2. **Adicionar Novo Documento**:
   - Carregue um novo documento `.txt` contendo informações sobre a empresa.
   - O assistente processará esse novo conteúdo e o integrará à base de dados.

## Contribuições

Contribuições são bem-vindas! Se você encontrar problemas, ou tiver sugestões para melhorias, fique à vontade para abrir um **issue** ou enviar um **pull request**.

---

Se você gostou do projeto ou tem alguma dúvida, entre em contato comigo. Obrigado por conferir o **PhillTech AI Assistente**!
