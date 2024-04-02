import requests
import telebot
from telebot import types

bot = telebot.TeleBot('token')
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
fl1 = False
fl2 = False
fl3 = False
fl4 = False
fl5 = False
fl6 = False
fl7 = False
fl8 = False
fl9 = False
fl10 = False
fl11 = False

def main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys):
    pass

def prov(mes, vopr):
    return True

def prosh_vop(flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12):
    global fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11
    fl1 = False
    fl2 = False
    fl3 = False
    fl4 = False
    fl5 = False
    fl6 = False
    fl7 = False
    fl8 = False
    fl9 = False
    fl10 = False
    fl11 = False
    if flag2:
        fl1 = True
        return '''Введите ФИО.
Например: Иванов Иван Иванович'''
    elif flag3:
        fl2 = True
        return '''Введите дату рождения. 
Например: 01.01.2000'''
    elif flag4:
        fl3 = True
        return '''Введите дату смерти. 
Например: 01.01.2000'''
    elif flag5:
        fl4 = True
        return '''Введите место рождения. 
Например: Россия'''
    elif flag6:
        fl5 = True
        return '''Введите место смерти.
Например: Россия'''
    elif flag7:
        fl6 = True
        return '''Введите ФИО супруга(ги).
Например: Иванов Иван Иванович'''
    elif flag8:
        fl7 = True
        return '''Укажите учебное заведение, которое закончил этот человек.
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского'''
    elif flag9:
        fl8 = True
        return '''Укажите род деятельности человека.
Например: Учёный математик'''
    elif flag10:
        fl9 = True
        return '''Укажите гражданство человека.
Например: Россия'''
    elif flag11:
        fl10 = True
        return '''Укажите ФИО детей.
Например: Иванов Иван Иванович'''
    elif flag12:
        fl11 = True
        return '''Укажите ФИО внуков:
Например: Иванов Иван Иванович'''
    else:
        return 'иди нахуй'
    
@bot.message_handler(commands = ['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Эпитафия')
    btn2 = types.KeyboardButton(text = 'Биография')
    kb.add(btn1)
    kb.add(btn2)
    bot.send_message(message.chat.id, 'Здрасьте. Выберете действие', reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == 'Эпитафия')
def epitafia(message):
    global flag1, deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Следующий вопрос')
    btn2 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn1)
    kb.add(btn2)
    flag1 = True
    deys = 'Эпитафия'
    bot.send_message(message.chat.id, '''Введите ФИО.
Например: Иванов Иван Иванович''', reply_markup=kb)
    
@bot.message_handler(func = lambda message: message.text == 'Биография')
def biografia(message):
    global flag1, deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Следующий вопрос')
    btn2 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn1)
    kb.add(btn2)
    flag1 = True
    deys = 'Биография'
    bot.send_message(message.chat.id, '''Введите ФИО.
Например: Иванов Иван Иванович''', reply_markup=kb)
    
@bot.message_handler(func = lambda message: message.text == f'Другой {deys}')
def noviy(message):
    global fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = f'Другой {deys}')
    btn2 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn1)
    kb.add(btn2)
    bot.send_message(message.chat.id, '''Вот {deys}
{main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys)}''', reply_markup=kb)
    
@bot.message_handler(func = lambda message: message.text == 'Начать заново')
def zanovo(message):
    global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12, fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys
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
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Эпитафия')
    btn2 = types.KeyboardButton(text = 'Биография')
    kb.add(btn1)
    kb.add(btn2)
    bot.send_message(message.chat.id, 'Выберете действие', reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == 'Прошлый вопрос')
def prosh_vopr(message):
    global flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12
    bot.send_message(message.chat.id, f'{prosh_vop(flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12)}')

