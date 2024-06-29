# доработать
from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

class WorkDB():
    def __init__(self) -> None:
        pass
    
    # распределитель 
    def main(self, data):
        pass
    
    # добавление записи в бд
    def add_zap(self):
        pass

@app.route("/<input>")
@cross_origin()
def server(input):
    print(input)
    # return main(input)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)