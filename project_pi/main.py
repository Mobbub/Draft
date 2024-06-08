from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import uuid, os, time, random

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'default_secret_key'
user_data = {}

words_igr = {
    "Базовый набор": {
        "1": "fdsf",
        "2": "dsfdsf",
        "3": "dsfsdf",
        "4": "dddsfdsf",
        "5": "wewqewq",
        "6": "ewqefds",
        "7": "gdfgfdg",
        "8": "gdfgdfg",
        "9": "gfdgfdg",
        "10": "fdgfdgfdg"
    },
    "IT": {
        "1": "gfdgdfgdfg",
        "2": "fgdbvcbvc",
        "3": "ghfgjhgf",
        "4": "jghyjyt",
        "5": "nbvnvb",
        "6": "serewr",
        "7": "kuyk",
        "8": "bvcbvc",
        "9": "tttt",
        "10": "jjjjjjj"
    },
    "Юриспруденция": {
        "1": "fdgqwe",
        "2": "qwert",
        "3": "hjklii",
        "4": "vcbvcbvc",
        "5": "luiloiu",
        "6": "zxczxc",
        "7": "dfdsfdsfsdf",
        "8": "dfffffffffffff",
        "9": "dyyyyyyyyyy",
        "10": "rrrrrrrrrrrrrrd"
    },
    "Новый год": {
        "1": "d",
        "2": "d",
        "3": "d",
        "4": "d",
        "5": "d",
        "6": "d",
        "7": "d",
        "8": "d",
        "9": "d",
        "10": "d"
    },
    "Marvel": {
        "1": "d",
        "2": "d",
        "3": "d",
        "4": "d",
        "5": "d",
        "6": "d",
        "7": "d",
        "8": "d",
        "9": "d",
        "10": "d"
    },
    "Природа": {
        "1": "d",
        "2": "d",
        "3": "d",
        "4": "d",
        "5": "d",
        "6": "d",
        "7": "d",
        "8": "d",
        "9": "d",
        "10": "d"
    },
    "Еда": {
        "1": "d",
        "2": "d",
        "3": "d",
        "4": "d",
        "5": "d",
        "6": "d",
        "7": "d",
        "8": "d",
        "9": "d",
        "10": "d"
    },
    "Фильмы": {
        "1": "d",
        "2": "d",
        "3": "d",
        "4": "d",
        "5": "d",
        "6": "d",
        "7": "d",
        "8": "d",
        "9": "d",
        "10": "d"
    }
}

def generate_session_id():
    return str(uuid.uuid4())

def prov_nast():
    user_data_for_session = user_data.get(session['session_id'], {})
    slov_kom = user_data_for_session['Команды']
    slov_dl = user_data_for_session['Длительность раунда']
    slov_kl = user_data_for_session['Количество очков для победы']
    slov_sv = user_data_for_session['Категория']['Свой набор']['Слова']
    status_sv = user_data_for_session['Категория']['Свой набор']['Статус']
    slov_kat = user_data_for_session['Категория']
    a = 0
    shet_kom = 0
    shet_dl_rau = 0
    shet_kl_och = 0
    shet_sv = 0
    shet_kat = 0
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

    if status_sv==True:
        for i in range(1, 301):
            if slov_sv[str(i)]:
                shet_sv+=1
                break
        if shet_sv == 0:
            return 'свой набор'
        else:
            a+=1
            shet_sv=0
    else:
        a+=1

    for key, value in slov_kat.items():
        if status_sv:
            shet_kat+=1
            break
        if key != 'Свой набор':
            if slov_kat[key]:
                shet_kat+=1
                break
    if shet_kat>0:
        a+=1
    else:
        return 'категории'

    if a == 5:
        return True
    return False

def db_word():
    user_data_for_session = user_data.get(session['session_id'], {})
    words_ret = []
    if user_data_for_session['Категория']['Свой набор']['Статус']:
        for i in range(1, 301):
            if user_data_for_session['Категория']['Свой набор']['Слова'][str(i)]:
                words_ret.append(user_data_for_session['Категория']['Свой набор']['Слова'][str(i)])
    for key, value in user_data_for_session['Категория'].items():
        if key == 'Свой набор':
            break
        elif user_data_for_session['Категория'][key]:
            for key_1, value_1 in words_igr[key].items():
                words_ret.append(value_1)
    return words_ret

