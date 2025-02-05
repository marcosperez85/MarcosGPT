#!/usr/bin/env python

# ### Import all needed packages
import boto3
import json

session = boto3.Session(profile_name = "AdministratorAccess-376129873205")
bedrock_runtime = session.client('bedrock-runtime', region_name='us-east-1')

# Para mantener el historial de la conversación
historia = []

print("\n*** Bienvenido a Marcos GPT ***")
print("\n¿En qué puedo ayudarte hoy?")

def chat():
    try:
        while True:
            prompt = input("\n>> ")

            if prompt.lower() in ["salir", "exit", "quit"]:
                print("\nMuchas gracias por usar este servicio\n")
                break
            
            # Guardamos la historia
            historia.append({"role": "user", "content": prompt})

            # ### Generation Configuration
            kwargs = {
                "modelId": "amazon.titan-text-lite-v1",
                "contentType": "application/json",
                "accept": "*/*",
                "body": json.dumps(
                    {
                        "inputText": "\n".join([f"{h['role']}: {h['content']}" for h in historia]),
                        "textGenerationConfig": {
                            "maxTokenCount": 200,
                            "temperature": 0,
                            "topP": 0.9
                        }
                    }
                )
            }

            print("\nGenerando respuesta...")

            response = bedrock_runtime.invoke_model(**kwargs)

            response_body = json.loads(response.get('body').read())
            generation = response_body['results'][0]['outputText']

            historia.append({"role": "assistant", "content": generation})  # Guardamos la respuesta

            print(f"\nMarcos GPT: {generation}\n")

    except KeyboardInterrupt:
        print("\nMuchas gracias por usar este servicio\n")

# Llamamos a la función para iniciar el programa
chat()






