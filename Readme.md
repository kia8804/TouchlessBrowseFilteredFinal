# Touchless Browse

## What does it do

Welcome to Touchless Browse, a revolutionary web browser that brings the science fiction fantasy of hands-free internet navigation to reality. This innovative project combines natural language processing, computer vision, and voice recognition and transcription models to provide a unique web browsing experience where physical interaction with a mouse and keyboard is a thing of the past.

**Key Features:**
- **Voice-Powered Google Searches:** Utilize your voice and the Whisper AI model for seamless Google searches, complete with GPT-powered summaries of links.
- **Voice & Hand Gesture Navigation:** Scroll and click through sites using just your voice. Plus, control a cursor with your index finger movements captured by your webcam, mimicking futuristic "holographic" control.

Touchless Browser is at the forefront of redefining how information is consumed and the internet is navigated, offering an unmatched level of innovation.

## How we built it

Touchless Browse is built on a blend of voice recognition, natural language processing, and gesture recognition technologies. Here's how we pieced it together:

- **Voice Input:** We employed the Whisper AI model for translating user voice input into text.
- **Natural Language Processing:** ChatGPT 3.5 API was used for processing user input and organizing web search results from the SERPER API (Google Search results). The results are reformatted and provided to the user through text-to-speech Python libraries.
- **Audio Processing:** We used PyAudio, FFMpeg, and PyDub for sophisticated audio processing.
- **Gesture Recognition:** OpenCV was utilized for facial recognition, modified to track the user's finger movements for cursor control via PyAutoGui.

## Challenges we ran into

The journey wasn't smooth, and we faced several challenges:
- **Eye Tracking for Scrolling:** Initially, we attempted to implement scrolling using eye tracking. However, the detailed nature of eye movements and the need for minimal webcam calibration made this impractical.
- **Gesture Recognition:** Implementing index finger movement recognition using image recognition libraries like OpenCV was a substantial challenge.
- **Speech Recognition Limitations:** We encountered issues with the native Python text-to-speech `speechrecognition` library, leading us to opt for OpenAI's Whisper API for its efficiency.
- **Managing Complexity:** Coordinating numerous functions across various branches was a significant task, making our documentation process crucial.

Despite these challenges, we emerged with a rewarding end product.

## Accomplishments that we're proud of

- **Integration of Advanced AI Technologies:** Successfully integrating computer vision, voice recognition, and natural language processing.
- **Gesture Recognition Module:** Developing a module that allows basic navigation through simple hand movements.
- **Realizing a Sci-Fi Dream:** Bringing to life a vision of a keyboardless and mouseless interface for accessing information.

## What we learned

- **Integration of AI Technologies:** The importance of integrating various AI technologies to build practical applications.
- **Product Differentiation:** The necessity of distinguishing our product in the market, leading to the unique touchless feature.
- **Limits of AI Models:** Understanding that AI models are tools that require human ingenuity to be fully utilized in applications.

## What's next for Touchless Browse

Looking forward, we aim to:
- **Enhance Gesture Recognition:** Expand the gesture recognition capabilities for more complex commands.
- **Improve Stability and Accuracy:** Focus on the stability and accuracy of voice and gesture inputs.
- **Enhance Virtual Keyboard and Mouse Functions:** Improve the virtual keyboard and mouse stability and scrolling functionalities.
- **AI-Driven Content Summarization:** Integrate AI-driven content summarization for enhanced browsing.

Our ultimate goal is to create a fully immersive, voice and gesture-based browsing experience accessible to all users.

## Security Note

For security reasons, API keys located in `key.py` have been omitted from the public version of our repository.

## Built With

![computer-vision](https://img.shields.io/badge/-computer--vision-blue) ![github](https://img.shields.io/badge/-github-black) ![gpt](https://img.shields.io/badge/-gpt-red) ![opencv](https://img.shields.io/badge/-opencv-green) ![pyaudio](https://img.shields.io/badge/-pyaudio-yellow) ![pydub](https://img.shields.io/badge/-pydub-orange) ![python](https://img.shields.io/badge/-python-blue) ![whisper](https://img.shields.io/badge/-whisper-lightgrey)
