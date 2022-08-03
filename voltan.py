from bottle import route, run, template, static_file
import bottle
bottle.TEMPLATES.clear()
@route('/hello')
def hello():
    return "Hello World!"


@route('/')
def mainPage():
    bottle.TEMPLATE_PATH.insert(0, 'C:/Users/hitpa/Desktop/views')
    return template('index'), template('menu_style')

@route('/chapters.html')
def mainPage():
    bottle.TEMPLATE_PATH.insert(0, 'C:/Users/hitpa/Desktop/views')
    return template('chapters'), template('chapters_style')
run(host='localhost', port=8080, debug=True)