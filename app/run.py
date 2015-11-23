import morepath
import waitress
from werkzeug.serving import run_simple

import app, root

def prod():
    morepath.autosetup()
    waitress.serve(app.App())

def dev():
    config = morepath.setup()
    config.scan(app)
    config.scan(root)
    config.commit()

    run_simple('localhost', 8080, app.App(), use_reloader=True, use_debugger=True)

if __name__ == '__main__':
    dev()