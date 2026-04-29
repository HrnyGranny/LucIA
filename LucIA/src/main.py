import os
import sys

# -----------------------------------------------------------------------------
# Module Setup
# -----------------------------------------------------------------------------
# Ensure the src directory is in the python path for relative imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from audio.listen import listen_mic
from llm.generate import generate_response
from audio.speak import speak_text

def run_assistant():
    """
    Main loop coordinating the assistant: Listen -> Think -> Speak
    """
    print("====================================")
    print("✨ Iniciando LucIA Assistant ✨")
    print("====================================")
    
    # Initialize conversation context
    chat_history = None
    
    while True:
        try:
            # -----------------------------------------------------------------
            # 1. Listen (Audio to Text)
            # -----------------------------------------------------------------
            user_input = listen_mic()
            
            if not user_input:
                continue
                
            print(f"👤 Tú: {user_input}")
            
            # -----------------------------------------------------------------
            # Core commands / End of execution
            # -----------------------------------------------------------------
            if user_input.lower() in ["salir", "apagar", "adiós", "detente"]:
                print("👋 [LucIA]: Hasta luego. Apagando el asistente.")
                speak_text("Hasta luego.")
                break
                
            # -----------------------------------------------------------------
            # 2. Think (Text to Text via Local LLM)
            # -----------------------------------------------------------------
            # Pass the previous history to maintain context
            ai_response, chat_history = generate_response(user_input, history=chat_history, model_name="llama3.1")
            print(f"🤖 LucIA: {ai_response}")
            
            # -----------------------------------------------------------------
            # 3. Speak (Text to Audio)
            # -----------------------------------------------------------------
            speak_text(ai_response)
            
        except KeyboardInterrupt:
            # Handle user pressing Ctrl+C gracefully
            print("\n[System] Asistente detenido por el usuario.")
            break
        except Exception as e:
            # Catch unexpected crashes without breaking the entire console
            print(f"\n[Error] Algo salió mal en el bucle principal: {e}")
            break

if __name__ == "__main__":
    run_assistant()