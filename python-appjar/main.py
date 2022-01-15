from appJar import gui

def inputMath(value=""):
    old_value=str(app.getEntry('math'))
    app.setEntry('math',old_value+str(value))

def submitMath(option):
    if option == '=':
        math=app.getEntry('math').replace('x','*').replace('^','**').replace(',','.')
        cal=eval(math)
        app.setEntry('math',str(cal).replace('.',','))
    if option == 'C':
        app.clearEntry('math')
    if option == '<':
        value =list(app.getEntry('math'))
        value.pop()
        value = ''.join([x for x in value])
        app.setEntry('math',str(value))

app=gui('Calculadora','400x500')
app.setFont(20)
app.addEntry("math",rowspan=1)
app.addButtons([[0,1,2,3,4,5,6,7,8,9],['+','-','x','/','^','(',')',',']],inputMath, rowspan=1, colspan=1)
app.addButtons(['=','<','C'],submitMath)
app.go()