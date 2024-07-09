# voice_assistant/service/voice_service.py

import pyttsx3
from datetime import datetime

class VoiceService:
    def __init__(self):
        self.engine = pyttsx3.init()