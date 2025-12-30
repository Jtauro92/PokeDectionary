'''Module for managing stats of a creature.'''
from validation import set_stat

class Stats():
    def __init__(self, hp=None, atk=None, defn=None, spatk=None, spdef=None, speed=None):
        self.__hp = hp
        self.__atk = atk
        self.__defn = defn
        self.__spatk = spatk
        self.__spdef = spdef
        self.__speed = speed

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    @set_stat
    def hp(self, value):
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    @set_stat
    def atk(self, value):
        self.__atk = value

    @property
    def defn(self):
        return self.__defn

    @defn.setter
    @set_stat
    def defn(self, value):
        self.__defn = value

    @property
    def spatk(self):
        return self.__spatk

    @spatk.setter
    @set_stat
    def spatk(self, value):
        self.__spatk = value

    @property
    def spdef(self):
        return self.__spdef


    @spdef.setter
    @set_stat
    def spdef(self, value):
        self.__spdef = value

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    @set_stat
    def speed(self, value):
        self.__speed = value

    def __iter__(self):
        yield from [self.__hp, self.__atk, self.__defn, 
                    self.__spatk, self.__spdef, self.__speed]

    




