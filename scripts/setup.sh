#!/bin/bash

# ImageInsight Bot Setup Script
# This script helps you set up the project quickly

set -e

echo "🚀 Setting up ImageInsight Bot..."
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python version $python_version is too old. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python $python_version detected"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "🔧 Creating .env file from template..."
    cp env.example .env
    echo "⚠️  Please edit .env file with your API keys:"
    echo "   - TELEGRAM_API_TOKEN: Get from @BotFather"
    echo "   - GROQ_API_KEY: Get from https://console.groq.com/"
    echo ""
    echo "📝 Edit .env file and then run: python main.py"
else
    echo "✅ .env file already exists"
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama is not installed. Please install it from https://ollama.ai/"
    echo "   After installation, run: ollama pull llava"
else
    echo "✅ Ollama detected"
    # Check if llava model is available
    if ollama list | grep -q "llava"; then
        echo "✅ llava model is available"
    else
        echo "📥 Pulling llava model..."
        ollama pull llava
    fi
fi

echo ""
echo "🎉 Setup complete!"
echo "=================="
echo "Next steps:"
echo "1. Edit .env file with your API keys"
echo "2. Run: python main.py"
echo "3. Start chatting with your ImageInsight Bot on Telegram!"
echo ""
echo "For help, run: make help" 
