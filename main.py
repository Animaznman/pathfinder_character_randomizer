import character as char
import requests
from requests.auth import HTTPBasicAuth
from pywebio.output import *
from pywebio.input import *


def main():

    character = char.Character('Placeholder') # Initialize empty character object
    # character.generate_character()
    # print(character.ancestry+" "+character.background+" "+character.job)

    # For updating pathfinder references
    api_key = 'da468b89-2bf8-4e2b-a939-79c6e6ef25ce'
    header = {"Authorization": api_key}
    r = requests.get('https://api.pathfinder2.fr/v1/pf2', headers = header)
    print(r.status_code)

    # Handling actual html output
    html_output(character)


def html_output(character):
    put_text('Pathfinder 2e Character Generator')
    # data = input_group("Preset Character Information",[
    #     input('Character Name', name = 'name', type = TEXT, placeholder = 'Names are hard'),
    #     select('Character Ancestry', name = 'Ancestry', options = char.ancestries),
    #     select('Character Background', name = 'Background', options = char.backgrounds),
    #     select('Character Class', name = 'Class', options = char.classes),
    #     radio('Character Gender', name = 'Gender', options = char.genders),
    #     input('Character Age', name = 'Age', type = NUMBER),
    #     select('Character Alignment', name = 'Alignment', options = char.flattened_alignments),
    #     slider('Character Height (in centimeters)', name = 'Height', value = 175, min_value = 10, max_value = 400),
    #     slider('Character Weight (in pounds)', name = 'Weight', value = 180, min_value = 1, max_value = 600)
    # ])

    def button_clicked():
        # put_text('button pushed')
        with use_scope('scope1', clear = True):
            new_char = char.Character('Placeholder')
            new_char.generate_character()
            put_table([
                ['Character Name', new_char.name],
                ['Ancestry', new_char.ancestry],
                ['Background', new_char.background],
                ['Class', new_char.job],
                ['Gender', new_char.gender],
                ['Age', new_char.age],
                ['Height (cm)', new_char.height],
                ['Weight (lbs)', new_char.weight],
                ['Alignment', new_char.alignment],
                ['Colors'], new_char.colors]
            )

    put_button('Generate Character', onclick = button_clicked)

    



if __name__ == "__main__":
    main()