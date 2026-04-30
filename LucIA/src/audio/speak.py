import os
import torch
from TTS.api import TTS
import sounddevice as sd
import numpy as np

try:
    from audio.formatter import clean_text_for_tts
except ImportError:
    from formatter import clean_text_for_tts

# -----------------------------------------------------------------------------
# Global Model Setup
# -----------------------------------------------------------------------------
# Initialize XTTSv2 model. It supports zero-shot high-quality voice cloning.
print("Loading XTTSv2 model...")
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def speak_text(text, language="es"):
    """
    Synthesize speech from text and play it.
    
    Args:
        text (str): The text to speak.
        language (str): Language code (e.g. 'es' for Spanish).
    """
    if not text:
        return

    # -------------------------------------------------------------------------
    # Resource checking
    # -------------------------------------------------------------------------
    # Expected path for the reference audio used for voice cloning
    speaker_wav = os.path.join(os.path.dirname(__file__), "voice_sample.wav")
    
    if not os.path.exists(speaker_wav):
         print(f"[Error] XTTS necesita una voz de referencia. Añade un archivo en: {speaker_wav}")
         return
             
    try:
        # ---------------------------------------------------------------------
        # Text Sanitization
        # ---------------------------------------------------------------------
        clean_text = clean_text_for_tts(text)

        print(f"[LucIA] Speaking: '{clean_text}'")
        
        # ---------------------------------------------------------------------
        # Speech Synthesis in RAM
        # ---------------------------------------------------------------------
        wav_data = tts.tts(text=clean_text, speaker_wav=speaker_wav, language=language)
        
        # ---------------------------------------------------------------------
        # Audio Playback
        # ---------------------------------------------------------------------
        audio_array = np.array(wav_data, dtype=np.float32)
        sd.play(audio_array, samplerate=24000)
        sd.wait() # Wait completely until file is done playing
        
        # Explicit VRAM release
        # Prevents progressive memory fragmentation on the RTX 4060
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
    except Exception as e:
        print(f"[Error] TTS error: {e}")

if __name__ == "__main__":
    # Test script execution
    speak_text("Hola, soy Lucía. Estoy lista para ayudarte. ¿Cómo puedo asistirte hoy? Hola Maricarmen", language="es")
