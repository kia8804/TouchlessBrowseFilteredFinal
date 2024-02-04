from record_audio_convert_to_text import *
from text_to_speech import *
from ask_google_SERP import *
from format_google_results_GPT import *
from select_website import *
from open_selected import *
# from voice_activation import *
from openai import *
import pyautogui
import playsound

keep_looping = True
while keep_looping:
    voice_handle = record_whisper_audio_transcript_START().lower()
    if "francis" in voice_handle: 
        text_to_speech("How can I help you?")
        
        print("Listening...")

        # Record audio and convert to text
        question = record_whisper_audio_transcript()
        print("User:", question)
        text_to_speech("I will check that on Google for you. Please wait...")
        # Ask google and get the responses in list format, then pass it to ChatGPT to make it into a nice summary
        relevant_google_search_response = ask_google_SERP(question)
        cleaned_GPT_summary_links = format_google_results_GPT(
            relevant_google_search_response
        )

        print("Assistant:", cleaned_GPT_summary_links)

        # Get the ChatGPT response and convert it to speech
        text_to_speech(cleaned_GPT_summary_links)
        website_number = select_website(cleaned_GPT_summary_links)
        open_selected(relevant_google_search_response, website_number)
        # break

    elif "up" in voice_handle:
        print("Scrolling up...")
        pyautogui.scroll(500) 
        # break

    elif "down" in voice_handle:
        print("Scrolling down...")
        pyautogui.scroll(-500)  # Scrolls up

    elif "click" in voice_handle:
        print("Clicking...")
        pyautogui.click()  # Scrolls up
