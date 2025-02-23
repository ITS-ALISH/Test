from telegram.ext import Updater, CommandHandler

# یہاں آپ کا Telegram bot token لگائیں
TOKEN = '7674186731:AAEyKqXWwSFOCAMFP7wS3kx94p4_85MjbNY'

# /start کمانڈ کے لیے ایک فنکشن
def start(update, context):
    welcome_message = "Welcome to the bot! How can I assist you today?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

# main فنکشن جہاں bot کو ترتیب دیا جاتا ہے
def main():
    # Updater bot token کے ساتھ bot کو کنٹرول کرتا ہے
    updater = Updater(token=TOKEN, use_context=True)
    
    # dispatcher میں ہینڈلرز کو ایڈ کرتے ہیں
    dispatcher = updater.dispatcher

    #