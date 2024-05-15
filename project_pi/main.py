from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def main_str():
    return render_template('main_str.html')

@app.route('/next')
def index2():
    return render_template('index2.html')

@app.route('/setings')
def set():
    return render_template('index_3.html')

@app.route('/save_set_1')
def save_set_1():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Длительность раунда"]["30"] == False:
        data["Длительность раунда"]["30"]=True
    else:
        data["Длительность раунда"]["30"]=False
    data["Длительность раунда"]["40"]=False
    data["Длительность раунда"]["50"]=False
    data["Длительность раунда"]["60"]=False
    data["Длительность раунда"]["120"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')

@app.route('/save_set_2')
def save_set_2():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Длительность раунда"]["40"] == False:
        data["Длительность раунда"]["40"]=True
    else:
        data["Длительность раунда"]["40"]=False
    data["Длительность раунда"]["30"]=False
    data["Длительность раунда"]["50"]=False
    data["Длительность раунда"]["60"]=False
    data["Длительность раунда"]["120"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')

@app.route('/save_set_3')
def save_set_3():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Длительность раунда"]["50"] == False:
        data["Длительность раунда"]["50"]=True
    else:
        data["Длительность раунда"]["50"]=False
    data["Длительность раунда"]["40"]=False
    data["Длительность раунда"]["30"]=False
    data["Длительность раунда"]["60"]=False
    data["Длительность раунда"]["120"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')

@app.route('/save_set_4')
def save_set_4():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Длительность раунда"]["60"] == False:
        data["Длительность раунда"]["60"]=True
    else:
        data["Длительность раунда"]["60"]=False
    data["Длительность раунда"]["40"]=False
    data["Длительность раунда"]["50"]=False
    data["Длительность раунда"]["30"]=False
    data["Длительность раунда"]["120"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')

@app.route('/save_set_5')
def save_set_5():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Длительность раунда"]["120"] == False:
        data["Длительность раунда"]["120"]=True
    else:
        data["Длительность раунда"]["120"]=False
    data["Длительность раунда"]["40"]=False
    data["Длительность раунда"]["50"]=False
    data["Длительность раунда"]["60"]=False
    data["Длительность раунда"]["30"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')

@app.route('/save_set_6')
def save_set_6():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Количество очков для победы"]["20"] == False:
        data["Количество очков для победы"]["20"]=True
    else:
        data["Количество очков для победы"]["20"]=False
    data["Количество очков для победы"]["30"]=False
    data["Количество очков для победы"]["50"]=False
    data["Количество очков для победы"]["60"]=False
    data["Количество очков для победы"]["80"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')

@app.route('/save_set_7')
def save_set_7():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Количество очков для победы"]["30"] == False:
        data["Количество очков для победы"]["30"]=True
    else:
        data["Количество очков для победы"]["30"]=False
    data["Количество очков для победы"]["20"]=False
    data["Количество очков для победы"]["50"]=False
    data["Количество очков для победы"]["60"]=False
    data["Количество очков для победы"]["80"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')


@app.route('/save_set_8')
def save_set_8():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Количество очков для победы"]["50"] == False:
        data["Количество очков для победы"]["50"]=True
    else:
        data["Количество очков для победы"]["50"]=False
    data["Количество очков для победы"]["30"]=False
    data["Количество очков для победы"]["20"]=False
    data["Количество очков для победы"]["60"]=False
    data["Количество очков для победы"]["80"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')


@app.route('/save_set_9')
def save_set_9():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Количество очков для победы"]["60"] == False:
        data["Количество очков для победы"]["60"]=True
    else:
        data["Количество очков для победы"]["60"]=False
    data["Количество очков для победы"]["30"]=False
    data["Количество очков для победы"]["50"]=False
    data["Количество очков для победы"]["20"]=False
    data["Количество очков для победы"]["80"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')

@app.route('/save_set_10')
def save_set_10():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Количество очков для победы"]["80"] == False:
        data["Количество очков для победы"]["80"]=True
    else:
        data["Количество очков для победы"]["80"]=False
    data["Количество очков для победы"]["30"]=False
    data["Количество очков для победы"]["50"]=False
    data["Количество очков для победы"]["60"]=False
    data["Количество очков для победы"]["20"]=False
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index_3.html')

@app.route('/save')
def save():
    return render_template('index.html')

@app.route('/save_text_1')
def save_tex_1():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["Базовый набор"] == True:
        data["Категория"]["Базовый набор"]=False
    else:
        data['Категория']["Базовый набор"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_2')
def save_text_2():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["IT"] == True:
        data["Категория"]["IT"]=False
    else:
        data['Категория']["IT"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_3')
def save_text_3():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["Юриспруденция"] == True:
        data["Категория"]["Юриспруденция"]=False
    else:
        data['Категория']["Юриспруденция"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_4')
def save_text_4():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["Новый год"] == True:
        data["Категория"]["Новый год"]=False
    else:
        data['Категория']["Новый год"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_5')
def save_text_5():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["Marvel"] == True:
        data["Категория"]["Marvel"]=False
    else:
        data['Категория']["Marvel"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_6')
def save_text_6():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["Природа"] == True:
        data["Категория"]["Природа"]=False
    else:
        data['Категория']["Природа"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_7')
def save_text_7():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["Еда"] == True:
        data["Категория"]["Еда"]=False
    else:
        data['Категория']["Еда"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_8')
def save_text_8():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["Фильмы"] == True:
        data["Категория"]["Фильмы"]=False
    else:
        data['Категория']["Фильмы"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_10')
def save_text_10():
    with open('session.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
    if data["Категория"]["Свой набор"]["Статус"] == True:
        data["Категория"]["Свой набор"]["Статус"]=False
    else:
        data['Категория']["Свой набор"]["Статус"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/save_text_9', methods=['GET', 'POST']) ###
def save_text_9():
    words=[]
    if request.method == 'POST':
        new_word = request.form['new_word']
        with open('session.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        for i in range(15):
            if not data["Категория"]["Свой набор"]["Слова"][str(i)]:
                data["Категория"]["Свой набор"]["Слова"][str(i)]=new_word
                break
        for j in range(1, 15):
            if data["Категория"]["Свой набор"]["Слова"][str(i)]:
                words.append(data["Категория"]["Свой набор"]["Слова"][str(j)])
        with open('session.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('add_words.html', words=words)

@app.route('/game') ###
def game():
    return 'Соси'

if __name__ == '__main__':
    app.run(debug=True)
