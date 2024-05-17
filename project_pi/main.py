from flask import Flask, render_template, request, session
import json, uuid, os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'default_secret_key'
user_data = {}

def generate_session_id():
    return str(uuid.uuid4())

def prov_nast():
    user_data_for_session = user_data.get(session['session_id'], {})
    slov_kom = user_data_for_session['Команды']
    slov_dl = user_data_for_session['Длительность раунда']
    slov_kl = user_data_for_session['Количество очков для победы']
    a = 0
    shet_kom = 0
    shet_dl_rau = 0
    shet_kl_och = 0
    
    for key, value in slov_kom.items():
        if slov_kom[key]['Статус'] == True:
            shet_kom+=1
    if shet_kom>1:
        a+=1
        shet_kom=0
    else:
        shet_kom=0
        return 'кол-во команд'
    
    for key, value in slov_dl.items():
        if slov_dl[key] == True:
            shet_dl_rau+=1
    if shet_dl_rau == 1:
        a+=1
        shet_dl_rau=0
    else:
        shet_dl_rau=0
        return 'дл раунда'
    
    for key, value in slov_kl.items():
        if slov_kl[key] == True:
            shet_kl_och+=1
    if shet_kl_och == 1:
        a+=1
        shet_kl_och=0
    else:
        shet_kl_och=0
        return 'кол-во оч'
    
    if a == 3:
        return True
    return False
    
@app.route('/', methods=['GET', 'POST'])
def main_str():
    session.clear()
    session_id = session.get('session_id', None)
    print(session)
    print(session_id)
    if session_id is None:
        session['session_id'] = generate_session_id()
        user_data[session['session_id']] = {
                "Категория": {
                "Базовый набор": False,
                "IT": False,
                "Юриспруденция": False,
                "Новый год": False,
                "Marvel": False,
                "Природа": False,
                "Еда": False,
                "Фильмы": False,
                "Свой набор": {
                    "Статус": False,
                    "Слова": {
                        "0": "Слова",
                        "1": '',
                        "2": '',
                        "3": '',
                        "4": '',
                        "5": '',
                        "6": '',
                        "7": '',
                        "8": '',
                        "9": '',
                        "10": '',
                        "11": '',
                        "12": '',
                        "13": '',
                        "14": ''
                    }
                }
            },
            "Длительность раунда": {
                "30": False,
                "40": False,
                "50": False,
                "60": False,
                "120": False
            },
            "Количество очков для победы": {
                "20": False,
                "30": False,
                "50": False,
                "60": False,
                "80": False
            },
            "Команды": {
                "1": {
                    "Статус": False,
                    "Название": ''
                },
                "2": {
                    "Статус": False,
                    "Название": ''
                },
                "3": {
                    "Статус": False,
                    "Название": ''
                },
                "4": {
                    "Статус": False,
                    "Название": ''
                },
                "5": {
                    "Статус": False,
                    "Название": ''
                }
            }
        }
    user_data_for_session = user_data.get(session['session_id'], {})
    print(session)
    print(session_id)
    print(user_data_for_session)
    return render_template('main_str.html')

@app.route('/next', methods=['GET', 'POST'])
def index2():
    user_data_for_session = user_data.get(session['session_id'], {})
    team_1 = user_data_for_session["Команды"]["1"]["Название"]
    team_2 = user_data_for_session["Команды"]["2"]["Название"]
    team_3 = user_data_for_session["Команды"]["3"]["Название"]
    team_4 = user_data_for_session["Команды"]["4"]["Название"]
    team_5 = user_data_for_session["Команды"]["5"]["Название"]
    if request.method == 'POST':
        teams_1 = request.form['team_1']
        teams_2 = request.form['team_2']
        teams_3 = request.form['team_3']
        teams_4 = request.form['team_4']
        teams_5 = request.form['team_5']
        if teams_1:
            user_data_for_session["Команды"]["1"]["Статус"]=True
            user_data_for_session["Команды"]["1"]["Название"]=teams_1
        else:
            user_data_for_session["Команды"]["1"]["Статус"]=False
            user_data_for_session["Команды"]["1"]["Название"]=''
        if teams_2:
            user_data_for_session["Команды"]["2"]["Статус"]=True
            user_data_for_session["Команды"]["2"]["Название"]=teams_2
        else:
            user_data_for_session["Команды"]["2"]["Статус"]=False
            user_data_for_session["Команды"]["2"]["Название"]=''
        if teams_3:
            user_data_for_session["Команды"]["3"]["Статус"]=True
            user_data_for_session["Команды"]["3"]["Название"]=teams_3
        else:
            user_data_for_session["Команды"]["3"]["Статус"]=False
            user_data_for_session["Команды"]["3"]["Название"]=''
        if teams_4:
            user_data_for_session["Команды"]["4"]["Статус"]=True
            user_data_for_session["Команды"]["4"]["Название"]=teams_4
        else:
            user_data_for_session["Команды"]["4"]["Статус"]=False
            user_data_for_session["Команды"]["4"]["Название"]=''
        if teams_5:
            user_data_for_session["Команды"]["5"]["Статус"]=True
            user_data_for_session["Команды"]["5"]["Название"]=teams_5
        else:
            user_data_for_session["Команды"]["5"]["Статус"]=False
            user_data_for_session["Команды"]["5"]["Название"]=''
        return render_template('index_3.html')
    return render_template('index2.html', team_1 = team_1, team_2 = team_2, team_3 = team_3, team_4 = team_4, team_5 = team_5)

