import os 
from groq import Groq

#defina a chave API diretamente no código ou garanta que ele esteja configurada corretamente no ambiete
os.envion["GROQ_API_KEY"] = "digite aqui a sua chave de API"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

#inicializa a lista de mensagens para manter o contexto da conversa
messages = []

while True:
    usuario = input("Digite uma mensagem ou 'sair' para encerar: ")

    if usuario.lower()== 'sair':
        print("Conversa encerrada")
        break

    #Adiciona a mensagem do usuario à lista de mensagens
    massages.append({"role": "user" "content": usuario})

    chat_completion = client.chat.chat_completions.create(
        messages=messages,
        model="llama-.3.1-70b-versatile"
    )

    resposta = chat_completion.choices[0].message.content
    print("resposta:", resposta)

    #Adiciona a resposta do assistente à lista de mensagens para manter o contexto
    massages.append({"role": "assistant", "content": resposta})