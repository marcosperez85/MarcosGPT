#!/usr/bin/env python

# ### Import all needed packages
import boto3
import json

session = boto3.Session(profile_name = "AdministratorAccess-376129873205")

# ### Setup the Bedrock runtime
bedrock_runtime = session.client('bedrock-runtime', region_name='us-east-1')

print("\n*** Bienvenido a Marcos GPT ***")

def menuPrincipal():
    while True:

        print("\nMenú principal")
        print("1) Realizar una pregunta")
        print("2) Salir del programa")

        opcionElegida = input("\nSeleccione una opción: ")

        if opcionElegida == "1" :
                
            prompt = input("\n¿En qué puedo ayudarte?\n\n>> ")

            # ### Generation Configuration
            kwargs = {
                "modelId": "amazon.titan-text-lite-v1",
                "contentType": "application/json",
                "accept": "*/*",
                "body": json.dumps(
                    {
                        "inputText": prompt,
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

            print(f"\n{generation}\n")

        elif opcionElegida == "2":
            print("\nMuchas gracias por usar este servicio\n")
            break
        else:
            print("\nOpción no valida. Intente de nuevo.")

# Llamamos a la función para iniciar el programa
menuPrincipal()






