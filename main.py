from bottle import Bottle,run, route, template, static_file


# Route to serve static files like images, CSS, etc.
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@route('/')
def index():
    return template('index')


#main code
run(reloader=True)