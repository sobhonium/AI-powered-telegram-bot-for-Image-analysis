# ImageInsight Bot - AI-Powered Image Analysis

A Telegram bot that can analyze images and answer questions about them using AI models. The bot combines Ollama for image analysis and Groq for text processing.

## Features

- 🔍 **Advanced Image Analysis**: Upload images and get detailed AI-powered descriptions
- 💬 **Intelligent Conversations**: Ask questions about uploaded images with context-aware responses
- 🤖 **Dual AI Architecture**: Uses Ollama (llava) for image analysis and Groq for text processing
- 📱 **Seamless Telegram Integration**: Easy to use through Telegram interface
- 🧠 **Context Memory**: Remembers uploaded images for follow-up questions

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Groq API key
- Telegram Bot Token

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/imageinsight-bot.git
   cd imageinsight-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama** (if not already installed)
   ```bash
   # Follow instructions at https://ollama.ai/
   # Then pull the llava model
   ollama pull llava
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   TELEGRAM_API_TOKEN=your_telegram_bot_token
   GROQ_API_KEY=your_groq_api_key
   ```

## Configuration

### Getting API Keys

1. **Telegram Bot Token**:
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Create a new bot with `/newbot`
   - Copy the provided token

2. **Groq API Key**:
   - Sign up at [Groq Console](https://console.groq.com/)
   - Generate an API key
   - Copy the key

### Environment Setup

The bot uses environment variables for configuration. Create a `.env` file:

```env
TELEGRAM_API_TOKEN=your_telegram_bot_token_here
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

1. **Start the bot**
   ```bash
   python main.py
   ```

2. **Use the bot on Telegram**:
   - Send `/start` to begin
   - Upload an image to get a description
   - Ask questions about the uploaded image

## How it Works

1. **Image Upload**: When you send an image, the bot:
   - Downloads the image locally
   - Uses Ollama with the llava model to analyze the image
   - Provides a detailed description

2. **Question Answering**: When you ask questions:
   - If an image was previously uploaded, the bot uses it for context
   - Uses Groq's Llama model for text processing
   - Provides relevant answers based on the image content

## Project Structure

```
imageinsight-bot/
├── main.py              # Main bot application
├── requirements.txt      # Python dependencies
├── README.md           # This file
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore file
└── images/             # Downloaded images (created automatically)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

1. **Ollama not running**: Make sure Ollama is installed and running
   ```bash
   ollama serve
   ```

2. **Missing llava model**: Pull the required model
   ```bash
   ollama pull llava
   ```

3. **API key errors**: Verify your API keys are correct in the `.env` file

4. **Permission errors**: Ensure the bot has permission to create the `images/` directory

## Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure
- The bot stores images locally - consider implementing cleanup

## Support

If you encounter any issues, please:
1. Check the troubleshooting section
2. Open an issue on GitHub
3. Provide detailed error messages and steps to reproduce 