import os
import chainlit as cl
from openai import OpenAI
from dotenv import load_dotenv

SYSTEM_PROMPT = """
Você é um assistente familiar.

Regras:

1. Use linguagem simples, amigável e cotidiana.
2. Considere que algumas palavras possuem significados especiais dentro da família.
3. Quando receber perguntas sobre apelidos, pessoas da família ou brincadeiras internas, utilize o contexto familiar.
4. Responda de forma natural e descontraída.
5. Caso não saiba algo, diga que não possui essa informação.
6. Nunca invente fatos sobre a família.
7. Priorize as respostas da base local quando elas existirem.
8. Se a pergunta não estiver na base local, responda usando seu conhecimento geral.
9. Considere que existe um vocabulário próprio da família com apelidos e referências internas.
10. Mantenha respostas curtas e objetivas.
"""


load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

respostas = {
    "mundo": "A Vanessa Henare, mãe da Luana.",
    "brassinho": "Esse é o Marcio Henare.",
    "filhuxo": "Esse é o Marcio Henare.",
    "fofa": "Vovuxa, ou Maria Rita também conhecida por Lolo.",
    "mijona": "Vovuxa, ou Maria Rita também conhecida por Lolo.",
    "boca de sacola": "Vovuxa, ou Maria Rita também conhecida por Lolo.",
    "lantra": "Essa é fácil, só pode ser o BIG.",
    "file": "Essa é fácil, só pode ser o BIG.",
    "melhor": "Essa é fácil, só pode ser a Mamuxa Tadinha.",
    "coitadinha": "Essa é a Lucy.",
    "cachorro": "O Tito, aquele Lantra.",
    "comprar": "Essa é a Vovuxa.",
    "cartão": "Big, aquele Lantra.",
    "mercado": "Essa é a Vovuxa.",
    "linda": "Essa é a Mamuxa que acabou de tomar banho.",
    "gata": "Mamuxa, com certeza.",
    "rainha": "Só pode ser a Mamuxa.",
    "elegante": "Mamuxa, sempre impecável.",
    "cheirosa": "Mamuxa, acabadinha de se arrumar.",
    "brava": "Mamuxa quando alguém mexe nas coisas dela.",
    "carinhosa": "Mamuxa, com certeza.",
    "chorona": "Mamuxa vendo novela.",
    "cozinheira": "Mamuxa, ninguém cozinha igual.",
    "organizada": "Mamuxa, tudo no lugar certo.",
    "durona": "Mamuxa quando não quer moleza.",
    "sortuda": "Mamuxa, sempre ganha no bingo.",
    "risonha": "Mamuxa quando conta as histórias antigas.",
    "chefe": "Mamuxa manda em todo mundo.",
    "gordinho": "O Tito, aquele Lantra.",
    "esperto": "O BIG, sempre aprontando.",
    "medroso": "A Lucy, coitadinha.",
    "TV": "Vovuxa, vidrada na novela.",
    "remedio": "Vovuxa, hora do comprimido.",
    "festa": "Mamuxa organiza tudo.",
    "presente": "Mamuxa adora dar presente.",
}


@cl.on_message
async def main(message: cl.Message):
    texto = message.content.lower()

    # Respostas prontas
    for palavra, resposta in respostas.items():
        if palavra in texto:
            await cl.Message(content=resposta).send()
            return

    # OpenRouter
    resposta = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[
            {
                "role": "user",
                "content": message.content
            }
        ]
    )

    await cl.Message(
        content=resposta.choices[0].message.content
    ).send()