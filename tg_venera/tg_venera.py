import requests
import datetime
import telebot
import pickle
import re
from telebot import types
from geopy.geocoders import Nominatim

bot = telebot.TeleBot('token')
deys = ''

def main(person_info: dict, request_subject: dict) -> str:
    ai_role = ''
    if request_subject['deys'] == 'биография':
        ai_role = 'биограф'
    elif request_subject['deys'] == 'эпитафия':
        ai_role = 'надгробный писатель'

    prompt = {
        'modelUri': 'gpt://token/yandexgpt-lite',
        'completionOptions': {
            'stream': False,
            'temperature': 0.6,
            'maxTokens': '2000'
        },

        'messages': [
            {
                'role': 'system',
                'text': f'Ты {ai_role}, который составляет {request_subject['deys']} о человеке.'
            },
            {
                'role': 'user',
                'text': f'Привет! Я бы хотел, чтобы ты составил {request_subject['deys']} о человеке, сможешь сделать?'
            },
            {
                'role': 'assistant',
                'text': 'Привет! Хорошо, расскажи мне что-нибудь о нём.'
            },
            {
                'role': 'user',
                'text': f'Этого человека зовут {person_info['fio']}, он родился {person_info['dr']} '
                        f'в {person_info['mr']} и умер {person_info['ds']} в {person_info['ms']}. '
                        f'Его супругом(супругой) был(была) {person_info['supr']}. Этот человек окончил '
                        f'{person_info['obr']}. Его родом деятельности было {person_info['rd']}. Его гражданство - '
                        f'{person_info['graj']}. Из детей у него(неё) были {person_info['deti']}, а из внуков - '
                        f'{person_info['vnuki']}.'
            }
        ]
    }

    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Api-Key token'
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
    elif vopr == 'обр' or vopr == 'РД':
        if len(mes) >= 3:
            return True
        return False
    else:
        return True

# def prosh():
#     global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10 
#     if flag2:
#         flag1 = True
#         print(1)
#         return '''Введите ФИО.
# Например: Иванов Иван Иванович'''
#     elif flag3:
#         flag2 = True
#         print(2)
#         return '''Введите дату рождения. 
# Например: 01.01.2000'''
#     elif flag4:
#         flag3 = True
#         print(3)
#         return '''Введите дату смерти. 
# Например: 01.01.2000'''
#     elif flag5:
#         flag4 = True
#         print(4)
#         return '''Введите место рождения. 
# Например: Россия'''
#     elif flag6:
#         flag5 = True
#         print(5)
#         return '''Введите место смерти.
# Например: Россия'''
#     elif flag7:
#         flag6 = True
#         print(6)
#         return '''Введите ФИО супруга(ги).
# Например: Иванов Иван Иванович'''
#     elif flag8:
#         flag7 = True
#         print(7)
#         return '''Укажите учебное заведение, которое закончил этот человек.
# Например: Физико-технический институ (ФТИ) КФУ им. Вернадского'''
#     elif flag9:
#         flag8 = True
#         print(8)
#         return '''Укажите род деятельности человека.
# Например: Учёный математик'''
#     elif flag10:
#         flag9 = True
#         print(9)
#         return '''Укажите гражданство человека.
# Например: Россия'''
#     elif flag11:
#         flag10 = True
#         print(10)
#         return '''Укажите ФИО детей.
# Например: Иванов Иван Иванович'''
#     elif flag12:
#         flag11 = True
#         print(11)
#         return '''Укажите ФИО внуков:
# Например: Иванов Иван Иванович'''
#     else:
#         print(12)
#         return 'иди нахуй'

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
        if value == 'Следующий вопрос':
            massiv_otv[key] = None  
    return main(massiv_otv, massiv_deys)

@bot.message_handler(commands = ['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Эпитафия')
    btn2 = types.KeyboardButton(text = 'Биография')
    kb.add(btn1)
    kb.add(btn2)
    print(13)
    chat_id = message.chat.id
    if chat_id not in session:
        session[chat_id] = {'flag1': False, 'flag2': False, 'flag3': False, 'flag4': False, 'flag5': False, 'flag6': False, 'flag7': False, 'flag8': False, 'flag9': False, 'flag10': False, 'flag11': False, 'flag12': False, 'fio': '', 'dr': '', 'ds': '', 'mr': '', 'ms': '', 'supr': '', 'obr': '', 'rd': '', 'graj': '', 'deti': '', 'vnuki': '', 'dost': '', 'deys': ''}
        save_session(session)
    bot.send_message(message.chat.id, 'Здрасьте. Выберете действие', reply_markup=kb) ### 1

@bot.message_handler(func = lambda message: message.text == 'Эпитафия')
def epitafia(message):
    global deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Следующий вопрос')
    btn2 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn1)
    kb.add(btn2)
    print(14)
    chat_id = message.chat.id
    deys = message.text
    session[chat_id]['deys'] = message.text
    session[chat_id]['flag1'] = True
    bot.send_message(message.chat.id, '''Введите ФИО.
Например: Иванов Иван Иванович''', reply_markup=kb) ### 2
    save_session(session)

