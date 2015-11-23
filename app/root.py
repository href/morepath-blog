from app import App

@App.path(path='')
class Root(object):
    def __init__(self):
      self.name = 'Flemming Hansen'

@App.html(model=Root, template='root.pt')
def root_default(self, request):
    return {'name': self.name}
