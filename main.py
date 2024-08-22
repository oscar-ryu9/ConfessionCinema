import speech_recognition as sr

def transcribe_audio(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    # Recognize speech
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Sorry, could not understand audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

# Example usage
audio_file = "E:\Projects\BRAINROT\ConfessionCinema\one.wav"  # Provide path to your audio file
captions = transcribe_audio(audio_file)
print("Captions:", captions)
