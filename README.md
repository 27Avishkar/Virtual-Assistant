# Virtual Assistant Project

This project is a Python-based virtual assistant capable of understanding and responding to voice commands. It utilizes speech recognition and text-to-speech technologies to interact with users naturally. The assistant can perform a variety of tasks, including opening applications, managing system settings, and retrieving information such as the current weather.

## Features

- **Voice Interaction**: Uses speech recognition to process user commands and text-to-speech to provide audible responses.
- **Automated Tasks**: Opens applications (e.g., Notepad, Microsoft Word), adjusts system settings (e.g., brightness, volume), and performs web-based tasks.
- **Information Retrieval**: Provides current time, date, weather information.
- **System Control**: Manages system brightness and interacts with the operating system to launch applications.

## Technologies Used

- **Python**: Core language for scripting and executing commands.
- **SpeechRecognition**: Library for converting speech to text.
- **pyttsx3**: Library for converting text to speech.
- **webbrowser**: Module for web automation tasks.
- **OS Module**: For interacting with the operating system and executing system commands.

## How to Use

1. Clone the repository to your local machine.
2. Ensure you have the necessary libraries installed:
    ```sh
    pip install SpeechRecognition pyttsx3
    ```
3. Run the main script:
    ```sh
    python main.py
    ```
4. Speak commands such as "Open Google", "What is the weather?", or "Increase brightness".

## Example Commands

- "What is your name?"
- "Open YouTube"
- "Play music"
- "What is the time now?"
- "Open Notepad"
