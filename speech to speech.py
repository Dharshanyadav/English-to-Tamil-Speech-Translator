import gradio as gr
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import tempfile
import time 



def translate_speech(audio_filepath):
    if not audio_filepath:
        return "Error: No audio recorded. Please try recording again.", "", None

    recognizer = sr.Recognizer()
    recognized_text = ""
    translated_text = ""
    output_audio_path = None

    try:
        print(f"Processing audio file: {audio_filepath}")
        with sr.AudioFile(audio_filepath) as source:
            audio_data = recognizer.record(source)
            print("Recognizing English speech...")
            recognized_text = recognizer.recognize_google(audio_data, language='en-US')
            print(f"Recognized English: {recognized_text}")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "Error: Could not understand the spoken English.", "", None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return f"Error: Could not connect to Google Speech Recognition service. Check internet connection. ({e})", "", None
    except Exception as e:
        print(f"An unexpected error occurred during speech recognition: {e}")
        return f"Error during STT: {e}", "", None

    if not recognized_text:
         return "Error: Recognition failed, no text to translate.", "", None

    try:
        print(f"Translating '{recognized_text}' to Tamil...")
        translated_text = GoogleTranslator(source='en', target='ta').translate(recognized_text)
        print(f"Translated Tamil: {translated_text}")

    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return recognized_text, f"Error during Translation: {e}", None

    if not translated_text:
        return recognized_text, "Error: Translation resulted in empty text.", None

    try:
        print(f"Generating Tamil speech for: {translated_text}")
        tts = gTTS(text=translated_text, lang='ta', slow=False)

        timestamp = int(time.time())
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f'_{timestamp}.mp3')
        output_audio_path = temp_file.name
        temp_file.close() 
        tts.save(output_audio_path)
        print(f"Saved Tamil speech to: {output_audio_path}")

    except Exception as e:
        print(f"An error occurred during Text-to-Speech generation: {e}")
        return recognized_text, translated_text, f"Error during TTS: {e}" 
    return recognized_text, translated_text, output_audio_path


input_audio = gr.Audio(sources="microphone", type="filepath", label="Speak English Here")

output_recognized_text = gr.Textbox(label="Recognized English Text")
output_translated_text = gr.Textbox(label="Translated Tamil Text")
output_tamil_audio = gr.Audio(label="Translated Tamil Speech", type="filepath") # Use filepath for gTTS output

iface = gr.Interface(
    fn=translate_speech,
    inputs=input_audio,
    outputs=[output_recognized_text, output_translated_text, output_tamil_audio],
    title="English to Tamil Speech Translator",
    description="Record your English speech using the microphone. The app will transcribe it, translate it to Tamil, and speak the Tamil translation.",
    allow_flagging="never" )



print("Launching Gradio Interface...")
iface.launch()
