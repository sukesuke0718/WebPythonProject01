###########################################
# PythonでWebアプリケーションを作ってみよう
# Flaskを使ってみる
###########################################
from flask import Flask

myapp = Flask(__name__)

@myapp.route('/')
def index():
    return '''
    <h2>Flaskの練習ページです</h2>
    <p><a href="/hello">Helloページへ</a></p>
    '''

@myapp.route('/hello')
def hello():
    return 'こんにちは'

@myapp.route('/item/<int:item_id>')
def select_item(item_id):
    items = [('コーヒー',300),('紅茶',300),('ジュース',280),('牛乳',250),('ウーロン茶', 220)]
    item = items[item_id]
    return '{0}は{1}円です'.format(item[0],item[1])
