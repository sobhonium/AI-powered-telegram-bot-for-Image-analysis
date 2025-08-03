import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from groq import Groq
import nest_asyncio
from PIL import Image
import ollama
from dotenv import load_dotenv


def generate_text(instruction, file_path):
    result = ollama.generate(
        model='llava',
        prompt=instruction,
        images=[file_path],
        stream=False
    )['response']
    return result

# Load environment variables
load_dotenv()

# Apply nest_asyncio for environments like Jupyter
nest_asyncio.apply()

# === CONFIG ===
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Validate required environment variables
if not TELEGRAM_API_TOKEN:
    raise ValueError("TELEGRAM_API_TOKEN environment variable is required")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is required")

# === Groq Client Setup ===
client = Groq(api_key=GROQ_API_KEY)

# === Conversation History ===
hist = {"latest_image_path": None}

# === Groq Response Function ===
def get_groq_response(user_message):
    # Check if there's a saved image
    if hist["latest_image_path"] and os.path.exists(hist["latest_image_path"]):
        # Use the image to answer the question
        output = generate_text(user_message, hist["latest_image_path"])
        return output
    else:
        # No image available, use regular Groq chat
        messages = [
            {
                "role": "system",
                "content": "You are an assistant answering questions and helping."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        response_content = chat_completion.choices[0].message.content
        return response_content

# === Handlers ===
async def start(update: Update, context: CallbackContext):
    print("Start command received")
    await update.message.reply_text("🔍 Welcome to ImageInsight Bot! Send me an image and I'll provide intelligent analysis and answer your questions about it!")

async def handle_message(update: Update, context: CallbackContext):
    try:
        user_message = update.message.text
        bot_response = get_groq_response(user_message)
        await update.message.reply_text(bot_response)
    except Exception as e:
        print(f"Error in handle_message: {e}")
        await update.message.reply_text("Sorry, I encountered an error processing your message.")

async def handle_photo(update: Update, context: CallbackContext):
    try:
        # Create images directory if it doesn't exist
        os.makedirs("images", exist_ok=True)
        
        photo_file = await update.message.photo[-1].get_file()
        file_path = f"images/{update.message.message_id}.jpg"

        await photo_file.download_to_drive(file_path)

        instruction = "Can you describe this image in detail?"
        output = generate_text(instruction, file_path)

        # Save the image path for future questions
        hist["latest_image_path"] = file_path
        
        await update.message.reply_text(f"🔍 **Image Analysis Complete!**\n\n{output}\n\n💡 Now you can ask me intelligent questions about this image!")
        
    except Exception as e:
        print(f"Error in handle_photo: {e}")
        await update.message.reply_text("Sorry, I encountered an error processing your image.")

# === Main Bot Runner ===
async def main():
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("🔍 ImageInsight Bot is running...")
    await application.run_polling()

# === Entry Point ===
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())