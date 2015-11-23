import morepath
from more.chameleon import ChameleonApp

class App(ChameleonApp):
    pass

@App.template_directory()
def get_template_directory():
    return 'templates'

@App.setting_section(section='chameleon')
def get_setting_section():
    return {'debug': True}
