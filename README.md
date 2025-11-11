# Voice-Based Virtual Assistant (Python Project)

A lightweight, voice-controlled Python virtual assistant that can listen, talk, remember notes, tell jokes, open websites, do basic math, and even respond to random queries using an AI fallback model (Ollama with Mistral).

-

Features ❯️

- **Speech Recognition** : Understands your spoken commands
- **Text-to-Speech** : replies back with natural-sounding speech
- **Memory** : remembers small notes you tell it
- **Date & Time** : Tells you the current date or time
- **Web Control** : Opens Google and YouTube directly
- **Calculations** : Performs basic math operations
- **Entertainment** : Tells jokes, flips coins, and rolls dice

- **AI Fallback** : Uses Ollama’s Mistral model for intelligent responses to general queries

-

Tech Stack
- **Language:** Python 3.x
- **Libraries:
- `pyttsx3` for text to speech
`- `SpeechRecognition` for voice input
- `pyjokes` for humor
- `pyaudio` for microphone support

- `subprocess` & `webbrowser` for external tasks

- Optional: `ollama` CLI for AI fallback

---
Installation 
1. Clone the repository
```bash git clone https://github.com/YOUR_USERNAME/virtual-assistant.git cd virtual-assistant
