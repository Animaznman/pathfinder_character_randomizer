# Character Object to have stats and the randomization functions
import pandas as pd
import numpy as np
import random as rand

character_options = pd.read_csv('character_options.csv')
ancestries = character_options['Ancestries'].dropna().to_numpy()
backgrounds = character_options['Backgrounds'].to_numpy()
classes = character_options['Classes'].dropna().to_numpy()
genders = ['male', 'female', 'non-binary']
alignments = [["Lawful Good", "Neutral Good", "Choatic Good"],
    ["Lawful Neutral", "True Neutral", "Chaotic Neutral"],
    ["Lawful Evil", "Neutral Evil", "Chaotic Neutral"]]


class Character:
    (
        _ancestry,
        _background,
        _job,
        _gender,
        _age,
        _height,
        _weight,
        _alignment
    ) = (None, ) * 8

    def __init__(self, name):
        self.name = name
    
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
    
    '''
    Section for actual methods to run on class
    '''

    def randomize_ancestry(self):
        self._ancestry = ancestries[rand.randint(0, ancestries.size-1)]

    def randomize_background(self):
        self._background = backgrounds[rand.randint(0, backgrounds.size-1)]
    
    def randomize_class(self):
        self._job = backgrounds[rand.randint(0, backgrounds.size-1)]
    
    def randomize_gender(self):
        random_num = rand.gauss(1,.2)
        if random_num < .2 or random_num >1.8:
            self._gender = "non-binary"
        elif random_num >= .2 and random_num < 1:
            self._gender = "male"
        elif random_num >= 1 and random_num <=1.8:
            self._gender = "female"
    
    def randomize_age(self):
        self._age = rand.gauss(40, 5)

    def randomize_weight(self):
        self._weight = rand.gauss(180, 20)
    
    def randomize_height(self):
        self._height = rand.gauss(175, 20)

    def randomize_alignment(self):
        rand_1 = rand.randint(0,2)
        rand_2 = rand.randint(0,2)
        self._alignment = alignments[rand_1][rand_2]
    
