from bottle import get, post, request, run

drawform = '''
        <h2>どのボトルをお探しですか</h2>
        <form action="bottlesearch" method="post">
            <p>Brand:<input type="text" name="brand"/></p>
            <p>Since:<input type="text" name="since"/></p>
            <p><input value="Search" type="submit"/></p>
        </form>
    '''

@get('/bottlesearch')
def search():
    return drawform

# postメソッドでアクセスされたとき実行
@post('/bottlesearch')
def result():
    brand = request.forms.brand
    since = request.forms.since
    result = ('<p>{0}の{1}年のものですね。お探しします。<p>').format(brand,since)
    return drawform + result

run(host="localhost", port= 8080)

