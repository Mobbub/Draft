import requests, telebot, pickle, re, datetime
from telebot import types
from geopy.geocoders import Nominatim
from telebot.handler_backends import BaseMiddleware
from telebot.handler_backends import CancelUpdate

bot = telebot.TeleBot('token_bot', use_class_middlewares = True)
deys = ''

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
            bot.send_message(message.chat.id, 'Вы превысили скорость в отправке сообщений!🛑\n🚫Бот не будет реагировать на такую скорость🚫')
            return CancelUpdate()
        self.last_time[message.from_user.id] = message.date

    def post_process(self, message, data, exception):
        pass

bot.setup_middleware(SimpleMiddleware(0.01))

def main(person_info: dict, request_subject: dict) -> str:
    ai_role = ''
    if request_subject['deys'] == 'биография':
        ai_role = 'биограф'
    elif request_subject['deys'] == 'эпитафия':
        ai_role = 'писатель эпитафий'
    prompt = {
        'modelUri': 'gpt://token_catalog/yandexgpt-lite',
        'completionOptions': {
            'stream': False,
            'temperature': 1,
            'maxTokens': '2000'
        },
        'messages': [
            {
                'role': 'system',
                'text': f'Ты {ai_role}, который составляет {request_subject["deys"]} о человеке.'
            },
            {
                'role': 'user',
                'text': f'Привет! Я бы хотел, чтобы ты составил {request_subject["deys"]} о человеке, сможешь сделать?'
            },
            {
                'role': 'assistant',
                'text': 'Привет! Хорошо, расскажи мне что-нибудь о нём.'
            },
            {
                'role': 'user',
                'text': f'Этого человека зовут {person_info["fio"]}, он родился {person_info["dr"]} в {person_info["mr"]} и умер {person_info["ds"]} в {person_info["ms"]}. Его супругом(супругой) был(была) {person_info["supr"]}. Этот человек окончил {person_info["obr"]}. Его родом деятельности было {person_info["rd"]}. Его гражданство - {person_info["graj"]}. Из детей у него(неё) были {person_info["deti"]}, а из внуков - {person_info["vnuki"]}. Его достижения - {person_info["dost"]}'
            }
        ]
    }
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Api-Key token_key_gpt'
    }
    response = requests.post(url, headers=headers, json=prompt)
    start_point = '\\\\n\\\\n'
    end_point = '"},"status"'
    result = re.search(f'{start_point}(.*?){end_point}', response.text)
    if result: 
        return result.group(1).replace('\\n', '\n')
    else:
        return ''

def load_session():
    try:
        with open('session.pickle', 'rb') as f:
            session = pickle.load(f)
    except FileNotFoundError:
        session = {}
    return session

def save_session(session):
    with open('session.pickle', 'wb') as f:
        pickle.dump(session, f)

session = load_session()

def prov(mes, vopr, chat_id):
    if vopr == 'ФИО':
         if len(mes.split()) == 3:
             return True
         return False
    elif vopr == 'ДР' or vopr == 'ДС':
        try:
            date = datetime.datetime.strptime(mes, "%d.%m.%Y").date()
            if vopr == 'ДР':
                if date <= date.today():
                    return True
                return False
            elif vopr == 'ДС':
                if date >= datetime.datetime.strptime(session[chat_id]['dr'], "%d.%m.%Y").date() and date <= date.today():
                    return True
                return False
        except ValueError:
            return False
    elif vopr == 'МР' or vopr == 'МС' or vopr == 'ГРАЖ':
            geolocator = Nominatim(user_agent = "my_application")
            location = geolocator.geocode(mes)
            if location is not None:
                return True
            return False
    elif vopr == 'Дети' or vopr == 'Внуки' or vopr == 'Супруг':
        mes_nov = ''
        schet = 1
        for i in range(len(mes)):
            if mes[i] != ',':
                mes_nov += mes[i]
            else:
                schet += 1
        if (len(mes_nov.split()) % 3 == 0) and (len(mes_nov.split()) / 3 == schet):
            return True
        return False
    else:
        if len(mes) >= 3:
            return True
        return False

def mass_for_main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys):
    massiv_otv = {
        'fio': fio,
        'dr': dr,
        'ds': ds,
        'mr': mr,
        'ms': ms,
        'supr': supr,
        'obr': obr,
        'rd': rd,
        'graj': graj,
        'deti': deti,
        'vnuki': vnuki,
        'dost': dost,
    }
    massiv_deys = {
        'deys': deys
    }
    for key, value in massiv_otv.items():
        if value == 'Следующий вопрос▶️':
            massiv_otv[key] = 'Не указано'
    return main(massiv_otv, massiv_deys)

