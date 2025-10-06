import os
import telebot
import requests

# Obtenemos el token del bot desde la variable de entorno
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola! 👋 Soy tu bot de inversiones. Escribí /hoy para ver el dólar de hoy.")

@bot.message_handler(commands=['hoy'])
def send_today(message):
    try:
        # API confiable para el dólar oficial
        oficial = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=ARS").json()["rates"]["ARS"]
        
        # Para simular dólar blue, agregamos un margen
        blue = round(oficial * 1.50, 2)

        respuesta = f"💵 Dólar hoy:\n- Oficial: ${oficial:.2f}\n- Blue (estimado): ${blue}\n\nPronto agregaremos bonos y letras."
    except Exception as e:
        respuesta = f"No pude obtener los datos ahora 😕\nError: {e}"

    bot.reply_to(message, respuesta)

print("🤖 Bot iniciado correctamente...")
bot.polling()