@bot.message_handler(func = lambda message: True)
def info(message):
    # if message.text == 'Эпитафия' or message.text == 'Биография' or message.text == 'И то и то':
    #     main(message.chat.id, message.text)
    # else:
    #     bot.send_message(message.chat.id, 'Моя твоя не понимать')
    global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12, fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11, fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys
    if flag1 or fl1:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn2, btn3)
        kb.add(btn1)
        if prov(message.text, 'ФИО'):
            fio = message.text
            flag2 = True
            message.text = ''
            flag1 = False
            fl1 = False
            bot.send_message(message.chat.id, '''Введите дату рождения. 
Например: 01.01.2000''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО ещё раз, проверьте правильность написания. 
Например: ''', reply_markup=kb)
    elif flag2 or fl2:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'ДР'):
            dr = message.text
            flag3 = True
            message.text = ''
            flag2 = False
            fl2 = False
            bot.send_message(message.chat.id, '''Введите дату смерти. 
Например: 01.01.2000''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите дату рождения ещё раз, проверьте правильность написания. 
Например: 01.01.2000''', reply_markup=kb)
    elif flag3 or fl3:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'ДС'):
            ds = message.text
            flag4 = True
            message.text = ''
            flag3 = False
            fl3 = False
            bot.send_message(message.chat.id, '''Введите место рождения. 
Например: Россия''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите дату смерти ещё раз, проверьте правильность написания. 
Например: 01.01.2000''', reply_markup=kb)
    elif flag4 or fl4:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'МР'):
            mr = message.text
            flag5 = True
            message.text = ''
            flag4 = False
            fl4 = False
            bot.send_message(message.chat.id, '''Введите место смерти.
Например: Россия''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите место рождения ещё раз, проверьте правильность написания. 
Например: Россия''', reply_markup=kb)
    elif flag5 or fl5:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'МС'):
            ms = message.text
            flag6 = True
            message.text = ''
            flag5 = False
            fl5 = False
            bot.send_message(message.chat.id, '''Введите ФИО супруга(ги).
Например: Иванов Иван Иванович''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите место смерти ещё раз, проверьте правильность написания. 
Например: Россия''', reply_markup=kb)
    elif flag6 or fl6:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'Супруг'):
            supr = message.text
            flag7 = True
            message.text = ''
            flag6 = False
            fl6 = False
            bot.send_message(message.chat.id, '''Укажите учебное заведение, которое закончил этот человек.
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО супруга(ги) ещё раз, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif flag7 or fl7:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'обр'):
            obr = message.text
            flag8 = True
            message.text = ''
            flag7 = False
            fl7 = False
            bot.send_message(message.chat.id, '''Укажите род деятельности человека.
Например: Учёный математик''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите учебное заведение, которое закончил этот человек, проверьте правильность написания. 
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''', reply_markup=kb)
    elif flag8 or fl8:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'РД'):
            rd = message.text
            flag9 = True
            message.text = ''
            flag8 = False
            fl8 = False
            bot.send_message(message.chat.id, '''Укажите гражданство человека.
Например: Россия''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите род деятельности человека, проверьте правильность написания. 
Например: Учёный математик''', reply_markup=kb)
    elif flag9 or fl9:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'ГРАЖ'):
            graj = message.text
            flag10 = True
            message.text = ''
            flag9 = False
            fl9 = False
            bot.send_message(message.chat.id, '''Укажите ФИО детей.
Например: Иванов Иван Иванович''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите гражданство человека, проверьте правильность написания. 
Например: Россия''', reply_markup=kb)
    elif flag10 or fl10:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'Дети'):
            deti = message.text
            flag11 = True
            message.text = ''
            flag10 = False
            fl10 = False
            bot.send_message(message.chat.id, '''Укажите ФИО внуков:
Например: Иванов Иван Иванович''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО детей, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif flag11 or fl11:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'Внуки'):
            vnuki = message.text
            flag12 = True
            message.text = ''
            flag11 = False
            fl11 = False
            bot.send_message(message.chat.id, '''Введите награды, премии или достижения, которые есть у человека.
Например: Знак Почета 1954, 1981''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО внуков, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif flag12:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = f'Другой {deys}')
        btn2 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1)
        kb.add(btn2)
        if prov(message.text, 'дост'):
            dost = message.text
            flag12 = False
            bot.send_message(message.chat.id, f'''Вот {deys}:
{fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys}''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите награды, премии или достижения, которые есть у человека, проверьте правильность написания. 
Например: Знак Почета 1954, 1981''', reply_markup=kb)
    else:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Эпитафия')
        btn2 = types.KeyboardButton(text = 'Биография')
        kb.add(btn1)
        kb.add(btn2)
        bot.send_message(message.chat.id, 'моя твоя не понимать')
        bot.send_message(message.chat.id, 'Выберете действие', reply_markup=kb)

bot.polling()
