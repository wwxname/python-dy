# coding=utf-8
from flask import Flask



app = Flask(__name__)



@app.route('/')
def hello_word():
    return 'hello world'


if __name__ == '__main__':
    dict = app.config.items()
    for key in dict:
        print(key)

    #app.run(host='127.0.0.1', port=8080)