@bot.message_handler(commands = ['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton(text = 'Эпитафия')
    btn2 = types.KeyboardButton(text = 'Биография')
    kb.add(btn1)
    kb.add(btn2)
    chat_id = message.chat.id
    if chat_id not in session:
        session[chat_id] = {'flag1': False, 'flag2': False, 'flag3': False, 'flag4': False, 'flag5': False, 'flag6': False, 'flag7': False, 'flag8': False, 'flag9': False, 'flag10': False, 'flag11': False, 'flag12': False, 'fio': '', 'dr': '', 'ds': '', 'mr': '', 'ms': '', 'supr': '', 'obr': '', 'rd': '', 'graj': '', 'deti': '', 'vnuki': '', 'dost': '', 'deys': ''}
        save_session(session)
    bot.send_message(message.chat.id, 'Приветствую!👋 \nЯ буду задавать вам простые и однострочные вопросы, на которые вы должны будете отвечать, для составления биографии или эпитафии для человека, о котором вы хотите оставить память.\nЕсли у вас по какой-то причине нет ответа на вопрос, то нажмите на кнопку "Следующий вопрос 🔼".\nЕсли вы хотите получить больше информации о боте, то используйте команду /info')
    bot.send_message(message.chat.id, 'Что вас интересует?\nВыбери нужное вам действие под этим сообщением ⬇️', reply_markup=kb)

@bot.message_handler(commands = ['info'])
def info_sys(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn3 = types.KeyboardButton(text = '/start')
    kb.add(btn3)
    bot.send_message(message.chat.id, 'Что и как?\nДанный telegram бот создан для того, чтоб облегчить заполнение страницы об умершем человеке, а именно, он за вас напишет биографию или эпитафию по информации, которую вы дадите.\n<b><i>Маленькая подсказка: если на вопрос у вас есть несколько ответов, то просто перечислите их через запятую.</i></b>\n\nНавигация по командам:\n/start - начальная команда запуска бота.\n/info - информация об этом telegram боте.\n\nНавигация по кнопкам:\n├<b><i>Эпитафия</i></b> - бот начнёт запрашивать у вас информацию об человеке, для составления эпитафии.\n├<b><i>Биография</i></b> - бот начнёт запрашивать у вас информацию об человеке, для составления эпитафии.\n├<b><i>Следующий вопрос</i></b> 🔼 - если у вас нет ответа на вопрос, то нажмите эту кнопку, бот так и посчитает, что нет информации.\n├<b><i>Прошлый вопрос</i></b> 🔽 - если вы ошибочно ответили на прошлый вопрос или решили поменять ответ, то эта кнопка позволяет вернуться на одну стадию назад и ввести новый ответ.\n├<b><i>Начать заново</i></b> ↩️ - эта кнопка позволяет вернуться в самое начало и заново начать использовать этого бота.\n├<b><i>Другая биография/эпитафия</i></b> 🔄 - эта копка позволяет заменять биографию/эпитафию об этом же человеке, при том условии, если она вам не понравилась.\n\nХорошего использования!', reply_markup = kb, parse_mode = "HTML")

@bot.message_handler(func = lambda message: message.text == 'Эпитафия')
def epitafia(message):
    global deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn4 = types.KeyboardButton(text = 'Начать заново↩️')
    kb.add(btn4)
    chat_id = message.chat.id
    deys = (message.text).lower()
    session[chat_id]['deys'] = message.text
    session[chat_id]['flag1'] = True
    bot.send_message(message.chat.id, 'Введите <b><i>ФИО</i></b> 👤\nНапример: <i><code>Иванов Иван Иванович</code></i>', reply_markup = kb, parse_mode = "HTML")
    save_session(session)

@bot.message_handler(func = lambda message: message.text == 'Биография')
def biografia(message):
    global deys
    chat_id = message.chat.id
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn5 = types.KeyboardButton(text = 'Начать заново↩️')
    kb.add(btn5)
    deys = message.text.lower()
    session[chat_id]['deys'] = message.text
    session[chat_id]['flag1'] = True
    bot.send_message(message.chat.id, 'Введите <b><i>ФИО</i></b> 👤\nНапример: <i><code>Иванов Иван Иванович</code></i>', reply_markup=kb, parse_mode = "HTML")
    save_session(session)

@bot.message_handler(func = lambda message: message.text == f'Другая {deys}🔄')
def noviy(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn6 = types.KeyboardButton(text = f'Другая {deys}🔄')
    btn7 = types.KeyboardButton(text = 'Начать заново↩️')
    kb.add(btn6)
    kb.add(btn7)
    chat_id = message.chat.id
    bot.send_message(message.chat.id, f'''Вот {session[chat_id]['deys']}, которая у нас получилась:
{mass_for_main(session[chat_id]['fio'], session[chat_id]['dr'], session[chat_id]['ds'], session[chat_id]['mr'], session[chat_id]['ms'], session[chat_id]['supr'], session[chat_id]['obr'], session[chat_id]['rd'], session[chat_id]['graj'], session[chat_id]['deti'], session[chat_id]['vnuki'], session[chat_id]['dost'], session[chat_id]['deys'])}''', reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == 'Начать заново↩️')
def zanovo(message):
    global deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn8 = types.KeyboardButton(text = 'Эпитафия')
    btn9 = types.KeyboardButton(text = 'Биография')
    kb.add(btn8)
    kb.add(btn9)
    chat_id = message.chat.id
    session[chat_id] = {'flag1': False, 'flag2': False, 'flag3': False, 'flag4': False, 'flag5': False, 'flag6': False, 'flag7': False, 'flag8': False, 'flag9': False, 'flag10': False, 'flag11': False, 'flag12': False, 'fio': '', 'dr': '', 'ds': '', 'mr': '', 'ms': '', 'supr': '', 'obr': '', 'rd': '', 'graj': '', 'deti': '', 'vnuki': '', 'dost': '',}
    deys = ''
    save_session(session)
    bot.send_message(message.chat.id, 'Хорошо! Что вас интересует?\nВыбери нужное вам действие под этим сообщением ⬇️', reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == '◀️Прошлый вопрос')
def prosh_vopr(message):
    chat_id = message.chat.id
    if session[chat_id]['flag2']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn10 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn10)
        session[chat_id]['flag1'] = True
        bot.send_message(message.chat.id, 'Введите <b><i>ФИО</i></b> 👤\nНапример: <i><code>Иванов Иван Иванович</code></i>', reply_markup = kb, parse_mode = "HTML")
    elif session[chat_id]['flag3']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn11 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn12 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn11)
        kb.add(btn12)
        session[chat_id]['flag2'] = True
        bot.send_message(message.chat.id, 'Введите <b><i>дату рождения</i></b> 👶\nНапример: <code>30.12.2000</code>', reply_markup = kb, parse_mode = "HTML")
    elif session[chat_id]['flag4']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn13 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn14 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn13)
        kb.add(btn14)
        session[chat_id]['flag3'] = True
        bot.send_message(message.chat.id, 'Введите <b><i>дату смерти</i></b> 💀\nНапример: <code>30.12.2000</code>', reply_markup = kb, parse_mode = "HTML")
    elif session[chat_id]['flag5']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn15 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn16 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn17 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn16, btn15)
        kb.add(btn17)
        session[chat_id]['flag4'] = True
        bot.send_message(message.chat.id, 'Введите <b><i>место рождения</i></b> 🇷🇺\nНапример: <code>Россия, Москва</code>', reply_markup = kb, parse_mode = "HTML")
    elif session[chat_id]['flag6']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn18 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn19 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn20 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn19, btn18)
        kb.add(btn20)
        session[chat_id]['flag5'] = True
        bot.send_message(message.chat.id, 'Введите <b><i>место смерти</i></b> 🪦\nНапример: <code>Россия, Москва</code>', reply_markup = kb, parse_mode = "HTML")
    elif session[chat_id]['flag7']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn21 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn22 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn23 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn22, btn21)
        kb.add(btn23)
        session[chat_id]['flag6'] = True
        bot.send_message(message.chat.id, 'Введите <b><i>ФИО супруга(ги)</i></b> 👫\nНапример: <code>Иванов Иван Иванович</code>', reply_markup = kb, parse_mode = "HTML")
    elif session[chat_id]['flag8']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn24 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn25 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn26 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn25, btn24)
        kb.add(btn26)
        session[chat_id]['flag7'] = True
        bot.send_message(message.chat.id, 'Укажите <b><i>образование (учебное заведение), которое есть у человека</i></b> 🎓\nНапример: <code>КФУ им. Вернадского, информатика и вычислительная техника</code>', reply_markup = kb, parse_mode = "HTML")
    elif session[chat_id]['flag9']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn27 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn28 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn29 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn28, btn27)
        kb.add(btn29)
        session[chat_id]['flag8'] = True
        bot.send_message(message.chat.id, 'Укажите <b><i>род деятельности человека</i></b> 👨🏻‍🔧\nНапример: <code>Учёный-математик</code>', reply_markup = kb, parse_mode = "HTML")
    elif session[chat_id]['flag10']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn30 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn31 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn32 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn31, btn30)
        kb.add(btn32)
        session[chat_id]['flag9'] = True
        bot.send_message(message.chat.id, 'Укажите <b><i>гражданство человека</i></b> 👳🏽‍♀️\nНапример: <code>Россия Федерация</code>', reply_markup = kb, parse_mode="HTML")
    elif session[chat_id]['flag11']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn33 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn34 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn35 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn34, btn33)
        kb.add(btn35)
        session[chat_id]['flag10'] = True
        bot.send_message(message.chat.id, 'Укажите <b><i>ФИО детей</i></b> 👨‍👩‍👧‍👦\nНапример: <code>Иванов Иван Иванович</code>', reply_markup = kb, parse_mode="HTML")
    elif session[chat_id]['flag12']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn36 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn37 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn38 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn37, btn36)
        kb.add(btn38)
        session[chat_id]['flag11'] = True
        bot.send_message(message.chat.id, 'Укажите <b><i>ФИО внуков</i></b> 👨‍👧‍👦\nНапример: <code>Иванов Иван Иванович</code>', reply_markup = kb, parse_mode="HTML")

