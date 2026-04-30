# LucIA - AI Personal Assistant

LucIA is a local, private, and fast AI assistant running on Pop!_OS using NVIDIA CUDA acceleration.

## 🚀 Installation & Setup

### 1. System Requirements
- **OS:** Pop!_OS / Debian-based Linux.
- **GPU:** NVIDIA (Recommended for CUDA acceleration, e.g., RTX 4060).
- **Software:** - [Ollama](https://ollama.com/) (Local LLM Server).
  - Python 3.12+.

### 2. System Dependencies
Install the required system libraries for audio and Python development:

`sudo apt update`
`sudo apt install ffmpeg portaudio19-dev python3.12-dev python3.12-venv`

### 3. LLM Setup (Ollama)
Download and run the brain (por defecto usamos `llama3.1` o `llama3.2` para menos consumo de VRAM):

```bash
ollama pull llama3.1
```

### 4. Project Setup
Create a virtual environment and install Python dependencies:

```bash
python3 -m venv venv // ~/.pyenv/versions/3.11.9/bin/python -m venv venv
source venv/bin/activate
pip install -r LucIA/requirements.txt
```

### 5. Configurar la voz (XTTSv2)
Para que LucIA pueda hablar, el modelo Coqui TTS necesita un archivo corto de audio de referencia para clonar la voz:
1. Graba o toma un audio limpio de unos 3-5 segundos (evita ruidos de fondo).
2. Guárdalo como `voice_sample.wav` dentro de la ruta `LucIA/src/audio/`.

### 6. Ejecutar LucIA
Una vez tengas Ollama funcionando y el audio de prueba colocado, simplemente lanza el asistente usando la gráfica:

```bash
CUDA_VISIBLE_DEVICES=0 python LucIA/src/main.py
```

## 🛠 Project Structure
- `src/audio`: Voice recognition (Faster-Whisper).
- `src/llm`: Brain logic (Ollama connection).
- `src/ui`: Graphical Interface (Upcoming).
- `assets/voice_samples`: Storage for voice cloning profiles.
- `context`: Future storage for documents (RAG).

## 📝 License
This project is licensed under the MIT License.