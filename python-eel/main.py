import eel

eel.init('web')

@eel.expose
def calc(num):
    return eval(num.replace('x','*').replace('^','**').replace(',','.'))


eel.start('index.html',size=(600,600))