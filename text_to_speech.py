# from pathlib import Path
from openai import *
import record_audio_convert_to_text
import key
from playsound import playsound

"""
MAIN FUNCTION
Function to take a string of text and convert it to speech

Params:
    text - a string of the provided text
    speech_file_path - a string of the file path to save the audio file to

Returns:
    Nothing
"""


def text_to_speech(text, speech_file_path="audio_files/GPTSpeech.mp3"):
    client = OpenAI(api_key=key.OpenAIKey())
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    response.stream_to_file("C:/Users/adhit/OneDrive/Files/Documents/QHacks 2023/github/VoiceBrowse/audio_files/GPTSpeech.mp3")
    playsound("C:/Users/adhit/OneDrive/Files/Documents/QHacks 2023/github/VoiceBrowse/audio_files/GPTSpeech.mp3")


def text_to_speech_TEST():
    client = OpenAI(api_key=key.OpenAIKey())

    text = record_audio_convert_to_text.record_whisper_audio_transcript()
    # CHANGE THE CALL BELOW TO WHATEVER IS BEING RETURNED
    # text = "sample text"

    speech_file_path = "VoiceBrowse/audio_files/GPTSpeech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    response.stream_to_file(speech_file_path)


# text_to_speech()
# text_to_speech("Hi there")