@bot.message_handler(func = lambda message: True)
def info(message):
    chat_id = message.chat.id
    if session[chat_id]['flag1']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn39 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn40 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn39)
        kb.add(btn40)
        if prov(message.text, 'ФИО', chat_id):
            session[chat_id]['fio'] = message.text
            session[chat_id]['flag2'] = True
            message.text = ''
            session[chat_id]['flag1'] = False
            bot.send_message(message.chat.id, 'Введите <b><i>дату рождения</i></b> 👶\nНапример: <code>30.12.2000</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите ФИО ещё раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Иванов Иван Иванович</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag2']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn41 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn42 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn41)
        kb.add(btn42)
        if prov(message.text, 'ДР', chat_id):
            session[chat_id]['dr'] = message.text
            session[chat_id]['flag3'] = True
            message.text = ''
            session[chat_id]['flag2'] = False
            bot.send_message(message.chat.id, 'Введите <b><i>дату смерти</i></b> 💀\nНапример: <code>30.12.2000</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите дату рождения ещё раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>30.12.2000</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag3']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn43 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn44 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn45 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn44, btn43)
        kb.add(btn45)
        if prov(message.text, 'ДС', chat_id):
            session[chat_id]['ds'] = message.text
            session[chat_id]['flag4'] = True
            message.text = ''
            session[chat_id]['flag3'] = False
            bot.send_message(message.chat.id, 'Введите <b><i>место рождения</i></b> 🇷🇺\nНапример: <code>Россия, Москва</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите дату смерти ещё раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>30.12.2000</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag4']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn46 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn47 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn48 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn47, btn46)
        kb.add(btn48)
        if prov(message.text, 'МР', chat_id) or message.text == 'Следующий вопрос▶️':
            session[chat_id]['mr'] = message.text
            session[chat_id]['flag5'] = True
            message.text = ''
            session[chat_id]['flag4'] = False
            bot.send_message(message.chat.id, 'Введите <b><i>место смерти</i></b> 🪦\nНапример: <code>Россия, Москва</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите место рождения ещё раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Россия, Москва</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag5']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn49 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn50 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn51 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn50, btn49)
        kb.add(btn51)
        if prov(message.text, 'МС', chat_id) or message.text == 'Следующий вопрос▶️':
            session[chat_id]['ms'] = message.text
            session[chat_id]['flag6'] = True
            message.text = ''
            session[chat_id]['flag5'] = False
            bot.send_message(message.chat.id, 'Введите <b><i>ФИО супруга(ги)</i></b> 👫\nНапример: <code>Иванов Иван Иванович</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите место смерти ещё раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Россия, Москва</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag6']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn52 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn53 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn54 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn53, btn52)
        kb.add(btn54)
        if prov(message.text, 'Супруг', chat_id) or message.text == 'Следующий вопрос▶️':
            session[chat_id]['supr'] = message.text
            session[chat_id]['flag7'] = True
            message.text = ''
            session[chat_id]['flag6'] = False
            bot.send_message(message.chat.id, 'Укажите <b><i>образование (учебное заведение), которое есть у человека</i></b> 🎓\nНапример: <code>КФУ им. Вернадского, информатика и вычислительная техника</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите ФИО супруга(ги) ещё раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Иванов Иван Иванович</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag7']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn55 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn56 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn57 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn56, btn55)
        kb.add(btn57)
        if prov(message.text, 'обр', chat_id) or message.text == 'Следующий вопрос▶️':
            session[chat_id]['obr'] = message.text
            session[chat_id]['flag8'] = True
            message.text = ''
            session[chat_id]['flag7'] = False
            bot.send_message(message.chat.id, 'Укажите <b><i>род деятельности человека</i></b> 👨🏻‍🔧\nНапример: <code>Учёный-математик</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите образование (учебное заведение), которое есть у человека ещё раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>КФУ им. Вернадского, информатика и вычислительная техника</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag8']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn58 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn59 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn60 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn59, btn58)
        kb.add(btn60)
        if prov(message.text, 'РД', chat_id) or message.text == 'Следующий вопрос▶️':
            session[chat_id]['rd'] = message.text
            session[chat_id]['flag9'] = True
            message.text = ''
            session[chat_id]['flag8'] = False
            bot.send_message(message.chat.id, 'Укажите <b><i>гражданство человека</i></b> 👳🏽‍♀️\nНапример: <code>Российская Федерация</code>', reply_markup=kb, parse_mode="HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите род деятельности человека еще раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Учёный-математик</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag9']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn61 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn62 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn63 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn62, btn61)
        kb.add(btn63)
        if prov(message.text, 'ГРАЖ', chat_id) or message.text == 'Следующий вопрос▶️':
            session[chat_id]['graj'] = message.text
            session[chat_id]['flag10'] = True
            message.text = ''
            session[chat_id]['flag9'] = False
            bot.send_message(message.chat.id, 'Укажите <b><i>ФИО детей</i></b> 👨‍👩‍👧‍👦\nНапример: <code>Иванов Иван Иванович</code>', reply_markup=kb, parse_mode="HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите гражданство человека еще раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Российская Федерация</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag10']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn64 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn65 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn66 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn65, btn64)
        kb.add(btn66)
        if prov(message.text, 'Дети', chat_id) or message.text == 'Следующий вопрос▶️':
            session[chat_id]['deti'] = message.text
            session[chat_id]['flag11'] = True
            message.text = ''
            session[chat_id]['flag10'] = False
            bot.send_message(message.chat.id, 'Укажите <b><i>ФИО внуков</i></b> 👨‍👧‍👦\nНапример: <code>Иванов Иван Иванович</code>', reply_markup=kb, parse_mode="HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите ФИО детей еще раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Иванов Иван Иванович</code>', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag11']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn67 = types.KeyboardButton(text = 'Следующий вопрос▶️')
        btn68 = types.KeyboardButton(text = '◀️Прошлый вопрос')
        btn69 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn68, btn67)
        kb.add(btn69)
        if prov(message.text, 'Внуки', chat_id) or message.text == 'Следующий вопрос▶️':
            session[chat_id]['vnuki'] = message.text
            session[chat_id]['flag12'] = True
            message.text = ''
            session[chat_id]['flag11'] = False
            bot.send_message(message.chat.id, 'Введите <b><i>награды, премии или достижения, которые есть у человека</i></b> 🏅\nНапример: <code>Знак Почета 1954</code>', reply_markup=kb, parse_mode="HTML")
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите ФИО внуков еще раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Иванов Иван Иванович</code>''', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    elif session[chat_id]['flag12']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn70 = types.KeyboardButton(text = f'Другая {deys}🔄')
        btn71 = types.KeyboardButton(text = 'Начать заново↩️')
        kb.add(btn70)
        kb.add(btn71)
        if prov(message.text, 'дост', chat_id):
            session[chat_id]['dost'] = message.text
            session[chat_id]['flag12'] = False
            bot.send_message(message.chat.id, f'''Вот {session[chat_id]['deys'].lower()}, которая у нас получилась:\n{mass_for_main(session[chat_id]['fio'], session[chat_id]['dr'], session[chat_id]['ds'], session[chat_id]['mr'], session[chat_id]['ms'], session[chat_id]['supr'], session[chat_id]['obr'], session[chat_id]['rd'], session[chat_id]['graj'], session[chat_id]['deti'], session[chat_id]['vnuki'], session[chat_id]['dost'], session[chat_id]['deys'])}''', reply_markup=kb)
            save_session(session)
        else:
            bot.send_message(message.chat.id, 'Что то пошло не так... 😵‍💫\n<i>Введите награды, премии или достижения, которые есть у человека, еще раз, проверьте правильность и логику написанного.</i> ✅\nНапример: <code>Знак Почета 1954</code>''', reply_markup=kb, parse_mode = "HTML")
            save_session(session)
    else:
        kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn72 = types.KeyboardButton(text = 'Эпитафия')
        btn73 = types.KeyboardButton(text = 'Биография')
        kb.add(btn72)
        kb.add(btn73)
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю... 😔')
        bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=kb)
        save_session(session)

bot.polling()
