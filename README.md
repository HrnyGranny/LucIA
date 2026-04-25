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
Download and run the brain (Llama 3.1):

`ollama pull llama3.1`

### 4. Project Setup
Create a virtual environment and install Python dependencies:

`python3 -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

## 🛠 Project Structure
- `src/audio`: Voice recognition (Faster-Whisper).
- `src/llm`: Brain logic (Ollama connection).
- `src/ui`: Graphical Interface (Upcoming).
- `assets/voice_samples`: Storage for voice cloning profiles.
- `context`: Future storage for documents (RAG).

## 📝 License
This project is licensed under the MIT License.