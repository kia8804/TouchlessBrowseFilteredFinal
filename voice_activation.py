import openai
import threading
import time
import sounddevice as sd
import numpy as np
import key
import base64

# Set your OpenAI API key
openai.api_key = key.OpenAIKey()

# Variable to track whether voice activation is on or off
voice_activation_on = False

# Event to signal termination when "start," "scroll up," "scroll down," or "click" is detected
termination_event = threading.Event()

# Function to handle voice commands


def handle_voice_command():
    global voice_activation_on

    while voice_activation_on and not termination_event.is_set():
        try:
            # Record audio from the microphone
            fs = 44100  # Sample rate
            duration = 5  # Recording duration in seconds
            audio_input = sd.rec(int(fs * duration),
                                 samplerate=fs, channels=1, dtype=np.int16)
            sd.wait()

            # Convert audio data to base64 for OpenAI API
            audio_base64 = base64.b64encode(
                audio_input.tobytes()).decode('utf-8')

            # Use Whisper ASR API to decode audio
            response = openai.Whisper.decode(
                model="whisper-large", audio=audio_base64, temperature=0.6, max_tokens=60)

            if "start" in response:
                termination_event.set()
                print("Francis awake")
            elif "scroll up" in response:
                termination_event.set()
                print("Scroll up")
            elif "scroll down" in response:
                termination_event.set()
                print("Scroll down")
            elif "click" in response:
                termination_event.set()
                print("Click")

        except Exception as e:
            print(f"Error: {e}")

# Function to turn on voice activation


def turn_on_voice_activation():
    global voice_activation_on

    voice_activation_on = True
    threading.Thread(target=handle_voice_command).start()
    print("Voice activation turned ON")

# Function to turn off voice activation


def turn_off_voice_activation():
    global voice_activation_on
    voice_activation_on = False
    termination_event.set()
    print("Voice activation turned OFF")


# Example usage
turn_on_voice_activation()

# Check for "start," "scroll up," "scroll down," or "click" in a non-blocking way
while not termination_event.is_set():
    time.sleep(0.0000000005)

# Turn off voice activation when "start," "scroll up," "scroll down," or "click" is said
turn_off_voice_activation()
