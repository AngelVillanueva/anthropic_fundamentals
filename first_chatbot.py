import os
import logging
from dotenv import load_dotenv
import anthropic


# Configure logging
logging.basicConfig(level=logging.INFO)
# Load environment variables from .env file
load_dotenv()
anthropic.api_key = os.getenv("ANTHROPIC_API_KEY")
# Initialize the Anthropic client
if client := anthropic.Client():
    logging.info("👍 Todo ok con la API de Anthropic")
else:
    logging.error("❌ No se pudo obtener la colección")

# MAIN FUNCTION
def main():
    conversation = []
    pregunta = input("?").strip()
    while pregunta.lower() != "exit":
        conversation.append({"role": "user", "content": pregunta})
        respuesta = preguntar_ai(conversation, pregunta)
        conversation.append({"role": "assistant", "content": respuesta})
        pregunta = input("?").strip()

# AUX FUNCTION TO CALL THE ANTHROPIC API
def preguntar_ai(conversation, pregunta, modelo="claude-3-haiku-20240307"):
    logging.info(f"🤖 La conversación viene siendo... {conversation}")
    logging.info(f"🤖 Preguntando a la IA: {pregunta}")
    # Example usage of the client
    try:
        response = client.messages.create(
            model=modelo,
            max_tokens=200,
            messages=conversation
        )
        respuesta = response.content[0].text
        print(respuesta)
        return respuesta
    except Exception as e:
        logging.error(f"❌ Error al llamar a la API de Anthropic: {e}")

if __name__ == "__main__":
    main()
