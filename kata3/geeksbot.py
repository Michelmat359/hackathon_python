from telegram.ext import Updater, CommandHandler

def main():
    #iniciamos el updater/instanciamos
    updater = Updater(token=open("./bot_token").read(), use_context=True)

    #dentro del updater tiene un dispatcher que reparte el trabajo entre los manejadores
    #se añade un nuevo manejador para indicarle qué hacer con START
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #se añade manejador para el comando REPITE
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #añadir comando suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #Se pone en escucha. Pide notificaciones a Telegram
    updater.start_polling()
    #Acaba las tareas si esta procesandose cuando cerramos todo. Poner Siempre capturamos señales de parada
    updater.idle()

#definimos la función start con parámetros el update y el contexto
def start(update, context):
    #responder 
    update.message.reply_text("Hola, soy un bot")

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    #args = [2, 2]
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es "+ str(resultado))

main()