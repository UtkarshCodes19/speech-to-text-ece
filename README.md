# Speech-to-Text Transcription using Python

A simple speech-recognition application that converts recorded speech into text.

## Objective
Capture an audio recording, process the speech signal and produce a text transcription.

## ECE Connection
The project can be represented as:

**Human Speech → Microphone → Electrical/Audio Signal → Sampling & Digital Representation → Speech Recognition → Text**

From an ECE perspective, the microphone acts as a transducer, converting acoustic energy into an electrical signal. The signal is then represented digitally and processed by a speech-recognition system. This connects the project with Signals and Systems, Digital Signal Processing, audio processing and embedded systems.

The current implementation is a software prototype. A future embedded version could use a microphone connected to a microcontroller, DSP, Raspberry Pi, or other edge-computing platform.

## Technologies
- Python
- SpeechRecognition
- Streamlit
- Google speech-recognition service through the SpeechRecognition library

## Supported Audio
The application accepts:
- WAV
- AIFF/AIF
- FLAC

MP3 files may require additional audio-conversion software and are not used by the default application.

## How to Run

### 1. Create a virtual environment
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the application
```bash
streamlit run app.py
```

### 4. Use the application
1. Upload a supported audio file.
2. Select the language.
3. Click **Transcribe**.
4. Read the generated text.

## Command-Line Version
You can also transcribe a file directly:
```bash
python cli_transcribe.py sample.wav
```

## Project Workflow
**Audio Input → Digital Audio → Speech Recognition → Text Output**

## Future Improvements
- Add real-time microphone input.
- Add noise filtering and voice activity detection.
- Add local/offline speech recognition.
- Deploy on Raspberry Pi or another embedded platform.
- Add DSP-based preprocessing such as filtering and feature extraction.

## Important Note
The default recognizer uses an online recognition service, so an internet connection is required for transcription. Do not upload sensitive or private recordings.
