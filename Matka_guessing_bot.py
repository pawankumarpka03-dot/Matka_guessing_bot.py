from telegram.ext import Updater, CommandHandler
import json

# === CHANGE KARNE WALA PART ===
TOKEN = "7389112963:AAEhvxHiwRuRSdoa5JBCoqdefSpeVbDXQhM"   # BotFather ka token
ADMIN_USERNAME = "YourTelegramUsername"  # Apna telegram username (without @)
# ==============================

premium_users = []

def load_users():
    global premium_users
    try:
        with open("premium.json", "r") as f:
            premium_users = json.load(f)
    except:
        premium_users = []

def save_users():
    with open("premium.json", "w") as f:
        json.dump(premium_users, f)

def start(update, context):
    user_id = update.message.chat_id
    if user_id in premium_users:
        update.message.reply_text("✅ Welcome Premium Member!\nUse /guess for today’s full game numbers.")
    else:
        update.message.reply_text(
            "🙏 Welcome to Matka Premium Guessing Bot 🙏\n\n"
            "🔹 Free Guess: /freeguess\n"
            "🔹 Premium Guess: /guess (Only VIP)\n\n"
            f"👉 Premium lene ke liye Contact @{ADMIN_USERNAME}"
        )

def freeguess(update, context):
    update.message.reply_text("🎲 Free Guess: Jodi 4-7, Panna 128")

def guess(update, context):
    user_id = update.message.chat_id
    if user_id in premium_users:
        update.message.reply_text(
            "🔥 Premium Guess 🔥\n\n"
            "📌 Kalyan Day: 47-28-389\n"
            "📌 Kalyan Night: 65-29-478\n"
            "📌 Time Bazar: 18-49-236\n"
            "📌 Milan Day: 53-62-147\n"
            "📌 Milan Night: 84-17-269\n"
            "📌 Rajdhani Day: 73-29-358\n"
            "📌 Rajdhani Night: 25-68-479"
        )
    else:
        update.message.reply_text(f"❌ You are not a premium member.\n👉 Contact @{ADMIN_USERNAME} for upgrade.")

def addpremium(update, context):
    user = update.message.from_user
    if user.username == ADMIN_USERNAME:  # Sirf Admin
        try:
            user_id = int(context.args[0])
            if user_id not in premium_users:
                premium_users.append(user_id)
                save_users()
                update.message.reply_text(f"✅ User {user_id} added to Premium.")
            else:
                update.message.reply_text("⚠️ User already in Premium list.")
        except:
            update.message.reply_text("❌ Use: /addpremium USER_ID")
    else:
        update.message.reply_text("🚫 Only Admin can add premium users.")

# Load premium members
load_users()

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("freeguess", freeguess))
dp.add_handler(CommandHandler("guess", guess))
dp.add_handler(CommandHandler("addpremium", addpremium))

updater.start_polling()
updater.idle()
