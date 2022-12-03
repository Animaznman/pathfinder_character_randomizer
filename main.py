import character as char
import requests
from pywebio.output import *
from pywebio.input import *
import pandas as pd


def main():

    character = char.Character('') # Initialize empty character object
    # character.generate_character()
    # print(character.ancestry+" "+character.background+" "+character.job)
    # print(character.colors_data)

    # Update character options references
    # update_character_options()

    # Handling actual html output
    html_output(character)


def html_output(character):
    with use_scope('scope1', clear = True):
        put_text('Pathfinder 2e Character Generator')
        data = input_group("Preset Character Information",[
            actions(buttons = [
                {'label': 'Generate character', 'value': 'generate_character'},
                {'label': 'Generate character with priors', 'value': 'generate_character_with_priors', 'color': 'secondary'},
                {'label': 'Clear Form', 'value' : 'reset', 'type': 'reset', 'color': 'warning'},
                {'label': 'Cancel', 'type': 'cancel', 'color': 'danger'},
                ],
            name = 'top_options'
            ),
            input('Name', name = 'name', type = TEXT, value = character.name),
            select('Ancestry', name = 'Ancestry', options = char.ancestries, value = character.ancestry),
            select('Background', name = 'Background', options = char.backgrounds, value = character.background),
            select('Class', name = 'Class', options = char.classes, value = character.job),
            radio('Gender', name = 'Gender', options = char.genders, value = character.gender),
            input('Age', name = 'Age', type = NUMBER, value = character.age),
            select('Alignment', name = 'Alignment', options = char.flattened_alignments, value = character.alignment),
            slider('Height (in centimeters)', name = 'Height', min_value = 10, max_value = 400, value = character.height),
            slider('Weight (in pounds)', name = 'Weight', min_value = 1, max_value = 600, value = character.weight),
            input('Primary Color', name = 'color_1', type = 'color', value = character.colors_data[0]),
            input('Secondary Color', name = 'color_2', type = 'color', value = character.colors_data[1]),
            input('Tertiary Color', name = 'color_3', type = 'color', value = character.colors_data[2]),
            actions(buttons = [
                {'label': 'Print Character to csv', 'value': 'print_character', 'type': 'submit', 'color': 'success'}
                ], name = 'print'
            )
        ])
    # put_text('You clicked the `%s` button' % data['top_options'])
    if data['top_options'] == 'generate_character':
        character.generate_character()
        html_output(character)
    elif data['top_options'] == 'generate_character_with_priors':
        character.generate_character(data)
        html_output(character)
    elif data['top_options'] == 'reset':
        character = char.Character()
        html_output(character) # This seems pretty hacky.
    # elif data['top_options'] ==
    
    def button_clicked():
        # put_text('button pushed')
        with use_scope('scope1', clear = True):
            new_char = char.Character('Placeholder')
            new_char.generate_character()


            put_table([
                ['Character Name', new_char.name],
                ['Ancestry', new_char.ancestry,'Background', new_char.background,'Class', new_char.job],
                ['Gender', new_char.gender,'Age', new_char.age,'Alignment', new_char.alignment],
                ['Height (cm)', new_char.height, 'Weight (lbs)', new_char.weight],
                ['Colors', style(put_text(rgb_0),'background-color: rgb'+rgb_0), style(put_text(rgb_1),'background-color: rgb'+rgb_1), style(put_text(rgb_2),'background-color: rgb'+rgb_2)]
            ])

    # put_button('Generate Character', onclick = button_clicked)

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
