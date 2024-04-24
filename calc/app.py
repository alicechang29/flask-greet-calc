from flask import Flask
from flask import request
# from operations import add, sub, mult, div
# from operations import sub
# from operations import mult
# from operations import div
import operations

OPERATIONS = {
    "add": operations.add,
    "sub": operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

app = Flask(__name__)

@app.get('/add')
def add_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operations.add(a, b)}"

@app.get('/sub')
def sub_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operations.sub(a, b)}"

@app.get('/mult')
def mult_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operations.mult(a, b)}"

@app.get('/div')
def div_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operations.div(a, b)}"

@app.get('/math/<operation>')
def get_operation(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    # if(operation == 'add'):
    #     return f"{operations.add(a, b)}"


    return f"{OPERATIONS[operation](a, b)}"