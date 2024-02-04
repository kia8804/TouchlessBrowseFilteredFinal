import tkinter as tk
from threading import Thread
from record_audio_convert_to_text import *
from text_to_speech import *
from ask_google_SERP import *
from format_google_results_GPT import *
from select_website import *
from open_selected import *
from voice_activation import *

def update_text(new_text):
    # Function to update the text of the label
    global label
    label.config(text=new_text)

def handle_voice_commands():
    keep_looping = True
    while keep_looping:
        voice_handle = handle_voice_command()
        if True:
            update_text("Listening...")

            # Record audio and convert to text
            question = record_whisper_audio_transcript()
            update_text(f"User: {question}")

            # Ask google and get the responses in list format, then pass it to ChatGPT to make it into a nice summary
            relevant_google_search_response = ask_google_SERP(question)
            cleaned_GPT_summary_links = format_google_results_GPT(relevant_google_search_response)

            update_text(f"Assistant: {cleaned_GPT_summary_links}")

            # Get the ChatGPT response and convert it to speech
            text_to_speech(cleaned_GPT_summary_links)
            website_number = select_website(cleaned_GPT_summary_links)
            open_selected(relevant_google_search_response, website_number)
            # Optionally break or update keep_looping to false to exit the loop

def start_voice_commands_thread():
    voice_thread = Thread(target=handle_voice_commands)
    voice_thread.start()

# GUI setup
root = tk.Tk()
root.title("Touchless Browse")
root.geometry("400x300")  # Increased height for better visibility
root.configure(bg='#2a2a2a')
label = tk.Label(root, text="Default Text", font=('Helvetica', 16), fg='white', bg='#2a2a2a')
label.pack(expand=True)

# Update the label to show the app is idle initially
update_text("Idle")

# Start the voice command handling in a separate thread to keep the GUI responsive
start_voice_commands_thread()

# Start the main loop of the GUI
root.mainloop()
