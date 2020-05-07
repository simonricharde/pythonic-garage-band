import pytest
from pythonic_garage_band.garage_band import Musician, Guitarist, Bassist, Drummer, Band


def test_abstract_musician():

    with pytest.raises(TypeError):
         Musician("?" , "?")


def test_guitarist_name():
    surya = Guitarist("Surya Sivakumar")
    assert surya.name == "Surya Sivakumar"
    
def test_guitarist_instrument():
    surya = Guitarist("Surya Sivakumar")
    assert surya.instrument == "guitar".title()
    
def test_guitarist_play_solo():
    surya = Guitarist("Surya Sivakumar")
    assert surya.play_solo() =="En Iniya Pon Nilave"


def test_bassist_name():
    rehman = Bassist("AR Rehman")
    assert rehman.name == "AR Rehman"

def test_bassist_instrument():
    rehman = Bassist("AR Rehman")
    assert rehman.instrument == "bass".title()
   
def test_bassist_play_solo():
    rehman = Bassist("AR Rehman")
    assert rehman.play_solo() == "Yeno Vaanilai Maaruthey"


def test_drums_name():
    siva = Drummer("Drums Sivamani")
    assert siva.name == "Drums Sivamani"

def test_drums_instrument():
    siva = Drummer("Drums Sivamani")
    assert siva.instrument == "drum".title()
    
def test_drums_play_solo():
    siva = Drummer("Drums Sivamani")
    assert siva.play_solo() == "Puthu Vellai Mazhai"

def test_guitarist_repr():
    assert 'Guitarist instance' == Guitarist('Surya').__repr__()

def test_bassist_repr():
    assert 'Bassist instance' == Bassist('Rehman').__repr__()

def test_drummer_repr():
    assert 'Drummer instance' == Drummer('Sivamani').__repr__()

def test_guitarist_str():
    assert 'This Band name is Surya' == Guitarist('Surya').__str__()

def test_bassist_str():
    assert 'This Band name is Rehman' == Bassist('Rehman').__str__()

def test_drummer_str():
    assert 'This Band name is Sivamani' == Drummer('Sivamani').__str__()

def test_guitarist_get_instrument():
    assert 'guitar'.title() == Guitarist('Surya').get_instrument()

def test_bassist_get_instrument():
    assert 'bass'.title() == Bassist('Rehman').get_instrument()

def test_drummer_get_instrument():
    assert 'drum'.title() == Drummer('Sivamani').get_instrument()



def test_custom_solo_bass():
    solo = ""
    aniruth = Bassist("Aniruth Ravichander", solo)
    assert aniruth.play_solo() == solo


def test_play_solos_band1(harmony_band1):
    solos = harmony_band1.play_solos()
    print(solos)
    assert solos == "En Iniya Pon NilaveYeno Vaanilai MaarutheyPuthu Vellai Mazhai"

def test_play_solos_band2(harmony_band2):
    solos = harmony_band2.play_solos()
    print(solos)
    assert solos == "Yeno Vaanilai MaarutheyPuthu Vellai MazhaiEn Iniya Pon Nilave"

def test_play_solos_band3(harmony_band3):
    solos = harmony_band3.play_solos()
    print(solos)
    assert solos == "Puthu Vellai MazhaiEn Iniya Pon NilaveYeno Vaanilai Maaruthey"

def test_musicians_members():
    Musician.members = []
    guitarist = Guitarist('Surya')
    bassist = Bassist('Rehman')
    drummer = Drummer('Sivamani')
    assert [guitarist, bassist, drummer] == Musician.members

@pytest.fixture
def harmony_band1():
    harmony = Band (
        "harmony", 
        [Guitarist("Surya"), Bassist("Rehman"), Drummer("Sivamani")]
    )

    return harmony

@pytest.fixture
def harmony_band2():
    harmony = Band (
        "harmony", 
        [Bassist("Rehman"), Drummer("Sivamani"), Guitarist("Surya")]
    )

    return harmony

@pytest.fixture
def harmony_band3():
    harmony = Band (
        "harmony", 
        [Drummer("Sivamani"), Guitarist("Surya"), Bassist("Rehman")]
    )

    return harmony


