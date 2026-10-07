import sys
import speech_recognition as sr

def transcribe(audio_file, language="en-IN"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio, language=language)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli_transcribe.py path/to/audio.wav")
        raise SystemExit(1)

    path = sys.argv[1]
    try:
        print("Transcription:")
        print(transcribe(path))
    except sr.UnknownValueError:
        print("Speech could not be understood.")
    except sr.RequestError as exc:
        print(f"Recognition service error: {exc}")