@app.route('/setings')
def set():
    return render_template('index_3.html')

@app.route('/save_set_1')
def save_set_1():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Длительность раунда"]["30"] == False:
        user_data_for_session["Длительность раунда"]["30"]=True
    else:
        user_data_for_session["Длительность раунда"]["30"]=False
    user_data_for_session["Длительность раунда"]["40"]=False
    user_data_for_session["Длительность раунда"]["50"]=False
    user_data_for_session["Длительность раунда"]["60"]=False
    user_data_for_session["Длительность раунда"]["120"]=False
    return render_template('index_3.html')

@app.route('/save_set_2')
def save_set_2():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Длительность раунда"]["40"] == False:
        user_data_for_session["Длительность раунда"]["40"]=True
    else:
        user_data_for_session["Длительность раунда"]["40"]=False
    user_data_for_session["Длительность раунда"]["30"]=False
    user_data_for_session["Длительность раунда"]["50"]=False
    user_data_for_session["Длительность раунда"]["60"]=False
    user_data_for_session["Длительность раунда"]["120"]=False
    return render_template('index_3.html')

@app.route('/save_set_3')
def save_set_3():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Длительность раунда"]["50"] == False:
        user_data_for_session["Длительность раунда"]["50"]=True
    else:
        user_data_for_session["Длительность раунда"]["50"]=False
    user_data_for_session["Длительность раунда"]["40"]=False
    user_data_for_session["Длительность раунда"]["30"]=False
    user_data_for_session["Длительность раунда"]["60"]=False
    user_data_for_session["Длительность раунда"]["120"]=False
    return render_template('index_3.html')

@app.route('/save_set_4')
def save_set_4():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Длительность раунда"]["60"] == False:
        user_data_for_session["Длительность раунда"]["60"]=True
    else:
        user_data_for_session["Длительность раунда"]["60"]=False
    user_data_for_session["Длительность раунда"]["40"]=False
    user_data_for_session["Длительность раунда"]["50"]=False
    user_data_for_session["Длительность раунда"]["30"]=False
    user_data_for_session["Длительность раунда"]["120"]=False
    return render_template('index_3.html')

@app.route('/save_set_5')
def save_set_5():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Длительность раунда"]["120"] == False:
        user_data_for_session["Длительность раунда"]["120"]=True
    else:
        user_data_for_session["Длительность раунда"]["120"]=False
    user_data_for_session["Длительность раунда"]["40"]=False
    user_data_for_session["Длительность раунда"]["50"]=False
    user_data_for_session["Длительность раунда"]["60"]=False
    user_data_for_session["Длительность раунда"]["30"]=False
    return render_template('index_3.html')

@app.route('/save_set_6')
def save_set_6():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Количество очков для победы"]["20"] == False:
        user_data_for_session["Количество очков для победы"]["20"]=True
    else:
        user_data_for_session["Количество очков для победы"]["20"]=False
    user_data_for_session["Количество очков для победы"]["30"]=False
    user_data_for_session["Количество очков для победы"]["50"]=False
    user_data_for_session["Количество очков для победы"]["60"]=False
    user_data_for_session["Количество очков для победы"]["80"]=False
    return render_template('index_3.html')

@app.route('/save_set_7')
def save_set_7():
    user_data_for_session = user_data.get(session['session_id'], {})    
    if user_data_for_session["Количество очков для победы"]["30"] == False:
        user_data_for_session["Количество очков для победы"]["30"]=True
    else:
        user_data_for_session["Количество очков для победы"]["30"]=False
    user_data_for_session["Количество очков для победы"]["20"]=False
    user_data_for_session["Количество очков для победы"]["50"]=False
    user_data_for_session["Количество очков для победы"]["60"]=False
    user_data_for_session["Количество очков для победы"]["80"]=False
    return render_template('index_3.html')


@app.route('/save_set_8')
def save_set_8():
    user_data_for_session = user_data.get(session['session_id'], {})    
    if user_data_for_session["Количество очков для победы"]["50"] == False:
        user_data_for_session["Количество очков для победы"]["50"]=True
    else:
        user_data_for_session["Количество очков для победы"]["50"]=False
    user_data_for_session["Количество очков для победы"]["30"]=False
    user_data_for_session["Количество очков для победы"]["20"]=False
    user_data_for_session["Количество очков для победы"]["60"]=False
    user_data_for_session["Количество очков для победы"]["80"]=False
    return render_template('index_3.html')


