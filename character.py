# Character Object to have stats and the randomization functions
import pandas as pd
import numpy as np
import random as rand

character_options = pd.read_csv('character_options.csv')
ancestries = character_options['Ancestries'].dropna().to_numpy()
backgrounds = character_options['Backgrounds'].to_numpy()
classes = character_options['Classes'].dropna().to_numpy()
genders = ['Male', 'Female', 'Non-binary']
alignments = [["Lawful Good", "Neutral Good", "Choatic Good"],
    ["Lawful Neutral", "True Neutral", "Chaotic Neutral"],
    ["Lawful Evil", "Neutral Evil", "Chaotic Neutral"]]
flattened_alignments = np.array(alignments).flatten()

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
    def set_ancestry(self, index: int):
        self._ancestry = ancestries[index]
    ancestry = property(get_ancestry, set_ancestry)

    def get_background(self):
        return self._background
    def set_background(self, index: int):
        self._background = backgrounds[index]
    background = property(get_background, set_background)

    def get_class(self):
        return self._job
    def set_class(self, index: int):
        self._job = classes[index]
    job = property(get_class, set_class)

    def get_gender(self):
        return self._gender
    def set_gender(self, index: int):
        self._gender = genders[index]
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
    def set_alignment(self, alignment: tuple):
        self._alignment = alignments[alignment[0]][alignment[1]]
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
        self._ancestry = ancestries[rand.randint(0, ancestries.size-1)]

    def randomize_background(self):
        self._background = backgrounds[rand.randint(0, backgrounds.size-1)]

    def randomize_class(self):
        self._job = classes[rand.randint(0, classes.size-1)]

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
        if data['Ancestry'] is not None:
            self.set_ancestry(data['Ancestry'])
        else:
            self.randomize_ancestry()
        if data['Background'] is not None:
            self.set_background(data['Background'])
        else:
            self.randomize_background()
        if data['Class'] is not None:
            self.set_class(data['Class'])
        else:
            self.randomize_class()
        if data['Gender'] is not None:
            self.set_gender(data['Gender'])
        else:
            self.randomize_gender()
        if data['Alignment'] is not None:
            self.set_alignment(data['Alignment'])
        else:
            self.randomize_alignment()
        if data['Age'] is not None:
            self.set_age(data['Age'])
        else:
            self.randomize_age()
        if data['Height'] is not None:
            self.set_height(data['Height'])
        else:
            self.randomize_height()
        if data['weight'] is not None:
            self.set_weight(data['weight'])
        else:
            self.randomize_weight()
        if data['color_1'] is not None and data['color_2'] is not None and data['color_3'] is not None:
            self.set_colors(data['color_1'], data['color_2'], data['color_3'])
        else:
            self.randomize_colors()
