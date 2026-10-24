# AI Desktop Virtual Assistant 🤖

## 📌 About the Project

The **AI Desktop Virtual Assistant** is a Python-based desktop application designed to perform everyday tasks using voice commands or text input. It provides an interactive graphical user interface (GUI) where users can communicate with the assistant and receive responses in both text and voice.

The assistant can open websites, provide the current time and date, check weather information, play music, and manage files and folders. It also supports keyboard shortcuts for quick access to common commands.

## ✨ Features

- **Voice Recognition:** Accepts voice commands using a microphone.
- **Text Input:** Allows users to type commands through the GUI.
- **Text-to-Speech:** Responds to users with spoken output.
- **Website Access:** Opens Google and YouTube.
- **Music:** Opens Gaana for music and songs.
- **Date and Time:** Provides the current time, date, and day.
- **Weather Updates:** Displays the temperature and weather conditions for a specified city in India.
- **File and Folder Management:** Searches for folders and supports copying and moving files or folders.
- **Keyboard Shortcuts:** Executes frequently used commands quickly.
- **Interactive GUI:** Built using Tkinter with buttons for voice input, sending text commands, and clearing the conversation.

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Tkinter** – Graphical user interface
- **SpeechRecognition** – Voice recognition
- **PyAudio** – Microphone input support
- **pyttsx3** – Text-to-speech functionality
- **Pillow (PIL)** – Image handling in the GUI
- **Requests** – Fetching weather information from an API
- **OpenWeatherMap API** – Weather data
- **OS and Shutil** – File and folder operations
- **Datetime** – Date and time information
- **Webbrowser** – Opening websites

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
| `Ctrl + G` | Open Google |
| `Ctrl + Y` | Open YouTube |
| `Ctrl + T` | Show current time |
| `Ctrl + D` | Show current date |
| `Ctrl + M` | Open music |
| `Ctrl + L` | Clear the conversation |
| `Ctrl + Shift + D` | Show current day |
| `Ctrl + Shift + S` | Shut down the assistant |

## 💬 Example Commands

- "Hello"
- "What is your name?"
- "Open Google"
- "Open YouTube"
- "Play music"
- "What is the time?"
- "What is today's date?"
- "What day is it?"
- "What is the weather in Delhi?"
- "Open folder Downloads"
- "Copy file report from Documents to Desktop"
- "Move folder project from Desktop to Documents"
- "Quit"

## 📂 Project Structure

```text
AI-Desktop-Virtual-Assistant/
│
├── GUI.py                 # Main graphical user interface
├── action.py              # Processes commands and performs actions
├── speech_to_text.py      # Converts voice input into text
├── text_to_speech.py      # Converts text responses into speech
├── weather.py             # Fetches weather information
├── image/
│   └── assistant.png      # Assistant image displayed in the GUI
└── README.md              # Project documentation
```

## 🔑 API Configuration

This project uses the OpenWeatherMap API to retrieve weather information.

1. Create an account on [OpenWeatherMap](https://openweathermap.org/).
2. Generate your API key.
3. Store the key securely and configure it in `weather.py`.

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Developing desktop applications using Python and Tkinter.
- Integrating voice recognition and speech synthesis.
- Handling user input and processing commands.
- Working with external APIs to retrieve weather data.
- Automating file and folder operations.
- Implementing keyboard shortcuts and GUI event handling.
- Organizing a Python project into separate modules.

## 🚀 Future Improvements

- Improve voice recognition accuracy and response speed.
- Add more voice-controlled system operations.
- Support additional websites and online services.
- Enhance the GUI design and user experience.
- Add more intelligent command understanding.

## 👩‍💻 Author
Ekshnoordeep Kaur
