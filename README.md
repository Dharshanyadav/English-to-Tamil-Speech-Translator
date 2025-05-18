# English-to-Tamil Speech Translator

A web application that translates spoken English to Tamil speech in real-time using speech recognition, translation, and text-to-speech synthesis.

## Features

- **Speech Recognition**: Converts spoken English to text
- **Language Translation**: Translates English text to Tamil
- **Speech Synthesis**: Converts Tamil text to spoken audio
- **User-Friendly Interface**: Simple web UI built with Gradio

## Demo

![English-to-Tamil Speech Translator Demo](https://github.com/Dharshanyadav/English-to-Tamil-Speech-Translator/blob/cfd0fbd3eef1718408a88eb6cf888952adf9d510/image_2025-05-18_132803978.png)

## Requirements

- Python 3.6+
- Internet connection (for Google's speech recognition and translation services)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/english-tamil-translator.git
cd english-tamil-translator
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Dependencies

This project relies on the following Python libraries:
- gradio
- SpeechRecognition
- deep-translator
- gTTS (Google Text-to-Speech)

You can install all dependencies using the included requirements.txt file:
```
gradio>=3.50.2
SpeechRecognition>=3.10.0
deep-translator>=1.11.4
gTTS>=2.3.2
```

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your web browser and navigate to the displayed URL (typically http://127.0.0.1:7860/)

3. Click the microphone button and speak clearly in English

4. The application will:
   - Transcribe your English speech to text
   - Translate the English text to Tamil
   - Generate Tamil speech from the translated text
   - Display all outputs in the interface
 ![Image Alt](image_url)

## How It Works

The application follows these steps:

1. **Speech-to-Text (STT)**: Uses Google's Speech Recognition API to convert spoken English to text
2. **Translation**: Utilizes Google Translator to translate English text to Tamil
3. **Text-to-Speech (TTS)**: Employs Google's Text-to-Speech service to convert Tamil text to spoken audio

## Limitations

- Requires an internet connection to access Google's services
- Speech recognition accuracy depends on audio quality and accent
- Translation quality may vary for complex sentences or specific terminology
- Character limit restrictions from the underlying APIs

## Troubleshooting

- **No audio recorded**: Ensure your microphone is properly connected and has necessary permissions
- **Recognition failed**: Speak clearly and ensure minimal background noise
- **Translation errors**: Try simplifying the sentence or checking internet connectivity
- **Audio playback issues**: Verify your browser supports audio playback and your speakers are working

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google for their Speech Recognition, Translation, and Text-to-Speech services
- Gradio team for the simple web interface framework
- All open-source contributors to the libraries used in this project
