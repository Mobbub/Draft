from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# Список слов для игры
words = ["программирование", "компьютер", "алгоритм", "база данных", "Python", "Flask", "HTML", "CSS", "JavaScript"]

# Глобальная переменная для хранения времени начала игры
start_time = None

time_1 = 30
# Глобальная переменная для хранения текущего слова
current_word = None

# Список угаданных слов
guessed_words = []

# Глобальная переменная для отслеживания истечения времени
time_up = False

# Глобальная переменная для отслеживания нажатия кнопки "Отгадал" после истечения времени
guessed_after_time_up = False

team_1 = ['Команда ХУУУУУУУУУУУУУУУУУУУУЙ', 'teammmmm 2', 'teaaaaaam 3']

class Game:
    def __init__(self):
        self.words = ["программирование", "компьютер", "алгоритм", "база данных", "Python", "Flask", "HTML", "CSS", "JavaScript"]
        self.time_limit = 30
        self.team_1 = ['Команда ХУУУУУУУУУУУУУУУУУУУУЙ', 'teammmmm 2', 'teaaaaaam 3']
        self.current_word = None
        self.guessed_words = []
        self.time_up = False
        self.guessed_after_time_up = False
        self.time_left = 30
        
    def start_game(self):
        self.current_word = random.choice(self.words)
        self.start_time = time.time()

    def check_time_up(self):
        if self.start_time is not None and time.time() - self.start_time >= self.time_limit:
            self.time_up = True

    def handle_guess(self):
        self.check_time_up()

        if self.time_up and self.guessed_after_time_up:
            return {'error': 'Вы уже нажали кнопку "Отгадал" после истечения времени'}

        if self.time_up:
            self.guessed_words = []
            self.time_up = False
            self.guessed_after_time_up = True
            self.start_time = None
        else:
            self.guessed_words.append(self.current_word)

        new_word = random.choice([w for w in self.words if w not in self.guessed_words])
        self.current_word = new_word
        return {'new_word': new_word, 'team_1': self.team_1, 'guessed_words': self.guessed_words, 'time_up': self.time_up, 'guessed_after_time_up': self.guessed_after_time_up}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game_route():
    game = Game()

    if request.method == 'POST':
        if not game.start_time:
            return jsonify({'error': 'Игра не началась'})

        if request.form['action'] == 'guess' or request.form['action'] == 'guess_pr':
            return jsonify(game.handle_guess())
        else:
            return jsonify({'error': 'Неизвестное действие'})
    else:
        if not game.start_time:
            game.start_game()

        return render_template('game.html', team_1=game.team_1, word=game.current_word, guessed_words=game.guessed_words, time_up=game.time_up, guessed_after_time_up=game.guessed_after_time_up)

@app.route('/start_game', methods=['POST'])
def start_game():
    game_state = Game()
    if not game_state.guessed_after_time_up:
        game_state.start_time = time.time()
        game_state.current_word = random.choice(words)
        game_state.guessed_words = []
        game_state.time_up = False
        game_state.guessed_after_time_up = False
        return jsonify({'word': game_state.current_word, 'team_1': game_state.team_1, 'start_time': game_state.start_time, 'guessed_words': game_state.guessed_words, 'time_up': game_state.time_up, 'guessed_after_time_up': game_state.guessed_after_time_up})
    else:
        return jsonify({'error': 'Вы должны нажать кнопку "Отгадал" после истечения времени, чтобы начать новую игру'})

@app.route('/name_kom', methods=['POST'])
def name_kom():
    data = request.get_json()
    teams_1 = data.get('team_1')
    chet = data.get('chet')
    game_state = Game()
    team_new = ''
    for i in range(len(game_state.team_1) + 1):
        if i == len(game_state.team_1) - 1:
            team_new = game_state.team_1[0]
            break
        if game_state.team_1[i] == teams_1:
            team_new = game_state.team_1[i+1]
            break
    print(teams_1, chet)
    return jsonify({'team_1': team_new})

@app.route('/time_1', methods=['GET'])
def time_1():
    game_state = Game()
    data = {
        'time_1': game_state.time_left
    }
    return jsonify(data)
    
# @app.route('/game_save', methods=['POST'])
# def game_save():
#     game_1 = request.form['words_kom_1']
#     words_kam = request.form['komanda']
#     # for key, value in rah
# # game_1 = {'Слова': {'word_1': 1, 'word_2': 1, 'word_3': 1, 'word_4': 1, 'word_5': 1}}
# # words_kam = 'Название команды' 

if __name__ == '__main__':
    app.run(debug=True)