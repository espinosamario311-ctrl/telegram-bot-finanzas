import os
import telebot
import requests

# Obtenemos el token que le vamos a pasar desde Render
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola! 👋 Soy tu bot de inversiones. Escribí /hoy para ver información del mercado.")

@bot.message_handler(commands=['hoy'])
def send_today(message):
    try:
        data = requests.get("https://api.acuantoesta.com.ar/json/dolar").json()
        blue = data['dolar']['blue']['venta']
        oficial = data['dolar']['oficial']['venta']
        respuesta = f"💵 Dólar hoy:\n- Oficial: ${oficial}\n- Blue: ${blue}\n\nPronto también vas a ver bonos, letras y acciones."
    except Exception as e:
        respuesta = f"No pude obtener los datos ahora 😕\nError: {e}"
    bot.reply_to(message, respuesta)

print("🤖 Bot iniciado correctamente...")
bot.polling()
