import tempfile
import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Speech-to-Text", page_icon="🎙️")
st.title("🎙️ Speech-to-Text Transcription")
st.write("Upload a WAV, AIFF or FLAC audio recording and convert speech into text.")

uploaded = st.file_uploader(
    "Upload audio",
    type=["wav", "aiff", "aif", "flac"]
)

language = st.selectbox(
    "Recognition language",
    [
        ("English (India)", "en-IN"),
        ("English (US)", "en-US"),
        ("Hindi (India)", "hi-IN"),
    ],
    format_func=lambda x: x[0]
)

if uploaded:
    st.audio(uploaded)

    if st.button("Transcribe"):
        recognizer = sr.Recognizer()

        suffix = "." + uploaded.name.split(".")[-1].lower()
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded.getbuffer())
            audio_path = tmp.name

        try:
            with sr.AudioFile(audio_path) as source:
                audio = recognizer.record(source)

            with st.spinner("Converting speech to text..."):
                text = recognizer.recognize_google(
                    audio,
                    language=language[1]
                )

            st.success("Transcription completed")
            st.text_area("Recognized text", text, height=180)

        except sr.UnknownValueError:
            st.error("The speech could not be understood clearly.")
        except sr.RequestError as exc:
            st.error(
                "The speech-recognition service could not be reached. "
                "Check your internet connection and try again."
            )
            st.caption(str(exc))
        except Exception as exc:
            st.error(f"Error: {exc}")
