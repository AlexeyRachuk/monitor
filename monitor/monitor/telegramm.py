import telepot

token = '2122815268:AAERhoA2pXtSzVUkXPxmtlC7oEeJOWJWK5U'
my_id = 2122815268
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(2122815268, text, parse_mode="Markdown")
