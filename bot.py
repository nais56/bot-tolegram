# bot/bot.py
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
import config
import database
from scraper import extract_discounted_link, extract_cart_discounted_link
import utils

# تعريف حالات المحادثة
GET_PRODUCT_URL = 0

# بداية الدالة الرئيسية لبوت التسويق بالعمولة
def main():
    # تكوين المحادثة والمعالجات والتفاعل مع المستخدمين
    updater = Updater(token=config.bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.text & ~Filters.command, get_product_url)],
        states={
            GET_PRODUCT_URL: [MessageHandler(Filters.text & ~Filters.command, get_discounted_link)],
        },
        fallbacks=[],
    ))

    # تشغيل البوت
    updater.start_polling()
    updater.idle()

# دالة بداية المحادثة
def start(update: Update, context: CallbackContext):
    update.message.reply_text("مرحبًا! قم بإرسال رابط منتج AliExpress للحصول على رابط بتخفيض.")

# دالة للحصول على الرابط المخفض
def get_discounted_link(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_message = update.message.text

    # استدعاء وحدة scraper للحصول على الرابط المخفض
    if config.cart_discount_enabled:
        discounted_link = extract_cart_discounted_link(user_message)
    else:
        discounted_link = extract_discounted_link(user_message)

    # ثم أضف البيانات إلى قاعدة البيانات
    database.insert_product(user_id, user_message, discounted_link)

    response_message = f"رابط المنتج بتخفيض: {discounted_link}"
    update.message.reply_text(response_message)

# دالة رئيسية لتنفيذ البوت
if __name__ == '__main__':
    main()
