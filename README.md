# AI Voice-Text Assistant

AI-based assistant that allows users to interact with both voice and text. It integrates voice input recognition and text-based input processing to generate meaningful responses using Google's Generative AI and translation services.

## Features

- **Voice Input**: Users can speak their queries, and the system will recognize and transcribe the speech to text.
- **Text Input**: Users can type their queries if preferred.
- **Multilingual Support**: The assistant can translate non-English text into English for accurate processing.
- **Generative AI Integration**: Utilizes Google's Generative AI (Gemini) to generate intelligent and contextually relevant responses.

## Installation

To set up the project on your local machine, follow the steps below.

### 1. Clone the Repository

```bash
git clone https://github.com/FARINATTAR/AI-TextVoice-Assistant.git
cd AI-TextVoice-Assistant
```

### 2. Set API Keys

You’ll need to set up API key for Gemini

- **Google Generative AI (Gemini)**

Add these keys to your `.env` file (make sure to create the file in the root directory if it doesn’t exist):

```
GEMINI_API_KEY="Your Api key"
```

### 3. Run the Application

```bash
python main.py
```

Now, you can start interacting with your assistant via voice or text!

## Usage

- **Text Input**: Type your question when prompted.
- **Voice Input**: Say your question when prompted, and the assistant will transcribe your speech and respond accordingly.

To exit the program, type `exit` when prompted.