@bot.message_handler(func = lambda message: message.text == 'Биография')
def biografia(message):
    global deys
    chat_id = message.chat.id
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Следующий вопрос')
    btn2 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn1)
    kb.add(btn2)
    print(15)
    deys = message.text
    session[chat_id]['deys'] = message.text
    session[chat_id]['flag1'] = True
    bot.send_message(message.chat.id, '''Введите ФИО.
Например: Иванов Иван Иванович''', reply_markup=kb) ### 3
    save_session(session)

@bot.message_handler(func = lambda message: message.text == f'Другой {deys}')
def noviy(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = f'Другой {deys}')
    btn2 = types.KeyboardButton(text = 'Начать заново')
    kb.add(btn1)
    kb.add(btn2)
    chat_id = message.chat.id
    print(16)
    bot.send_message(message.chat.id, f'''Вот {session[chat_id]['deys']}:
{mass_for_main(session[chat_id]['fio'], session[chat_id]['dr'], session[chat_id]['ds'], session[chat_id]['mr'], session[chat_id]['ms'], session[chat_id]['supr'], session[chat_id]['obr'], session[chat_id]['rd'], session[chat_id]['graj'], session[chat_id]['deti'], session[chat_id]['vnuki'], session[chat_id]['dost'], session[chat_id]['deys'])}''', reply_markup=kb)
    
@bot.message_handler(func = lambda message: message.text == 'Начать заново')
def zanovo(message):
    global deys
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text = 'Эпитафия')
    btn2 = types.KeyboardButton(text = 'Биография')
    kb.add(btn1)
    kb.add(btn2)
    print(17)
    chat_id = message.chat.id
    session[chat_id] = {'flag1': False, 'flag2': False, 'flag3': False, 'flag4': False, 'flag5': False, 'flag6': False, 'flag7': False, 'flag8': False, 'flag9': False, 'flag10': False, 'flag11': False, 'flag12': False, 'fio': '', 'dr': '', 'ds': '', 'mr': '', 'ms': '', 'supr': '', 'obr': '', 'rd': '', 'graj': '', 'deti': '', 'vnuki': '', 'dost': '',}
    deys = ''
    save_session(session)
    bot.send_message(message.chat.id, 'Выберете действие', reply_markup=kb) ### 4

@bot.message_handler(func = lambda message: message.text == 'Прошлый вопрос')
def prosh_vopr(message):
    print(18)
    chat_id = message.chat.id
    if session[chat_id]['flag2']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1)
        kb.add(btn2)
        session[chat_id]['flag1'] = True
        print(1)
        bot.send_message(message.chat.id, '''Введите ФИО.
Например: Иванов Иван Иванович''', reply_markup=kb)
    elif session[chat_id]['flag3']:
        session[chat_id]['flag2'] = True
        print(2)
        bot.send_message(message.chat.id, '''Введите дату рождения. 
Например: 01.01.2000''')
    elif session[chat_id]['flag4']:
        session[chat_id]['flag3'] = True
        print(3)
        bot.send_message(message.chat.id, '''Введите дату смерти. 
Например: 01.01.2000''')
    elif session[chat_id]['flag5']:
        session[chat_id]['flag4'] = True
        print(4)
        bot.send_message(message.chat.id, '''Введите место рождения. 
Например: Россия''')
    elif session[chat_id]['flag6']:
        session[chat_id]['flag5'] = True
        print(5)
        bot.send_message(message.chat.id, '''Введите место смерти.
Например: Россия''')
    elif session[chat_id]['flag7']:
        session[chat_id]['flag6'] = True
        print(6)
        bot.send_message(message.chat.id, '''Введите ФИО супруга(ги).
Например: Иванов Иван Иванович''')
    elif session[chat_id]['flag8']:
        session[chat_id]['flag7'] = True
        print(7)
        bot.send_message(message.chat.id, '''Укажите учебное заведение, которое закончил этот человек.
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''')
    elif session[chat_id]['flag9']:
        session[chat_id]['flag8'] = True
        print(8)
        bot.send_message(message.chat.id, '''Укажите род деятельности человека.
Например: Учёный математик''')
    elif session[chat_id]['flag10']:
        session[chat_id]['flag9'] = True
        print(9)
        bot.send_message(message.chat.id, '''Укажите гражданство человека.
Например: Россия''')
    elif session[chat_id]['flag11']:
        session[chat_id]['flag10'] = True
        print(10)
        bot.send_message(message.chat.id, '''Укажите ФИО детей.
Например: Иванов Иван Иванович''')
    elif session[chat_id]['flag12']:
        session[chat_id]['flag11'] = True
        print(11)
        bot.send_message(message.chat.id, '''Укажите ФИО внуков:
Например: Иванов Иван Иванович''')
    else:
        print(12)
        bot.send_message(message.chat.id, 'иди нахуй') ### 5

