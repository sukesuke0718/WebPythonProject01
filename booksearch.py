from flask import Flask
from flask import request
from flask  import render_template

myapp = Flask(__name__)

@myapp.route('/booksearch', methods = ['GET'])
def booksearch():
    title = request.args.get('title')
    author = request.args.get('author')
    return '{1}さんの本「{0}」ですね。お探しします'.format(title,author)

@myapp.route('/searchform')
def searchform():
    # テンプレートを読み込む
    renderpage = render_template("searchform.html")
    return renderpage

@myapp.route('/result', methods=['POST'])
def show_result():
    # フォームで入力された文字を取得する
    title = request.form['title']
    author = request.form['author']
    the_result = '<p>{1}さんの本「{0}」ですね。お探しします</p>'.format(title,author)
    link_back = '<p><a href = "/searchform">検索ページへ</a></p>'
    return the_result + link_back
