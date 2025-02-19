import telebot
from telebot.handler_backends import BaseMiddleware, CancelUpdate

bot = telebot.TeleBot('token', use_class_middlewares = True)

class SimpleMiddleware(BaseMiddleware):
    def __init__(self, limit) -> None:
        self.last_time = {}
        self.limit = limit
        self.update_types = ['message']

    def pre_process(self, message, data):
        if not message.from_user.id in self.last_time:
            self.last_time[message.from_user.id] = message.date
            return
        if message.date - self.last_time[message.from_user.id] < self.limit:
            bot.send_message(message.chat.id, 'поддержи емае\nhttps://www.donationalerts.com/r/provodaaaaaa')
            return CancelUpdate()
        self.last_time[message.from_user.id] = message.date

    def post_process(self, message, data, exception):
        pass

bot.setup_middleware(SimpleMiddleware(0.01))

@bot.message_handler(commands = ['start'])
def start(message):
    if message.chat.type in ['group', 'supergroup']:
        bot.send_message(message.chat.id, 'поддержи емае\nhttps://www.donationalerts.com/r/provodaaaaaa')
    
@bot.message_handler(commands = ['csfd'])
def csfd(message):
    if message.chat.type in ['group', 'supergroup']:
        bot.send_message(message.chat.id, 'Расписание на сегодня')
        
@bot.message_handler(commands = ['csfm'])
def csfm(message):
    if message.chat.type in ['group', 'supergroup']:
        bot.send_message(message.chat.id, 'Расписание на завтра')
        
bot.polling()