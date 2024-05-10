
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def main_str():
    return render_template('main_str.html')

@app.route('/next')
def index2():
    return render_template('index2.html')

@app.route('/save')
def save():
    return render_template('index.html')

@app.route('/save_text_1')
def save_tex_1t():
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

@app.route('/save_text_9') ###
def save_text_9():
    with open('session.json', 'r', encoding='utf-8') as f:
            data=json.load(f)
    if data["Категория"]["Свой выбор"]["Статус"] == True:
        data["Категория"]["Свой выбор"]["Статус"]=False
    else:
        data['Категория']["Свой выбор"]["Статус"]=True
    with open('session.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html')

@app.route('/game') ###
def game():
    return 'Соси'

if __name__ == '__main__':
    app.run(debug=True)
