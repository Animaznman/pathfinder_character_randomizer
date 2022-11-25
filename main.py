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
    
    put_button('Generate Character', onclick = generate_character())
    put_table([
        ['Character Name', character.name],
        ['Ancestry', character.ancestry],
        ['Background', character.background],
        ['Class', character.job],
        ['Gender', character.gender],
        ['Age', character.age],
        ['Height (cm)', character.height],
        ['Weight (lbs)', character.weight],
        ['Alignment', character.alignment],
        ['Colors'], character.colors]
    )



if __name__ == "__main__":
    main()