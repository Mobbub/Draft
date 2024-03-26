import requests
import telebot
from telebot import types

bot = telebot.TeleBot('6952931811:AAGaxnDxuIeDmcfB460Ce6JVlvMXJ2En278')
flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False
flag7 = False
flag8 = False
flag9 = False
flag10 = False
flag11 = False
flag12 = False
fio = ''
dr = ''
ds = ''
mr = ''
ms = ''
supr = ''
obr = ''
rd = ''
graj = ''
deti = ''
vnuki = ''
dost = ''
deys = ''

def main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys):
    pass

@bot.message_handler(commands = ['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Эпитафия')
    btn2 = types.KeyboardButton(text = 'Биография')
    kb.add(btn1)
    kb.add(btn2)
    bot.send_message(message.chat.id, 'Здрасьте. Выберете действие', reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == 'Эпитафия')
def start(message):
    global flag1, deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Следующий вопрос')
    btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
    btn3 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn2, btn3)
    kb.add(btn1)
    flag1 = True
    deys = 'Эпитафия'
    bot.send_message(message.chat.id, '''Введите ФИО.
Например: Иванов Иван Иванович''', reply_markup=kb)
    
@bot.message_handler(func = lambda message: message.text == 'Биография')
def start(message):
    global flag1, deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Следующий вопрос')
    btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
    btn3 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn2, btn3)
    kb.add(btn1)
    flag1 = True
    deys = 'Биография'
    bot.send_message(message.chat.id, '''Введите ФИО.
Например: Иванов Иван Иванович''', reply_markup=kb)
    
@bot.message_handler(func = lambda message: message.text == f'Другой {deys}')
def start(message):
    global flag1, fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = f'Другой {deys}')
    btn2 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn1)
    kb.add(btn2)
    bot.send_message(message.chat.id, '''Вот {deys}
{main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys)}''', reply_markup=kb)
    
@bot.message_handler(func = lambda message: message.text == 'Начать заново')
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Эпитафия')
    btn2 = types.KeyboardButton(text = 'Биография')
    kb.add(btn1)
    kb.add(btn2)
    bot.send_message(message.chat.id, 'Выберете действие', reply_markup=kb)

@bot.message_handler(func = lambda message: True)
def info(message):
    global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12, fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys
    if flag1:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn2, btn3)
        kb.add(btn1)
        fio = message.text
        flag2 = True
        message.text = ''
        flag1 = False
        bot.send_message(message.chat.id, '''Введите дату рождения. 
Например: 01.01.2000''', reply_markup=kb)
    elif flag2 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        dr = message.text
        flag3 = True
        message.text = ''
        flag2 = False
        bot.send_message(message.chat.id, '''Введите дату смерти. 
Например: 01.01.2000''', reply_markup=kb)
    elif flag3 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        ds = message.text
        flag4 = True
        message.text = ''
        flag3 = False
        bot.send_message(message.chat.id, '''Введите место рождения. 
Например: Россия''', reply_markup=kb)
    elif flag4 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        mr = message.text
        flag5 = True
        message.text = ''
        flag4 = False
        bot.send_message(message.chat.id, '''Введите место смерти.
Например: Россия''', reply_markup=kb)
    elif flag5 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        ms = message.text
        flag6 = True
        message.text = ''
        flag5 = False
        bot.send_message(message.chat.id, '''Введите ФИО супруга(ги).
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif flag6 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        supr = message.text
        flag7 = True
        message.text = ''
        flag6 = False
        bot.send_message(message.chat.id, '''Укажите учебное заведение, которое закончил этот человек.
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''', reply_markup=kb)
    elif flag7 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        obr = message.text
        flag8 = True
        message.text = ''
        flag7 = False
        bot.send_message(message.chat.id, '''Укажите род деятельности человека.
Например: Учёный математик''', reply_markup=kb)
    elif flag8 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        rd = message.text
        flag9 = True
        message.text = ''
        flag8 = False
        bot.send_message(message.chat.id, '''Укажите гражданство человека.
Например: Россия''', reply_markup=kb)
    elif flag9 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        graj = message.text
        flag10 = True
        message.text = ''
        flag9 = False
        bot.send_message(message.chat.id, '''Укажите ФИО детей.
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif flag10 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        deti = message.text
        flag11 = True
        message.text = ''
        flag10 = False
        bot.send_message(message.chat.id, '''Укажите ФИО внуков:
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif flag11 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        vnuki = message.text
        flag12 = True
        message.text = ''
        flag11 = False
        bot.send_message(message.chat.id, '''Укажите награды, премии или достижения, которые есть у человека.
Например: Знак Почета 1954, 1981''', reply_markup=kb)
    elif flag12 == True:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = f'Другой {deys}')
        btn2 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1)
        kb.add(btn2)
        dost = message.text
        flag12 = False
        bot.send_message(message.chat.id, f'''Вот {deys}:
{main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys)}''', reply_markup=kb)
    else:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Эпитафия')
        btn2 = types.KeyboardButton(text = 'Биография')
        kb.add(btn1)
        kb.add(btn2)
        bot.send_message(message.chat.id, 'моя твоя не понимать')
        bot.send_message(message.chat.id, 'Выберете действие', reply_markup=kb)

bot.polling()
