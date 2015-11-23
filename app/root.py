from app import App

class Root(object):
    def __init__(self):
      self.name = 'Flemming'

root = Root()

@App.view(model=Root)
def hello_world(self, request):
    return "Hello %s!" % root.name
