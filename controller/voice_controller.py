# voice_assistant/controller/voice_controller.py

from repository.voice_repository import VoiceRepository
from service.voice_service import VoiceService

class VoiceController:
    def __init__(self):
        self.voice_repo = VoiceRepository()
        self.voice_service = VoiceService()