#!/usr/bin/env python

# ### Import all needed packages
import boto3
import json

session = boto3.Session(profile_name = "AdministratorAccess-376129873205")

# ### Setup the Bedrock runtime
bedrock_runtime = session.client('bedrock-runtime', region_name='us-east-1')

print("\n*** Bienvenido a Marcos GPT ***")
prompt = input("\n¿En qué puedo ayudarte?\n\n")

# ### Generation Configuration

kwargs = {
    "modelId": "amazon.titan-text-lite-v1",
    "contentType": "application/json",
    "accept": "*/*",
    "body": json.dumps(
        {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 100,
                "temperature": 0,
                "topP": 0.9
            }
        }
    )
}

# Invoco al modelo de la misma forma que se hizo con los ejemplos de antes sólo que ahora el prompt es el contenido
# de un archivo de texto.
# Al usar un "temperature" de 0, logro mayor consistencia en las respuestas sin que el LLM sea demasiado creativo.
response = bedrock_runtime.invoke_model(**kwargs)

response_body = json.loads(response.get('body').read())
generation = response_body['results'][0]['outputText']

print(f"{generation}\n")



