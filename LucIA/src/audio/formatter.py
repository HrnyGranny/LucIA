import re

def clean_text_for_tts(text: str) -> str:
    """
    Cleans and formats text to improve TTS (XTTSv2) performance, 
    prevent language hallucinations, and optimize pacing.
    """
    if not text:
        return ""
        
    # 1. Quitamos caracteres raros, markdown y emojis comunes que confunden el idioma
    clean = re.sub(r'[*"_*~#|()]', '', text)
    
    # 2. Conservamos la entonación pero evitamos repeticiones exageradas (!!! o ??? o ...)
    # que son las que realmente causan que el modelo XTTS alucine o cambie de idioma.
    clean = re.sub(r'!+', '!', clean)
    clean = re.sub(r'\?+', '?', clean)
    clean = re.sub(r'\.+', '.', clean)
    clean = re.sub(r'¡+', '¡', clean)
    clean = re.sub(r'¿+', '¿', clean)
    
    # 3. Limpiar saltos de línea y espacios dobles
    clean = re.sub(r'\s+', ' ', clean).strip()
    
    # 4. Asegurarnos de que termine en punto o exclamación/interrogación 
    # para que la voz baje el tono correctamente al final y corte la generación.
    if clean and not clean[-1] in ['.', '!', '?']:
        if clean[-1] == ',':
            clean = clean[:-1] + '.'
        else:
            clean += '.'
        
    return clean
