import character as char
import requests
from pywebio.output import *
from pywebio.input import *
from pywebio.pin import *
from pywebio.platform import config
import pandas as pd

priors = {}

@config(theme="dark")
def main():

    character = char.Character('') # Initialize empty character object
    # character.generate_character()
    # print(character.ancestry+" "+character.background+" "+character.job)
    # print(character.colors_data)

    # Update character options references
    # update_character_options()

    # Handling actual html output
    html_output(character)




# def html_output(character):
#     with use_scope('scope1', clear = True):
#         put_text('Pathfinder 2e Character Generator')
#         data = input_group("Preset Character Information",[
#             actions(buttons = [
#                 {'label': 'Generate character', 'value': 'generate_character'},
#                 {'label': 'Generate character with priors', 'value': 'generate_character_with_priors', 'color': 'secondary'},
#                 {'label': 'Clear Form', 'value' : 'reset', 'type': 'reset', 'color': 'warning'},
#                 {'label': 'Cancel', 'type': 'cancel', 'color': 'danger'},
#                 ],
#             name = 'top_options'
#             ),
#             input('Name', name = 'name', type = TEXT, value = character.name),
#             select('Ancestry', name = 'Ancestry', options = char.ancestries, value = character.ancestry),
#             select('Background', name = 'Background', options = char.backgrounds, value = character.background),
#             select('Class', name = 'Class', options = char.classes, value = character.job),
#             radio('Gender', name = 'Gender', options = char.genders, value = character.gender),
#             input('Age', name = 'Age', type = NUMBER, value = character.age),
#             select('Alignment', name = 'Alignment', options = char.flattened_alignments, value = character.alignment),
#             slider('Height (in centimeters)', name = 'Height', min_value = 10, max_value = 400, value = character.height),
#             slider('Weight (in pounds)', name = 'Weight', min_value = 1, max_value = 600, value = character.weight),
#             input('Primary Color', name = 'color_1', type = 'color', value = character.colors_data[0]),
#             input('Secondary Color', name = 'color_2', type = 'color', value = character.colors_data[1]),
#             input('Tertiary Color', name = 'color_3', type = 'color', value = character.colors_data[2]),
#             actions(buttons = [
#                 {'label': 'Print Character to csv', 'value': 'print_character', 'type': 'submit', 'color': 'success'}
#                 ], name = 'print'
#             )
#         ])

    # elif data['top_options'] ==

def gen_char(character):
    character.generate_character()
    pin_update('Age', value = character.age)
    pin_update('Gender', value = character.gender)
    pin_update('Ancestry', value = character.ancestry)
    pin_update('Background', value = character.background)
    pin_update('Class', value = character.job)
    pin_update('Alignment', value = character.alignment)
    pin_update('Height', value = character.height)
    pin_update('Weight', value = character.weight)
    pin_update('color_1', value = character.colors_data[0])
    pin_update('color_2', value = character.colors_data[1])
    pin_update('color_3', value = character.colors_data[2])

def gen_char_pri(character):
    # Run generate_character_with_priors function that is yet to be designed

def clear_form()

def html_output(character):

    with use_scope('button_scope', clear = True):
        put_buttons([
            dict(label = 'Generate Character', value = character, color = 'primary'),
            dict(label = 'Generate Character with Priors', value = character, color = 'secondary'),
            dict(label = 'Clear Form', value = character, color = 'warning'),
            dict(label = 'Cancel', value = character, color = 'danger')
        ],
        onclick = gen_char)
    with use_scope('scope1', clear = True):
        put_text('Pathfinder 2e Character Generator')
        # options = put_actions(buttons = [
        #         {'label': 'Generate character', 'value': 'generate_character'},
        #         {'label': 'Generate character with priors', 'value': 'generate_character_with_priors', 'color': 'secondary'},
        #         {'label': 'Clear Form', 'value' : 'reset', 'color': 'warning'},
        #         {'label': 'Cancel', 'value' : 'cancel', 'color': 'danger'},
        #         ],
        #     name = 'options'
        # )
        put_table([[put_text("Character Information")],
            [
                put_input(label = 'Name', name = 'Name', type = TEXT, value = character.name),
                put_input(label = 'Age', name = 'Age', type = NUMBER, value = character.age),
                put_radio(label = 'Gender', name = 'Gender', options = char.genders, value = character.gender)
            ],
            [
                put_select(label = 'Ancestry', name = 'Ancestry', options = char.ancestries, value = character.ancestry),
                put_select(label = 'Background', name = 'Background', options = char.backgrounds, value = character.background),
                put_select(label = 'Class', name = 'Class', options = char.classes, value = character.job),
            ],
            [
                put_select(label = 'Alignment', name = 'Alignment', options = char.flattened_alignments, value = character.alignment),
                put_slider(label = 'Height (in centimeters)', name = 'Height', min_value = 10, max_value = 400, value = character.height),
                put_slider(label = 'Weight (in pounds)', name = 'Weight', min_value = 1, max_value = 600, value = character.weight),
            ],
            [
                put_input(label = 'Primary Color', name = 'color_1', type = 'color', value = character.colors_data[0]),
                put_input(label = 'Secondary Color', name = 'color_2', type = 'color', value = character.colors_data[1]),
                put_input(label = 'Tertiary Color', name = 'color_3', type = 'color', value = character.colors_data[2]),
            ]
        ])

def update_character_options():

    api_key = 'da468b89-2bf8-4e2b-a939-79c6e6ef25ce'
    header = {"Authorization": api_key}
    r = requests.get('https://api.pathfinder2.fr/v1/pf2', headers = header)
    print(r.status_code)

    # Update list of ancestries
    ancestries = requests.get('https://api.pathfinder2.fr/v1/pf2/ancestry', headers = header)
    ancestry_list = []
    for result in ancestries.json()['results']:
        ancestry_list.append(result['name'])
    ancestry_list.pop()

    # Update list of backgrounds
    backgrounds = requests.get('https://api.pathfinder2.fr/v1/pf2/background', headers = header)
    background_list = []
    for result in backgrounds.json()['results']:
        background_list.append(result['name'])
    background_list.pop()

    # Update list of classes
    classes = requests.get('https://api.pathfinder2.fr/v1/pf2/class', headers = header)
    classes.json()['results']
    class_list = []
    for result in classes.json()['results']:
        class_list.append(result['name'])
    class_list.pop()

    # Produce csv for character_options.csv
    max_len = max([len(ancestry_list), len(background_list), len(class_list)])
    for item in [ancestry_list, background_list, class_list]:
        while len(item)< max_len:
            item.append(None)


    data = {'Ancestries': ancestry_list, 'Backgrounds': background_list, 'Classes': class_list}

    df = pd.DataFrame(data = data)
    df.to_csv('character_options.csv')




if __name__ == "__main__":
    main()
