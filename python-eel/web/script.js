
let math = document.querySelector('#output')

function buttonAdd(event){
    let result = math.value + (event.target.value)
    return math.value=result
}

function buttonRemove(event){
    let list = math.value.split('')
    list.pop()
    list = list.join('')
    console.log(list)
    return math.value=list
}

function buttonClear(event){
    return math.value=''
}
/*
function buttonResult(event){
    let cal = eval(math.value.replace('x','*').replace('^','**').replace(',','.'))
    return math.value = cal
}
*/

async function buttonResult(){
    let cal = await eel.calc(math.value)();
    return math.value = cal
}