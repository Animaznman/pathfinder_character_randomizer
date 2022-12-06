from pywebio.output import *
from pywebio.input import *
from pywebio.pin import *

commands = []

def run_this():
    with use_scope('this_scope', clear = True):
        put_text("This ran???")
        pin_update('updater', value = 'Non-default value')
        # commands.append(changed)
        commands.append(pin_wait_change('updater', 'Ancestry'))
        put_code(commands)


def run_that():
    with use_scope('this_scope', clear = True):
        put_text("This other thing ran")
        pin_update('updater', value = 'Other non-default value')
        # commands.append(changed)
        commands.append(pin_wait_change('updater', 'Ancestry'))
        put_code(commands)


# put_buttons([dict(label = 'Press A', value = 'a', color = 'primary'),
# dict(label = 'Press B', value = 'b', color = 'secondary')],
# onclick = [run_that, run_this])


# onclick = run_this)
put_select(label = 'Ancestry', name = 'Ancestry', options = ['Blarg', 'Blurg', 'Blorg'])
put_input(label = 'Update Me', name = 'updater', value = 'Default Value')
while True:
    commands.append(pin_wait_change('updater','Ancestry'))
    with use_scope('this_scope', clear = True):
            put_code(commands)
