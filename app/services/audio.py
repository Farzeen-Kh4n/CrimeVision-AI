import whisper

class AudioAnalyzer:
    def __init__(self, model_size="base"):
        print("Loading Whisper Audio Model...")
        # Lightweight whisper model taaki laptop par load na pade
        self.model = whisper.load_model(model_size)
        print("Whisper Model loaded successfully!")

    def transcribe_audio(self, audio_path):
        """
        Activity 3.1: Implement audio transcription for witness statements.
        """
        result = self.model.transcribe(audio_path)
        return result["text"]

    def extract_key_events(self, transcript):
        """
        Activity 3.2: Extract key events and generate structured timelines.
        """
        events = []
        transcript_lower = transcript.lower()
        
        if "gun" in transcript_lower or "fire" in transcript_lower or "weapon" in transcript_lower:
            events.append({"timeline": "Critical Threat", "description": "Firearm or weapon mention detected in audio."})
        elif "help" in transcript_lower or "emergency" in transcript_lower:
            events.append({"timeline": "Distress Signal", "description": "Call for help or emergency detected."})
        else:
            events.append({"timeline": "General Statement", "description": "Standard witness or background audio logged."})
            
        return events