def team_vivod():
    user_data_for_session = user_data.get(session['session_id'], {})
    slov = user_data_for_session["Команды"]
    result = []
    for key, value in slov.items():
        if slov[key]['Статус']:
            result.append(slov[key]['Название'])
    return result

@app.route('/', methods=['GET'])
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
                        "14": '',
                        "15": '',
                        "16": '',
                        "17": '',
                        "18": '',
                        "19": '',
                        "20": '',
                        "21": '',
                        "22": '',
                        "23": '',
                        "24": '',
                        "25": '',
                        "26": '',
                        "27": '',
                        "28": '',
                        "29": '',
                        "30": '',
                        "31": '',
                        "32": '',
                        "33": '',
                        "34": '',
                        "35": '',
                        "36": '',
                        "37": '',
                        "38": '',
                        "39": '',
                        "40": '',
                        "41": '',
                        "42": '',
                        "43": '',
                        "44": '',
                        "45": '',
                        "46": '',
                        "47": '',
                        "48": '',
                        "49": '',
                        "50": '',
                        "51": '',
                        "52": '',
                        "53": '',
                        "54": '',
                        "55": '',
                        "56": '',
                        "57": '',
                        "58": '',
                        "59": '',
                        "60": '',
                        "61": '',
                        "62": '',
                        "63": '',
                        "64": '',
                        "65": '',
                        "66": '',
                        "67": '',
                        "68": '',
                        "69": '',
                        "70": '',
                        "71": '',
                        "72": '',
                        "73": '',
                        "74": '',
                        "75": '',
                        "76": '',
                        "77": '',
                        "78": '',
                        "79": '',
                        "80": '',
                        "81": '',
                        "82": '',
                        "83": '',
                        "84": '',
                        "85": '',
                        "86": '',
                        "87": '',
                        "88": '',
                        "89": '',
                        "90": '',
                        "91": '',
                        "92": '',
                        "93": '',
                        "94": '',
                        "95": '',
                        "96": '',
                        "97": '',
                        "98": '',
                        "99": '',
                        "100": '',
                        "101": '',
                        "102": '',
                        "103": '',
                        "104": '',
                        "105": '',
                        "106": '',
                        "107": '',
                        "108": '',
                        "109": '',
                        "110": '',
                        "111": '',
                        "112": '',
                        "113": '',
                        "114": '',
                        "115": '',
                        "116": '',
                        "117": '',
                        "118": '',
                        "119": '',
                        "120": '',
                        "121": '',
                        "122": '',
                        "123": '',
                        "124": '',
                        "125": '',
                        "126": '',
                        "127": '',
                        "128": '',
                        "129": '',
                        "130": '',
                        "131": '',
                        "132": '',
                        "133": '',
                        "134": '',
                        "135": '',
                        "136": '',
                        "137": '',
                        "138": '',
                        "139": '',
                        "140": '',
                        "141": '',
                        "142": '',
                        "143": '',
                        "144": '',
                        "145": '',
                        "146": '',
                        "147": '',
                        "148": '',
                        "149": '',
                        "150": '',
                        "151": '',
                        "152": '',
                        "153": '',
                        "154": '',
                        "155": '',
                        "156": '',
                        "157": '',
                        "158": '',
                        "159": '',
                        "160": '',
                        "161": '',
                        "162": '',
                        "163": '',
                        "164": '',
                        "165": '',
                        "166": '',
                        "167": '',
                        "168": '',
                        "169": '',
                        "170": '',
                        "171": '',
                        "172": '',
                        "173": '',
                        "174": '',
                        "175": '',
                        "176": '',
                        "177": '',
                        "178": '',
                        "179": '',
                        "180": '',
                        "181": '',
                        "182": '',
                        "183": '',
                        "184": '',
                        "185": '',
                        "186": '',
                        "187": '',
                        "188": '',
                        "189": '',
                        "190": '',
                        "191": '',
                        "192": '',
                        "193": '',
                        "194": '',
                        "195": '',
                        "196": '',
                        "197": '',
                        "198": '',
                        "199": '',
                        "200": '',
                        "201": '',
                        "202": '',
                        "203": '',
                        "204": '',
                        "205": '',
                        "206": '',
                        "207": '',
                        "208": '',
                        "209": '',
                        "210": '',
                        "211": '',
                        "212": '',
                        "213": '',
                        "214": '',
                        "215": '',
                        "216": '',
                        "217": '',
                        "218": '',
                        "219": '',
                        "220": '',
                        "221": '',
                        "222": '',
                        "223": '',
                        "224": '',
                        "225": '',
                        "226": '',
                        "227": '',
                        "228": '',
                        "229": '',
                        "230": '',
                        "231": '',
                        "232": '',
                        "233": '',
                        "234": '',
                        "235": '',
                        "236": '',
                        "237": '',
                        "238": '',
                        "239": '',
                        "240": '',
                        "241": '',
                        "242": '',
                        "243": '',
                        "244": '',
                        "245": '',
                        "246": '',
                        "247": '',
                        "248": '',
                        "249": '',
                        "250": '',
                        "251": '',
                        "252": '',
                        "253": '',
                        "254": '',
                        "255": '',
                        "256": '',
                        "257": '',
                        "258": '',
                        "259": '',
                        "260": '',
                        "261": '',
                        "262": '',
                        "263": '',
                        "264": '',
                        "265": '',
                        "266": '',
                        "267": '',
                        "268": '',
                        "269": '',
                        "270": '',
                        "271": '',
                        "272": '',
                        "273": '',
                        "274": '',
                        "275": '',
                        "276": '',
                        "277": '',
                        "278": '',
                        "279": '',
                        "280": '',
                        "281": '',
                        "282": '',
                        "283": '',
                        "284": '',
                        "285": '',
                        "286": '',
                        "287": '',
                        "288": '',
                        "289": '',
                        "290": '',
                        "291": '',
                        "292": '',
                        "293": '',
                        "294": '',
                        "295": '',
                        "296": '',
                        "297": '',
                        "298": '',
                        "299": '',
                        "300": ''
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
                    "Название": '',
                    "Баллы": 0
                },
                "2": {
                    "Статус": False,
                    "Название": '',
                    "Баллы": 0
                },
                "3": {
                    "Статус": False,
                    "Название": '',
                    "Баллы": 0
                },
                "4": {
                    "Статус": False,
                    "Название": '',
                    "Баллы": 0
                },
                "5": {
                    "Статус": False,
                    "Название": '',
                    "Баллы": 0
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    return render_template('index_3.html')

@app.route('/save_set_1')
def save_set_1():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    if not user_data_for_session:
        return redirect(url_for("main_str"))
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
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    return render_template('index.html')

@app.route('/save_text_1')
def save_tex_1():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["Базовый набор"] == True:
        user_data_for_session["Категория"]["Базовый набор"]=False
    else:
        user_data_for_session['Категория']["Базовый набор"]=True
    return render_template('index.html')

@app.route('/save_text_2')
def save_text_2():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["IT"] == True:
        user_data_for_session["Категория"]["IT"]=False
    else:
        user_data_for_session['Категория']["IT"]=True
    return render_template('index.html')

@app.route('/save_text_3')
def save_text_3():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["Юриспруденция"] == True:
        user_data_for_session["Категория"]["Юриспруденция"]=False
    else:
        user_data_for_session['Категория']["Юриспруденция"]=True
    return render_template('index.html')

@app.route('/save_text_4')
def save_text_4():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["Новый год"] == True:
        user_data_for_session["Категория"]["Новый год"]=False
    else:
        user_data_for_session['Категория']["Новый год"]=True
    return render_template('index.html')

@app.route('/save_text_5')
def save_text_5():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["Marvel"] == True:
        user_data_for_session["Категория"]["Marvel"]=False
    else:
        user_data_for_session['Категория']["Marvel"]=True
    return render_template('index.html')

@app.route('/save_text_6')
def save_text_6():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["Природа"] == True:
        user_data_for_session["Категория"]["Природа"]=False
    else:
        user_data_for_session['Категория']["Природа"]=True
    return render_template('index.html')

@app.route('/save_text_7')
def save_text_7():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["Еда"] == True:
        user_data_for_session["Категория"]["Еда"]=False
    else:
        user_data_for_session['Категория']["Еда"]=True
    return render_template('index.html')

@app.route('/save_text_8')
def save_text_8():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["Фильмы"] == True:
        user_data_for_session["Категория"]["Фильмы"]=False
    else:
        user_data_for_session['Категория']["Фильмы"]=True
    return render_template('index.html')

@app.route('/save_text_10')
def save_text_10():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if user_data_for_session["Категория"]["Свой набор"]["Статус"] == True:
        user_data_for_session["Категория"]["Свой набор"]["Статус"]=False
    else:
        user_data_for_session['Категория']["Свой набор"]["Статус"]=True
    return render_template('index.html')

@app.route('/save_text_9') ###
def save_text_9():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    return render_template('add_words.html')

wordss = []

@app.route('/add_word', methods=['POST'])
def add_word():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    word = request.json['word']
    print(word)
    words = []
    for i in range(1, 301):
        if not user_data_for_session["Категория"]["Свой набор"]["Слова"][str(i)]:
            user_data_for_session["Категория"]["Свой набор"]["Слова"][str(i)]=word
            break
    for j in range(1, 301):
            if user_data_for_session["Категория"]["Свой набор"]["Слова"][str(j)]:
                a = user_data_for_session["Категория"]["Свой набор"]["Слова"][str(j)]
                words.append(a)
    return jsonify({'words': words})

@app.route('/remove_word', methods=['POST'])
def remove_word():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    word = request.json['word']
    words = []
    for i in range(1, 301):
        if user_data_for_session["Категория"]["Свой набор"]["Слова"][str(i)] == word:
            user_data_for_session["Категория"]["Свой набор"]["Слова"][str(i)]=''
            break
    for j in range(1, 301):
            if user_data_for_session["Категория"]["Свой набор"]["Слова"][str(j)]:
                a = user_data_for_session["Категория"]["Свой набор"]["Слова"][str(j)]
                words.append(a)
    return jsonify({'words': words})

def db_dl():
    user_data_for_session = user_data.get(session['session_id'], {})
    slov_dl = user_data_for_session['Длительность раунда']
    result = ''
    for key, value in slov_dl.items():
        if slov_dl[key]:
            result=int(key)
            break
    return result

def db_och():
    user_data_for_session = user_data.get(session['session_id'], {})
    slov_och = user_data_for_session['Количество очков для победы']
    result = ''
    for key, value in slov_och.items():
        if slov_och[key]:
            result=int(key)
            break
    return result

class Game():
    def __init__(self) -> None:
        self.words = db_word()
        self.dl_raund = db_dl()
        self.och_pob = db_och()
        self.team_1 = team_vivod()    
        self.flag = False

current_word = None
guessed_words = []
start_time = None
time_up = False
guessed_after_time_up = False

@app.route('/game', methods = ['GET', 'POST']) ###
def game():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    if prov_nast() == 'дл раунда':
        return 'Соси дл раунда'
    elif prov_nast() == 'кол-во команд':
        return 'Соси кол-во команд'
    elif prov_nast() == 'кол-во оч':
        return 'Соси кол-во оч'
    elif prov_nast() == 'свой набор':
        return 'Соси, ошибка с категорией Свой набор'
    elif prov_nast() == 'категории':
        return 'Соси, выбери категории'
    elif prov_nast():
        game = Game()
        global start_time, current_word, guessed_words, time_up, guessed_after_time_up  # Используем глобальные переменные
        if request.method == 'POST':
            if start_time is None:  # Игра еще не началась
                return jsonify({'error': 'Игра не началась'})
            if request.form['action'] == 'guess':
                if current_word is None:
                    return jsonify({'error': 'Слово не было загружено'})
                if time_up and guessed_after_time_up:  # Время вышло и кнопка "Отгадал" уже была нажата
                    return jsonify({'error': 'Вы уже нажали кнопку "Отгадал" после истечения времени'})
                if time_up:  # Время вышло
                    guessed_words = []  # Очищаем список угаданных слов
                    time_up = False  # Сбрасываем флаг истечения времени
                    guessed_after_time_up = True  # Устанавливаем флаг нажатия кнопки "Отгадал" после истечения времени
                    start_time = None  # Сбрасываем время начала игры
                else:
                    guessed_words.append(current_word)  # Добавляем текущее слово в список угаданных
                list_length = len(game.words)
                random_index = random.randint(0, list_length - 1)
                new_word = game.words[random_index]
                # new_word = random.choice([w for w in game.words if w not in guessed_words])
                current_word = new_word
                return jsonify({'new_word': new_word, 'team_1': game.team_1, 'guessed_words': guessed_words, 'time_up': time_up, 'guessed_after_time_up': guessed_after_time_up})
            elif request.form['action'] == 'guess_pr':
                if current_word is None:
                    return jsonify({'error': 'Слово не было загружено'})
                if time_up and guessed_after_time_up:  # Время вышло и кнопка "Отгадал" уже была нажата
                    return jsonify({'error': 'Вы уже нажали кнопку "Отгадал" после истечения времени'})
                if time_up:  # Время вышло
                    guessed_words = []  # Очищаем список угаданных слов
                    time_up = False  # Сбрасываем флаг истечения времени
                    guessed_after_time_up = True  # Устанавливаем флаг нажатия кнопки "Отгадал" после истечения времени
                    start_time = None  # Сбрасываем время начала игры
                else:
                    guessed_words.append(current_word)  # Добавляем текущее слово в список угаданных
                list_length = len(game.words)
                random_index = random.randint(0, list_length - 1)
                new_word = game.words[random_index]
                # random.choice([w for w in game.words if w not in guessed_words])
                current_word = new_word
                return jsonify({'new_word': new_word, 'team_1': game.team_1, 'guessed_words': guessed_words, 'time_up': time_up, 'guessed_after_time_up': guessed_after_time_up})        
            else:
                return jsonify({'error': 'Неизвестное действие'})
        else:
            if start_time is None:  # Игра еще не началась
                current_word = random.choice(game.words)
                return render_template('game.html', team_1 = game.team_1, word=current_word, guessed_words=guessed_words, time_up=time_up, guessed_after_time_up=guessed_after_time_up)
            else:  # Игра уже идет
                word = current_word
                return render_template('game.html', team_1 = game.team_1, word=word, start_time=start_time, guessed_words=guessed_words, time_up=time_up, guessed_after_time_up=guessed_after_time_up)
    else:
        return 'Просто соси'

@app.route('/start_game', methods=['POST'])
def start_game():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    game = Game()
    global start_time, current_word, guessed_words, time_up, guessed_after_time_up
    if not guessed_after_time_up:  # Проверяем, что пользователь нажал кнопку "Отгадал" после истечения времени
        start_time = time.time()
        current_word = random.choice(game.words)
        guessed_words = []  # Очищаем список угаданных слов
        time_up = False  # Сбрасываем флаг истечения времени
        guessed_after_time_up = False  # Сбрасываем флаг нажатия кнопки "Отгадал" после истечения времени
        return jsonify({'word': current_word, 'team_1': game.team_1, 'start_time': start_time, 'guessed_words': guessed_words, 'time_up': time_up, 'guessed_after_time_up': guessed_after_time_up})
    else:
        return jsonify({'error': 'Вы должны нажать кнопку "Отгадал" после истечения времени, чтобы начать новую игру'})

@app.route('/name_kom', methods = ['GET', 'POST'])
def name_kom():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    game = Game()
    if request.method == 'POST':
        data = request.get_json()
        teams_1 = data.get('team_1')
        team_new = ''
        chet = data.get('chet')
        for i in range(len(game.team_1) + 1):
            if i == len(game.team_1) - 1:
                team_new = game.team_1[0]
                break
            if game.team_1[i] == teams_1:
                team_new = game.team_1[i+1]
                break
        # print(chet, teams_1, team_new, game.och_pob)
        for key, value in user_data_for_session['Команды'].items():
            if user_data_for_session['Команды'][key]['Название'] == teams_1: 
                user_data_for_session['Команды'][key]['Баллы']+=chet
                if user_data_for_session['Команды'][key]['Баллы'] >= game.och_pob:
                    game.flag = True
                break
        # print(user_data_for_session['Команды'][key]['Название'], teams_1)
        # print(user_data_for_session['Команды'][key]['Баллы'])
        # print(chet)
        # print(type(chet))
        return jsonify({'team_1': team_new, 'red_flag': game.flag})
    return redirect(url_for("main_str"))
 
@app.route('/time_1', methods = ['GET'])
def time_1():
    user_data_for_session = user_data.get(session['session_id'], {})
    if not user_data_for_session:
        return redirect(url_for("main_str"))
    game = Game()
    data = {
        'time_1': game.dl_raund
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
