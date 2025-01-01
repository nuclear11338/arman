import telebot
import openai

# Replace with your bot token and OpenAI API key
TELEGRAM_API_TOKEN = "7677067483:AAH4nLqNPyZ46C_C8J3cmXVeZOvtnEyflRE"
OPENAI_API_KEY = ""

# Initialize bot and OpenAI
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
openai.api_key = OPENAI_API_KEY

# Function to generate AI-based responses
def generate_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return "⚠️ Sorry, I couldn't process your request right now. Please try again later."

# Start command
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "👋 Hi! I'm your AI chatbot. Type anything, and I'll reply with an auto-generated response!"
    )

# Handle all text messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    bot.send_message(message.chat.id, "🤔 Let me think...")
    response = generate_response(user_message)
    bot.send_message(message.chat.id, response)

# Polling
bot.polling()
