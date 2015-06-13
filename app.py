from bottle import request, get, post, view, redirect
from pypograph import Typograph
import os

typograph = Typograph()
BASE_DIR = os.path.dirname(__file__)


@get('/')
@view('index')
def index_page():
    pass


@post('/process')
def process_page():
    form = request.forms.decode()
    return typograph.typo(form['text'])


if __name__ == '__main__':
    from bottle import run, static_file

    @get('/static/<filename>')
    def static_server(filename):
        return static_file(filename, root=os.path.join(BASE_DIR, 'static'))

    try:
        run(host='localhost', port=8000, reloader=True)
    except KeyboardInterrupt:
        print('Exiting')