@bot.message_handler(func = lambda message: True)
def info(message):
    # if message.text == 'Эпитафия' or message.text == 'Биография' or message.text == 'И то и то':
    #     main(message.chat.id, message.text)
    # else:
    #     bot.send_message(message.chat.id, 'Моя твоя не понимать')
    chat_id = message.chat.id
    if session[chat_id]['flag1']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn2, btn3)
        kb.add(btn1)
        if prov(message.text, 'ФИО') or message.text == 'Следующий вопрос':
            session[chat_id]['fio'] = message.text
            session[chat_id]['flag2'] = True
            message.text = ''
            session[chat_id]['flag1'] = False
            print(19)
            bot.send_message(message.chat.id, '''Введите дату рождения. 
Например: 01.01.2000''', reply_markup=kb) ### 6
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО ещё раз, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb) ### 7
            save_session(session)
    elif session[chat_id]['flag2']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'ДР') or message.text == 'Следующий вопрос':
            session[chat_id]['dr'] = message.text
            session[chat_id]['flag3'] = True
            message.text = ''
            session[chat_id]['flag2'] = False
            print(20)
            bot.send_message(message.chat.id, '''Введите дату смерти. 
Например: 01.01.2000''', reply_markup=kb) ### 8
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите дату рождения ещё раз, проверьте правильность написания. 
Например: 01.01.2000''', reply_markup=kb) ### 9
            save_session(session)
    elif session[chat_id]['flag3']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'ДС') or message.text == 'Следующий вопрос':
            session[chat_id]['ds'] = message.text
            session[chat_id]['flag4'] = True
            message.text = ''
            session[chat_id]['flag3'] = False
            print(21)
            bot.send_message(message.chat.id, '''Введите место рождения. 
Например: Россия''', reply_markup=kb) ### 10
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите дату смерти ещё раз, проверьте правильность написания. 
Например: 01.01.2000''', reply_markup=kb) ### 11
            save_session(session)
    elif session[chat_id]['flag4']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'МР') or message.text == 'Следующий вопрос':
            session[chat_id]['mr'] = message.text
            session[chat_id]['flag5'] = True
            message.text = ''
            session[chat_id]['flag4'] = False
            print(22)
            bot.send_message(message.chat.id, '''Введите место смерти.
Например: Россия''', reply_markup=kb) ### 12
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите место рождения ещё раз, проверьте правильность написания. 
Например: Россия''', reply_markup=kb) ### 13
            save_session(session)
    elif session[chat_id]['flag5']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'МС') or message.text == 'Следующий вопрос':
            session[chat_id]['ms'] = message.text
            session[chat_id]['flag6'] = True
            message.text = ''
            session[chat_id]['flag5'] = False
            print(23)
            bot.send_message(message.chat.id, '''Введите ФИО супруга(ги).
