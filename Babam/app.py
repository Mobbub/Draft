from flask import Flask, request, render_template, jsonify, redirect, session, url_for
from werkzeug.utils import secure_filename

import os, uuid, datetime, random

import db
import bus_logic

# Путь сохрания бд
UPLOAD_FOLDER = 'static/db'
# Расширения бд, которые разрешено загружать
ALLOWED_EXTENSIONS = {'db', 'json', 'csv', 'sql'}

app = Flask(__name__)

# Настройки конфига сайта
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.permanent_session_lifetime = datetime.timedelta(days=31)

class Working_files():
    def __init__(self) -> None:
        self.list_type = ['png', 'jpeg', 'jpg', 'pdf']
        
    def names_files_folder(self):
        folder_path = "static/image_analysis/first_image"

        file_list = []

        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                file_list.append(filename)
        return file_list
        
    def check_file(self, file_name, file_type):
        if file_name == '':
            return {
                'status': 1,
                'message': 'Нет файла'
            }

        if file_type not in self.list_type:
            return {
                'status': 2,
                'message': 'Ошибка формата'
            }
            
        return {'status': 200}

# Мэин роут с главной страницей работы
@app.route('/')
@app.route('/main')
def main():
    if 'Login' not in session: #or not session['Login']:
        return redirect(url_for("authorization"))
    return render_template('admin.html')

# Роут авторизации
@app.route('/authorization')
def authorization():
    session.permanent = True
    if 'Login' not in session:
        session['Login'] = ''
        session['Password'] = ''
        session['DB'] = ''
        session.modified = True
    return render_template('index.html')

### доработать авторизацию, добавить jwt токен и через какую то почту подтверждение
# Роут принимающий пост запросы для авторизации
@app.route('/log', methods=['POST'])
def log():
    if 'Login' not in session:
        return jsonify({'НЕ ГУД'}) ###
    
    if request.method == 'POST': ###
        login = request.json['login']
        password = request.json['password']
        # if db.EmployeesDatabase.authenticate_user(login, password):
        #     session.permanent = True
        #     session['Login'] = login
        #     session['Password'] = password
        #     session.modified = True
        #     return jsonify({'status': 200})
        return jsonify({'status': 200}) # статус 0 верхнюю функцию раскоментить, когда бд подключим фул
    
# Роут для выхода с аккаунта, очищается сессия
@app.route('/exit', methods=['POST'])
def exit():
    index_action = request.json['index_action']
    
    if index_action == -1:
        session.permanent = True
        session['Login'] = ''
        session['Password'] = ''
        session.modified = True
        return jsonify({
            'status': 200,
            'message': 'Успешный выход'
        })

    return jsonify({
        'status': 0,
        'message': 'Произошла ошибка'
    })
    
def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
### доделать добавление в сессию файла
@app.route('/up_db', methods=['POST'])
def up_db():
    if 'Login' not in session:
        return jsonify({'message': 'НЕ ГУД 1 '}) ###
    
    if 'file' not in request.files:
        return jsonify({'message': 'НЕ ГУД 2'}) ### сообщение об ошибке надо сделать

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message': 'НЕ ГУД 3'}) ### сообщение об ошибке надо сделать
    
    if file:
        if allowed_file(file.filename) == False:
            return jsonify({'message': 'НЕ ГУД4 '})
        else:    
            filename = secure_filename(file.filename)
            
            ### надо добавить провреку имени и генерации нового, если файл с таким именем уже есть
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['DB'] = file.filename
            
            
            return jsonify(bus_logic.general_Statistics(db.ClientsDatabase.fetch_data_from_file(f'static/db/{session["DB"]}'))) ### сообщение о том, что всё успешно загрузилось
    else:
        return jsonify({'message': 'НЕ ГУД'})

if __name__ == '__main__':
    app.run(debug=True)