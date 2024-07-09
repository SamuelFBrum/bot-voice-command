# voice_assistant/repository/voice_repository.py

import speech_recognition as sr

class VoiceRepository:
    def __init__(self):
        self.recognizer = sr.Recognizer()