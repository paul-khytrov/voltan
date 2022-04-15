from bottle import route, run, template, static_file
import bottle

@route('/hello')
def hello():
    return "Hello World!"


@route('/')
def mainPage():
    bottle.TEMPLATE_PATH.insert(0, 'C:/Users/hitpa/Desktop/views')
    return template('index'), template('style')
run(host='localhost', port=8080, debug=True)