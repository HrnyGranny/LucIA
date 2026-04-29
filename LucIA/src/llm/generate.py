import ollama

def generate_response(prompt: str, history: list = None, model_name: str = "llama3.1") -> tuple[str, list]:
    """
    Sends a prompt to a local Ollama model and gets the response maintaining conversation history.
    
    Args:
        prompt (str): The transcribed text from the user.
        history (list): Previous conversation messages to maintain state. Defaults to None.
        model_name (str): The name of the local Ollama model to use.
                          
    Returns:
        tuple: (The AI's text response, the updated history list)
    """
    # -------------------------------------------------------------------------
    # Context Initialization
    # -------------------------------------------------------------------------
    # Initialize conversation state if empty
    if history is None:
        history = [
            {
                'role': 'system',
                'content': 'Eres LucIA, una asistente personal amigable, útil y concisa. Respondes en español. Manten tus respuestas conversacionales y no muy largas para que sea natural y fácil de escuchar.'
            }
        ]
        
    # Append user input
    history.append({'role': 'user', 'content': prompt})
    
    try:
        # ---------------------------------------------------------------------
        # LLM Query Execution
        # ---------------------------------------------------------------------
        print(f"[System] Sending to local AI ({model_name})...")
        response = ollama.chat(model=model_name, messages=history)
        
        reply = response['message']['content']
        
        # Append AI response
        history.append({'role': 'assistant', 'content': reply})
        
        # ---------------------------------------------------------------------
        # Memory Management
        # ---------------------------------------------------------------------
        # Limit context window to prevent VRAM overflow (system prompt + last 10 messages)
        if len(history) > 11:
            history = [history[0]] + history[-10:]
            
        return reply, history

    except Exception as e:
        # ---------------------------------------------------------------------
        # Error Handling & Rollback
        # ---------------------------------------------------------------------
        # Handle connection failures and rollback history
        print(f"[Error] LLM error: Asegúrate de tener Ollama instalado y el modelo descargado. Error: {e}")
        history.pop()
        return "Lo siento, ha habido un problema conectando con mi cerebro.", history

if __name__ == "__main__":
    # Test script execution
    print(generate_response("Hola, ¿quién eres?"))
