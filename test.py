from pywebio.output import *
from pywebio.input import *
from pywebio.pin import *

def func_1():
    put_text("func_1 reached")
def func_2():
    put_text("func_2 reached")
def func_3():
    put_text("func_3 reached")
def func_4():
    put_text("func_4 reached")

with use_scope('button_scope', clear = True):
        put_buttons([
            dict(label = 'Func 1', value = None, color = 'primary'),
            dict(label = 'Func 2', value = None, color = 'secondary'),
            dict(label = 'Func 3', value = None, color = 'warning'),
            dict(label = 'Func 4', value = None, color = 'danger')
        ],
        onclick = [func_1, func_2, func_3, func_4])