Например: Иванов Иван Иванович''', reply_markup=kb) ### 14
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите место смерти ещё раз, проверьте правильность написания. 
Например: Россия''', reply_markup=kb) ### 15
            save_session(session)
    elif session[chat_id]['flag6']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'Супруг') or message.text == 'Следующий вопрос':
            session[chat_id]['supr'] = message.text
            session[chat_id]['flag7'] = True
            message.text = ''
            session[chat_id]['flag6'] = False
            print(24)
            bot.send_message(message.chat.id, '''Укажите учебное заведение, которое закончил этот человек.
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''', reply_markup=kb) ### 16
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО супруга(ги) ещё раз, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb) ### 17
            save_session(session)
    elif session[chat_id]['flag7']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'обр') or message.text == 'Следующий вопрос':
            session[chat_id]['obr'] = message.text
            session[chat_id]['flag8'] = True
            message.text = ''
            session[chat_id]['flag7'] = False
            print(25)
            bot.send_message(message.chat.id, '''Укажите род деятельности человека.
Например: Учёный математик''', reply_markup=kb) ### 18
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите учебное заведение, которое закончил этот человек, проверьте правильность написания. 
Например: Физико-технический институ (ФТИ) КФУ им. Вернадского''', reply_markup=kb) ### 19
            save_session(session)
    elif session[chat_id]['flag8']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'РД') or message.text == 'Следующий вопрос':
            session[chat_id]['rd'] = message.text
            session[chat_id]['flag9'] = True
            message.text = ''
            session[chat_id]['flag8'] = False
            print(26)
            bot.send_message(message.chat.id, '''Укажите гражданство человека.
Например: Россия''', reply_markup=kb) ### 20
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите род деятельности человека, проверьте правильность написания. 
Например: Учёный математик''', reply_markup=kb) ### 21
            save_session(session)    
    elif session[chat_id]['flag9']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'ГРАЖ') or message.text == 'Следующий вопрос':
            session[chat_id]['graj'] = message.text
            session[chat_id]['flag10'] = True
            message.text = ''
            session[chat_id]['flag9'] = False
            print(27)
            bot.send_message(message.chat.id, '''Укажите ФИО детей.
Например: Иванов Иван Иванович''', reply_markup=kb) ### 22
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите гражданство человека, проверьте правильность написания. 
Например: Россия''', reply_markup=kb) ### 23
            save_session(session)
    elif session[chat_id]['flag10']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'Дети') or message.text == 'Следующий вопрос':
            session[chat_id]['deti'] = message.text
            session[chat_id]['flag11'] = True
            message.text = ''
            session[chat_id]['flag10'] = False
            print(28)
            bot.send_message(message.chat.id, '''Укажите ФИО внуков:
Например: Иванов Иван Иванович''', reply_markup=kb) ### 24
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО детей, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb) ### 25
            save_session(session)
    elif session[chat_id]['flag11']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Следующий вопрос')
        btn2 = types.KeyboardButton(text = 'Прошлый вопрос')
        btn3 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1, btn2)
        kb.add(btn3)
        if prov(message.text, 'Внуки') or message.text == 'Следующий вопрос':
            session[chat_id]['vnuki'] = message.text
            session[chat_id]['flag12'] = True
            message.text = ''
            session[chat_id]['flag11'] = False
            print(29)
            bot.send_message(message.chat.id, '''Введите награды, премии или достижения, которые есть у человека.
Например: Знак Почета 1954, 1981''', reply_markup=kb) ### 26
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите ФИО внуков, проверьте правильность написания. 
Например: Иванов Иван Иванович''', reply_markup=kb) ### 27
            save_session(session)
    elif session[chat_id]['flag12']:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = f'Другой {deys}')
        btn2 = types.KeyboardButton(text = 'Начать заново')
        kb.add(btn1)
        kb.add(btn2)
        if prov(message.text, 'дост'):
            session[chat_id]['dost'] = message.text
            session[chat_id]['flag12'] = False
            print(30)
            bot.send_message(message.chat.id, f'''Вот {session[chat_id]['deys']}:
{mass_for_main(session[chat_id]['fio'], session[chat_id]['dr'], session[chat_id]['ds'], session[chat_id]['mr'], session[chat_id]['ms'], session[chat_id]['supr'], session[chat_id]['obr'], session[chat_id]['rd'], session[chat_id]['graj'], session[chat_id]['deti'], session[chat_id]['vnuki'], session[chat_id]['dost'], session[chat_id]['deys'])}''', reply_markup=kb)
            save_session(session)
        else:
            bot.send_message(message.chat.id, '''Что то пошло не так, введите награды, премии или достижения, которые есть у человека, проверьте правильность написания. 
Например: Знак Почета 1954, 1981''', reply_markup=kb)
            save_session(session)
    else:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text = 'Эпитафия')
        btn2 = types.KeyboardButton(text = 'Биография')
        kb.add(btn1)
        kb.add(btn2)
        print(31)
        bot.send_message(message.chat.id, 'моя твоя не понимать') ### 28
        bot.send_message(message.chat.id, 'Выберете действие', reply_markup=kb)
        save_session(session)

bot.polling()
