import pyaudio
import wave
from pydub import AudioSegment
from openai import *
import keyboard
import key


def record_until_space_pressed(output_filename):
    """
    Records audio from the default microphone until the spacebar is pressed and saves it as an MP3 file.

    Args:
        output_filename (str): The name of the output MP3 file (e.g., "output.mp3").
    """
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set the audio parameters
    sample_rate = 44100
    channels = 2
    format = pyaudio.paInt16

    # Open an audio stream
    stream = audio.open(
        format=format,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=1024,
    )

    print("Press the spacebar to stop recording...")

    frames = []

    # Record audio until spacebar is pressed
    while True:
        data = stream.read(1024)
        frames.append(data)
        if keyboard.is_pressed("space"):
            break

    print("Recording complete.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wav_filename = "audio_files/audio.wav"
    with wave.open(wav_filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))

    # Convert the WAV file to MP3
    # audio_segment = AudioSegment.from_wav(wav_filename)
    # audio_segment.export(output_filename, format="mp3")


def record_five_seconds(output_filename):
    """
    Records audio from the default microphone for 5 seconds and saves it as an MP3 file.

    Args:
        output_filename (str): The name of the output MP3 file (e.g., "output.mp3").
    """
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set the audio parameters
    sample_rate = 44100
    channels = 2
    format = pyaudio.paInt16
    duration = 5  # Duration in seconds

    # Open an audio stream
    stream = audio.open(
        format=format,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=1024,
    )

    print(f"Listening...")

    frames = []

    # Record audio for the specified duration
    for _ in range(int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    # print("Recording complete.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wav_filename = "audio_files/audio.wav"
    with wave.open(wav_filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))

    # Convert the WAV file to MP3
    # audio_segment = AudioSegment.from_wav(wav_filename)
    # audio_segment.export(output_filename, format="mp3")


# def record_whisper_audio_transcript():
#     client = OpenAI(api_key=key.OpenAIKey())
#     record_until_space_pressed("audio_files/audio.wav")

#     audio_file = open("audio_files/audio.wav", "rb")
#     transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
#     return transcript.text


def record_whisper_audio_transcript():
    client = OpenAI(api_key=key.OpenAIKey())
    record_five_seconds("audio_files/audio.wav")

    audio_file = open("audio_files/audio.wav", "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file)
    return transcript.text

def record_five_seconds(output_filename):
    """
    Records audio from the default microphone for 5 seconds and saves it as an MP3 file.

    Args:
        output_filename (str): The name of the output MP3 file (e.g., "output.mp3").
    """
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set the audio parameters
    sample_rate = 44100
    channels = 2
    format = pyaudio.paInt16
    duration = 5  # Duration in seconds

    # Open an audio stream
    stream = audio.open(
        format=format,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=1024,
    )

    print(f"Listening...")

    frames = []

    # Record audio for the specified duration
    for _ in range(int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    # print("Recording complete.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wav_filename = "audio_files/audio.wav"
    with wave.open(wav_filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))


def record_three_seconds(output_filename):
    """
    Records audio from the default microphone for 5 seconds and saves it as an MP3 file.

    Args:
        output_filename (str): The name of the output MP3 file (e.g., "output.mp3").
    """
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set the audio parameters
    sample_rate = 44100
    channels = 2
    format = pyaudio.paInt16
    duration = 3  # Duration in seconds

    # Open an audio stream
    stream = audio.open(
        format=format,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=1024,
    )

    frames = []

    # Record audio for the specified duration
    for _ in range(int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    # print("Recording complete.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wav_filename = "audio_files/audio.wav"
    with wave.open(wav_filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))

def record_whisper_audio_transcript_START():
    client = OpenAI(api_key=key.OpenAIKey())
    record_three_seconds("audio_files/audio.wav")

    audio_file = open("audio_files/audio.wav", "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file)
    
    # print("NOT FINISHED", transcript.text)
    return transcript.text


# print(record_whisper_audio_transcript())
