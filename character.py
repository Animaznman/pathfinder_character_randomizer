# Character Object to have stats and the randomization functions
import pandas as pd
import numpy as np
import random as rand

character_options = pd.read_csv('character_options.csv')
ancestries = character_options['Ancestries'].dropna().to_numpy()
backgrounds = character_options['Backgrounds'].to_numpy()
classes = character_options['Classes'].dropna().to_numpy()

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

    '''
    Section for actual methods to run on class
    '''

    def randomize_ancestry(self):
        self._ancestry = ancestries[rand.randint(0, ancestries.size-1)]

    def randomize_background(self):
        self._background = backgrounds[rand.randint(0, backgrounds.size-1)]
    
    def randomize_class(self):
        self._job = backgrounds[rand.randint(0, backgrounds.size-1)]
    