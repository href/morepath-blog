import morepath
import waitress
from werkzeug.serving import run_simple

from app import app

def prod():
    morepath.autosetup()
    waitress.serve(app.App())

def dev():
    morepath.autosetup()
    run_simple('localhost', 8080, app.App(), use_reloader=True, use_debugger=True)

if __name__ == '__main__':
    dev()