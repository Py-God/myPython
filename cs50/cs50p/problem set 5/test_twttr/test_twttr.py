from twttr import shorten

def test_shortener_lowercase():
    assert shorten('twitter') == 'twttr'
    assert shorten('name') == 'nm'

def test_shortener_uppercase():
    assert shorten('Boluwatife') == 'Blwtf'
    assert shorten('Pickaxe') == 'Pckx'
