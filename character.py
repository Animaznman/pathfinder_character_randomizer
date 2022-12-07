# Character Object to have stats and the randomization functions
import pandas as pd
import numpy as np
import random as rand

character_options = pd.read_csv('character_options.csv')
ancestries = np.insert(character_options['Ancestries'].dropna().to_numpy(), 0, None)
backgrounds = np.insert(character_options['Backgrounds'].dropna().to_numpy(), 0, None)
classes = np.insert(character_options['Classes'].dropna().to_numpy(), 0, None)
genders = ['Male', 'Female', 'Non-binary']
alignments = [["Lawful Good", "Neutral Good", "Chaotic Good"],
    ["Lawful Neutral", "True Neutral", "Chaotic Neutral"],
    ["Lawful Evil", "Neutral Evil", "Chaotic Neutral"]]
flattened_alignments = np.insert(np.array(alignments).flatten(), 0, None)

class Character:
    (
        _ancestry,
        _background,
        _job,
        _gender,
        _age,
        _height,
        _weight,
        _alignment,
        _colors # Tuples of hex code to represent colors for character (tuple of strings)
    ) = (None, ) * 9
    colors_data = ['#FFFFFF', '#FFFFFF', '#FFFFFF'] # I might get lazy and not update this each time _colors is updated hurrhurr


    def __init__(self, name='', data = {}):
        self.name = name
        self.data = data

    def get_ancestry(self):
        return self._ancestry
    def set_ancestry(self, ancestry):
        self._ancestry = ancestry
    ancestry = property(get_ancestry, set_ancestry)

    def get_background(self):
        return self._background
    def set_background(self, background):
        self._background = background
    background = property(get_background, set_background)

    def get_class(self):
        return self._job
    def set_class(self, input):
        self._job = input
    job = property(get_class, set_class)

    def get_gender(self):
        return self._gender
    def set_gender(self, gender):
        self._gender = gender
    gender = property(get_gender, set_gender)

    def get_age(self):
        return self._age
    def set_age(self, age: int):
        self._age = age
    age = property(get_age, set_age)

    def get_height(self):
        return self._height
    def set_height(self, height: float):
        self._height = height
    height = property(get_height, set_height)

    def get_weight(self):
        return self._weight
    def set_weight(self, weight: float):
        self._weight = weight
    weight = property(get_weight, set_weight)

    def get_alignment(self):
        return self._alignment
    def set_alignment(self, alignment):
        self._alignment = alignment
    alignment = property(get_alignment, set_alignment)

    def get_colors(self):
        return self._colors
    def set_colors(self, colors: tuple):
        self._colors = colors
    colors = property(get_colors, set_colors)

    '''
    Section for actual methods to run on class
    '''

    def randomize_ancestry(self):
        self._ancestry = ancestries[rand.randint(1, ancestries.size-1)]

    def randomize_background(self):
        self._background = backgrounds[rand.randint(1, backgrounds.size-1)]

    def randomize_class(self):
        self._job = classes[rand.randint(1, classes.size-1)]

    def randomize_gender(self):
        random_num = rand.gauss(1,.2)
        if random_num < .2 or random_num >1.8:
            self._gender = "Non-binary"
        elif random_num >= .2 and random_num < 1:
            self._gender = "Male"
        elif random_num >= 1 and random_num <=1.8:
            self._gender = "Female"

    def randomize_age(self):
        self._age = round(rand.gauss(40, 10))

    def randomize_weight(self):
        self._weight = round(rand.gauss(180, 20))

    def randomize_height(self):
        self._height = round(rand.gauss(175, 20))

    def randomize_alignment(self):
        rand_1 = rand.randint(0,2)
        rand_2 = rand.randint(0,2)
        self._alignment = alignments[rand_1][rand_2]

    def randomize_colors(self):
        r = lambda: rand.randint(0,255)
        color1 = '#{:02x}{:02x}{:02x}'.format(r(), r(), r()) # I copied this from stack overflow :D hashtagallshame
        color2 = '#{:02x}{:02x}{:02x}'.format(r(), r(), r()) # To be honest, I'm still kinda fuzzy on how this works
        color3 = '#{:02x}{:02x}{:02x}'.format(r(), r(), r()) # Lambda functions be wild, yo.

        self.colors_data = (color1, color2, color3)

    # Generate a character by taking in possible inputs
    def generate_character(self, data = {}):
        if 'Ancestry' in data:
            self.set_ancestry(data['Ancestry'])
        else:
            self.randomize_ancestry()
        if 'Background' in data:
            self.set_background(data['Background'])
        else:
            self.randomize_background()
        if 'Class' in data:
            self.set_class(data['Class'])
        else:
            self.randomize_class()
        if 'Gender' in data:
            self.set_gender(data['Gender'])
        else:
            self.randomize_gender()
        if 'Alignment' in data:
            self.set_alignment(data['Alignment'])
        else:
            self.randomize_alignment()
        if 'Age' in data:
            self.set_age(data['Age'])
        else:
            self.randomize_age()
        if 'Height' in data:
            self.set_height(data['Height'])
        else:
            self.randomize_height()
        if 'weight' in data:
            self.set_weight(data['weight'])
        else:
            self.randomize_weight()
        if 'color_1' in data and 'color_2' in data and 'color_3' in data:
            self.set_colors((data['color_1'], data['color_2'], data['color_3']))
        else:
            self.randomize_colors()
