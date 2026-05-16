import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8600847860:AAH_hRNU3muXYH9Dl0vXzj_E2TBhsYeJNNs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚚 Welcome to Global Transit Logistics\n\n"
        "Commands:\n"
        "/track - Track shipment\n"
        "/status - Delivery status\n"
        "/services - Our services\n"
        "/support - Customer support"
    )

async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 Please send your tracking number.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚚 Your shipment is currently in transit.")

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Services:\n"
        "- International Shipping\n"
        "- Cargo Handling\n"
        "- Express Delivery"
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Contact support: @YourUsername")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("track", track))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("services", services))
    app.add_handler(CommandHandler("support", support))

    await app.run_polling()

nest_asyncio.apply()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
