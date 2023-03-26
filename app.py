import openai

openai.api_key = "CHAT_GPT_KEY"

messages = [{"role": "system","content": "Eres un asistente muy útil"}]

while True: 
    content = input("¿De qué quieres hablar?")

    if content == "salir":
        break

    messages.append({"role": "user", "content": content })

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                             messages=[{"role": "user", "content": content}])
    
    response_content = response.choices[0].message.content
    
    messages.append({"role": "assistant", "content": response_content })
    
    print(response_content)
