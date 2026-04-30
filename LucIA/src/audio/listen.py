import speech_recognition as sr
from faster_whisper import WhisperModel
import os

# -----------------------------------------------------------------------------
# Global Model Setup
# -----------------------------------------------------------------------------
# Setting up Whisper Model (RTX 4060 targeted)
# Using 'small' model inside float16 for the best speed/accuracy ratio
print("Loading Whisper model on CUDA (RTX 4060)...")
whisper_model = WhisperModel("small", device="cpu", compute_type="int8")

def listen_mic():
    """
    Captures audio from the microphone and transcribes it to text using Faster-Whisper.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone(device_index=18, sample_rate=48000) as source:
        
        # ---------------------------------------------------------------------
        # Environment Calibration
        # ---------------------------------------------------------------------
        print("\n[System] Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("🎤 [LucIA] Listening... (Speak now)")
        try:
            # -----------------------------------------------------------------
            # Audio Capture
            # -----------------------------------------------------------------
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            print("[System] Transcribing...")
            
            temp_filename = "temp_audio.wav"
            with open(temp_filename, "wb") as f:
                f.write(audio_data.get_wav_data())
            
            # -----------------------------------------------------------------
            # Transcription Process
            # -----------------------------------------------------------------
            segments, info = whisper_model.transcribe(temp_filename, language="es")
            
            transcribed_text = ""
            for segment in segments:
                transcribed_text += segment.text
            
            # -----------------------------------------------------------------
            # Cleanup
            # -----------------------------------------------------------------
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
                
            return transcribed_text.strip()
            
        except sr.WaitTimeoutError:
            # Handle scenario where user says nothing
            print("[System] No speech detected.")
            return ""
        except Exception as e:
            # Handle hardware mismatches or device issues
            print(f"[Error] Microphone or Transcription error: {e}")
            return ""

if __name__ == "__main__":
    # Test script execution
    result = listen_mic()
    if result:
        print(f"\nUser said: {result}")