@app.route('/save_set_9')
def save_set_9():
    user_data_for_session = user_data.get(session['session_id'], {})    
    if user_data_for_session["Количество очков для победы"]["60"] == False:
        user_data_for_session["Количество очков для победы"]["60"]=True
    else:
        user_data_for_session["Количество очков для победы"]["60"]=False
    user_data_for_session["Количество очков для победы"]["30"]=False
    user_data_for_session["Количество очков для победы"]["50"]=False
    user_data_for_session["Количество очков для победы"]["20"]=False
    user_data_for_session["Количество очков для победы"]["80"]=False
    return render_template('index_3.html')

@app.route('/save_set_10')
def save_set_10():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Количество очков для победы"]["80"] == False:
        user_data_for_session["Количество очков для победы"]["80"]=True
    else:
        user_data_for_session["Количество очков для победы"]["80"]=False
    user_data_for_session["Количество очков для победы"]["30"]=False
    user_data_for_session["Количество очков для победы"]["50"]=False
    user_data_for_session["Количество очков для победы"]["60"]=False
    user_data_for_session["Количество очков для победы"]["20"]=False
    return render_template('index_3.html')

@app.route('/save')
def save():
    return render_template('index.html')

@app.route('/save_text_1')
def save_tex_1():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["Базовый набор"] == True:
        user_data_for_session["Категория"]["Базовый набор"]=False
    else:
        user_data_for_session['Категория']["Базовый набор"]=True
    return render_template('index.html')

@app.route('/save_text_2')
def save_text_2():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["IT"] == True:
        user_data_for_session["Категория"]["IT"]=False
    else:
        user_data_for_session['Категория']["IT"]=True
    return render_template('index.html')

@app.route('/save_text_3')
def save_text_3():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["Юриспруденция"] == True:
        user_data_for_session["Категория"]["Юриспруденция"]=False
    else:
        user_data_for_session['Категория']["Юриспруденция"]=True
    return render_template('index.html')

@app.route('/save_text_4')
def save_text_4():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["Новый год"] == True:
        user_data_for_session["Категория"]["Новый год"]=False
    else:
        user_data_for_session['Категория']["Новый год"]=True
    return render_template('index.html')

@app.route('/save_text_5')
def save_text_5():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["Marvel"] == True:
        user_data_for_session["Категория"]["Marvel"]=False
    else:
        user_data_for_session['Категория']["Marvel"]=True
    return render_template('index.html')

@app.route('/save_text_6')
def save_text_6():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["Природа"] == True:
        user_data_for_session["Категория"]["Природа"]=False
    else:
        user_data_for_session['Категория']["Природа"]=True
    return render_template('index.html')

@app.route('/save_text_7')
def save_text_7():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["Еда"] == True:
        user_data_for_session["Категория"]["Еда"]=False
    else:
        user_data_for_session['Категория']["Еда"]=True
    return render_template('index.html')

@app.route('/save_text_8')
def save_text_8():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["Фильмы"] == True:
        user_data_for_session["Категория"]["Фильмы"]=False
    else:
        user_data_for_session['Категория']["Фильмы"]=True
    return render_template('index.html')

@app.route('/save_text_10')
def save_text_10():
    user_data_for_session = user_data.get(session['session_id'], {})
    if user_data_for_session["Категория"]["Свой набор"]["Статус"] == True:
        user_data_for_session["Категория"]["Свой набор"]["Статус"]=False
    else:
        user_data_for_session['Категория']["Свой набор"]["Статус"]=True
    return render_template('index.html')

@app.route('/save_text_9', methods=['GET', 'POST']) ###
def save_text_9():
    user_data_for_session = user_data.get(session['session_id'], {})
    words=[]
    if request.method == 'POST':
        new_word = request.form['word']
        for i in range(15):
            if not user_data_for_session["Категория"]["Свой набор"]["Слова"][str(i)]:
                user_data_for_session["Категория"]["Свой набор"]["Слова"][str(i)]=new_word
                break
        for j in range(1, 15):
            if user_data_for_session["Категория"]["Свой набор"]["Слова"][str(i)]:
                words.append(user_data_for_session["Категория"]["Свой набор"]["Слова"][str(j)])
    return render_template('add_words.html', words=words)

@app.route('/game') ###
def game():
    if prov_nast() == 'дл раунда':
        return 'Соси дл раунда'
    elif prov_nast() == 'кол-во команд':
        return 'Соси кол-во команд'
    elif prov_nast() == 'кол-во оч':
        return 'Соси кол-во оч'
    elif prov_nast():
        return 'Не соси'
    return 'Просто соси'

if __name__ == '__main__':
    app.run(debug=True)
