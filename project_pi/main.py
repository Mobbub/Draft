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

@app.route('/save_text', methods=['POST'])
def save_text():
    text=request.form['text']
    with open('session.json', 'r', encoding='utf-8') as f:
            data=json.load(f)
    if text == 'Свой набор':
        pass
    else:
        data['Категория']=text
    with open('session.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    return 'Соси'

if __name__ == '__main__':
    app.run(debug=True)
