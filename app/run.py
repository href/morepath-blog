import morepath
import waitress
from werkzeug.serving import run_simple

import main
# import root

def prod():
    morepath.autosetup()
    waitress.serve(main.App())

def dev():
    config = morepath.setup()
    config.scan(main)
    # config.scan(root)
    config.commit()

    run_simple('localhost', 8080, main.App(), use_reloader=True, use_debugger=True)

if __name__ == '__main__':
    dev()