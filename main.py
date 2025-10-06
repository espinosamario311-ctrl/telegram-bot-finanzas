import os
import telebot
import requests

# Token del bot
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Mensaje de bienvenida
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola! 👋 Soy tu bot de inversiones. Escribí /hoy para ver datos de hoy.")

# Comando /hoy: dólar, bonos, acciones y letras
@bot.message_handler(commands=['hoy'])
def send_today(message):
    respuesta = "📊 Datos de hoy:\n\n"

    # 1️⃣ Dólar
    try:
        resp = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=ARS", timeout=5)
        data = resp.json()
        if "rates" in data and "ARS" in data["rates"]:
            oficial = data["rates"]["ARS"]
            blue = round(oficial * 1.50, 2)
            respuesta += f"💵 Dólar:\n- Oficial: ${oficial:.2f}\n- Blue (estimado): ${blue}\n\n"
        else:
            respuesta += "💵 Dólar: No disponible 😕\n\n"
    except Exception as e:
        respuesta += f"💵 Dólar: Error al obtener datos 😕\n"

    # 2️⃣ Bonos (simulados)
    try:
        bonos = {
            "Bonar 2030": "100,50%",
            "AL30": "98,75%",
            "GD30": "102,30%"
        }
        respuesta += "📈 Bonos:\n"
        for nombre, valor in bonos.items():
            respuesta += f"- {nombre}: {valor}\n"
        respuesta += "\n"
    except:
        respuesta += "📈 Bonos: No disponibles 😕\n\n"

    # 3️⃣ Acciones (simuladas)
    try:
        acciones = {
            "GGAL": "$1500",
            "YPF": "$700",
            "BMA": "$1200"
        }
        respuesta += "🏦 Acciones:\n"
        for nombre, precio in acciones.items():
            respuesta += f"- {nombre}: {precio}\n"
        respuesta += "\n"
    except:
        respuesta += "🏦 Acciones: No disponibles 😕\n\n"

    # 4️⃣ Letras del Tesoro (simuladas)
    try:
        letras = {
            "S31G5": "Valor nominal: $1.200.000, Tasa: 1,46%",
            "S15G5": "Valor nominal: $1.030.509, Tasa: 1,4679%"
        }
        respuesta += "💰 Letras:\n"
        for nombre, info in letras.items():
            respuesta += f"- {nombre}: {info}\n"
    except:
        respuesta += "💰 Letras: No disponibles 😕\n"

    bot.reply_to(message, respuesta)

print("🤖 Bot iniciado correctamente...")
bot.polling()

