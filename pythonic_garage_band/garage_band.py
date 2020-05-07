from abc import ABC, abstractmethod

class Band():
    all_members = []
    def __init__(self, name, members=[]):
        
        self.name = name
        self.members = members
        self.__class__.all_members.append(self)

    def play_solos(self):
        solos = ""
        for solo in self.members:
            solos += f"{solo.play_solo()}"
        return solos[:]

    def __str__(self):
        return f"This Band name is {self.name}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance."

    @classmethod
    def to_list(cls):
        return cls.all_members

class Musician(ABC):
    members = []
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        self.__class__.members.append(self)

    @abstractmethod
    def get_instrument(self):
        return self.instrument

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):

    play_type = "Guitar"
    
    def __init__(self, name):
        super().__init__(name, self.__class__.play_type)
    
    def play_solo(self):
        return "En Iniya Pon Nilave"

    def get_instrument(self):
        return self.__class__.play_type

    def __str__(self):
        return f"This Band name is {self.name}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance"


class Bassist(Musician):

    play_type = "Bass"

    def __init__(self, name, solo= "Yeno Vaanilai Maaruthey"):
        super().__init__(name, self.__class__.play_type)
        self.solo = solo

    def play_solo(self):
            return self.solo

    def get_instrument(self):
        return self.__class__.play_type
    
    def __str__(self):
        return f"This Band name is {self.name}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance"


class Drummer(Musician):

    play_type = "Drum"

    def __init__(self, name, solo= "Puthu Vellai Mazhai"):
        super().__init__(name, self.__class__.play_type)
        self.solo = solo

    def play_solo(self):
            return self.solo
    
    def get_instrument(self):
        return self.__class__.play_type

    def __str__(self):
        return f"This Band name is {self.name}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance"