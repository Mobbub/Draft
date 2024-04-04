import requests
import datetime
import telebot
from telebot import types
from geopy.geocoders import Nominatim

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

def main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys):
    pass

def prov(mes, vopr):
    if vopr == 'ФИО':
         if len(mes.split()) == 3:
             return True
         return False
    elif vopr == 'ДР' or vopr == 'ДС':
        try:
            date = datetime.datetime.strptime(mes, "%d.%m.%Y")
            return True
        except ValueError:
            return False
    elif vopr == 'МР' or vopr == 'МС':
            geolocator = Nominatim(user_agent="my_application")  # Создание объекта геокодера
            location = geolocator.geocode(mes)  # Геокодирование места
            if location is not None:
                return True
            return False
    elif vopr == 'Дети' or vopr == 'Внуки' or vopr == 'Супруг':
        mes_nov = ''
        schet = 0
        for i in range(len(mes)):
            if mes[i] != ',':
                mes_nov += mes[i]
            else:
                schet += 1
        if (len(mes_nov.split()) % 3 == 0) and (len(mes_nov.split()) % 3 == schet - 1):
            return True
        return False
    else:
        return True

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
        'deys': deys
    }
    for key, value in massiv_otv.items():
        if value == 'Следующий вопрос':
            massiv_otv[key] = None  
    return main(massiv_otv)

@bot.message_handler(commands = ['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Эпитафия')
    btn2 = types.KeyboardButton(text = 'Биография')
    kb.add(btn1)
    kb.add(btn2)
    print(13)
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
    print(14)
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
    print(15)
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
    print(16)
    bot.send_message(message.chat.id, '''Вот {deys}
{mass_for_main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys)}''', reply_markup=kb)
    
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
    print(17)
    bot.send_message(message.chat.id, 'Выберете действие', reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == 'Прошлый вопрос')
def prosh_vopr(message):
    print(18)
    global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12 
    if flag2:
        flag1 = True
        print(1)
        bot.send_message(message.chat.id, '''Введите ФИО.
Например: Иванов Иван Иванович''')
    elif flag3:
        flag2 = True
        print(2)
        bot.send_message(message.chat.id, '''Введите дату рождения. 
Например: 01.01.2000''')
    elif flag4:
        flag3 = True
        print(3)
        bot.send_message(message.chat.id, '''Введите дату смерти. 
Например: 01.01.2000''')
    elif flag5:
        flag4 = True
        print(4)
        bot.send_message(message.chat.id, '''Введите место рождения. 
Например: Россия''')
    elif flag6:
        flag5 = True
        print(5)
        bot.send_message(message.chat.id, '''Введите место смерти.
Например: Россия''')
    elif flag7:
        flag6 = True
        print(6)
        bot.send_message(message.chat.id, '''Введите ФИО супруга(ги).
Например: Иванов Иван Иванович''')
    elif flag8:
        flag7 = True
        print(7)
        bot.send_message(message.chat.id, '''Укажите учебное заведение, которое закончил этот человек.
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''')
    elif flag9:
        flag8 = True
        print(8)
        bot.send_message(message.chat.id, '''Укажите род деятельности человека.
Например: Учёный математик''')
    elif flag10:
        flag9 = True
        print(9)
        bot.send_message(message.chat.id, '''Укажите гражданство человека.
Например: Россия''')
    elif flag11:
        flag10 = True
        print(10)
        bot.send_message(message.chat.id, '''Укажите ФИО детей.
Например: Иванов Иван Иванович''')
    elif flag12:
        flag11 = True
        print(11)
        bot.send_message(message.chat.id, '''Укажите ФИО внуков:
Например: Иванов Иван Иванович''')
    else:
        print(12)
        bot.send_message(message.chat.id, 'иди нахуй')

@bot.message_handler(func = lambda message: True)
def info(message):
    global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12, fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11, fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys
    if flag1:
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
            print(19)
            bot.send_message(message.chat.id, '''Введите дату рождения. 
Например: 01.01.2000''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО ещё раз, проверьте правильность написания. 
Например: ''', reply_markup=kb)
    elif flag2:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1)
        kb.add(btn2)
        if prov(message.text, 'ДР'):
            dr = message.text
            flag3 = True
            message.text = ''
            flag2 = False
            print(20)
            bot.send_message(message.chat.id, '''Введите дату смерти. 
Например: 01.01.2000''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите дату рождения ещё раз, проверьте правильность написания. 
Например: 01.01.2000''', reply_markup=kb)
    elif flag3:
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
            print(21)
            bot.send_message(message.chat.id, '''Введите место рождения. 
Например: Россия''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите дату смерти ещё раз, проверьте правильность написания. 
Например: 01.01.2000''', reply_markup=kb)
    elif flag4:
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
            print(22)
            bot.send_message(message.chat.id, '''Введите место смерти.
Например: Россия''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите место рождения ещё раз, проверьте правильность написания. 
Например: Россия''', reply_markup=kb)
    elif flag5:
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
            print(23)
            bot.send_message(message.chat.id, '''Введите ФИО супруга(ги).
Например: Иванов Иван Иванович''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите место смерти ещё раз, проверьте правильность написания. 
Например: Россия''', reply_markup=kb)
    elif flag6:
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
            print(24)
            bot.send_message(message.chat.id, '''Укажите учебное заведение, которое закончил этот человек.
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО супруга(ги) ещё раз, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif flag7:
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
            print(25)
            bot.send_message(message.chat.id, '''Укажите род деятельности человека.
Например: Учёный математик''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите учебное заведение, которое закончил этот человек, проверьте правильность написания. 
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''', reply_markup=kb)
    elif flag8:
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
            print(26)
            bot.send_message(message.chat.id, '''Укажите гражданство человека.
Например: Россия''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите род деятельности человека, проверьте правильность написания. 
Например: Учёный математик''', reply_markup=kb)
    elif flag9:
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
            print(27)
            bot.send_message(message.chat.id, '''Укажите ФИО детей.
Например: Иванов Иван Иванович''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите гражданство человека, проверьте правильность написания. 
Например: Россия''', reply_markup=kb)
    elif flag10:
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
            print(28)
            bot.send_message(message.chat.id, '''Укажите ФИО внуков:
Например: Иванов Иван Иванович''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО детей, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif flag11:
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
            print(29)
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
            print(30)
            bot.send_message(message.chat.id, f'''Вот {deys}:
{mass_for_main(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost, deys)}''', reply_markup=kb)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите награды, премии или достижения, которые есть у человека, проверьте правильность написания. 
Например: Знак Почета 1954, 1981''', reply_markup=kb)
    else:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Эпитафия')
        btn2 = types.KeyboardButton(text = 'Биография')
        kb.add(btn1)
        kb.add(btn2)
        print(31)
        bot.send_message(message.chat.id, 'моя твоя не понимать')
        bot.send_message(message.chat.id, 'Выберете действие', reply_markup=kb)

bot.polling()
