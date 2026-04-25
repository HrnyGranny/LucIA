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
```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev python3.12-dev python3.12-venv