class Man:
    def __init__(self,name):
        self.name = name
        print('init')

    def hello(self):
        print('hello ' + self.name)

    def goodbye(self):
        print('goodbye ' + self.name)

m = Man('dggoo')
m.hello()
m.goodbye()
#init
#hello dggoo
#goodbye dggoo
