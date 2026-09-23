import telebot
from telebot import types
import qrcode

bot = telebot.TeleBot("Token")

@bot.message_handler(func=lambda message: True)
def qr(message):
    try:
        text = message.text
        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make(fit=True)
        image = qr.make_image(fill="black", back_color="white")
        img = "qr_code.png"
        image.save(img)

        tt = bot.get_me().username
        ff = "@DuDrD - @SeyedAliShakeriii"
        caption = f"تم صنع بواسطة  @{tt} - {ff}"
        with open(img, "rb") as qr_image:
            bot.send_photo(message.chat.id, qr_image, caption=caption)
    except Exception as e:
        bot.reply_to(message, "دز فقط رسالة .")

bot.polling()