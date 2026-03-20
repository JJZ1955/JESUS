import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # Load the Whisper model
    result = model.transcribe(file_path, language="es")  # Transcribe audio to text in Spanish
    return result["text"]

# Example usage
if __name__ == '__main__':
    file_path = 'path_to_your_audio_file.wav'
    transcription = transcribe_audio(file_path)
    print(transcription)