from fuel import convert, guage

def test_convert():
    assert convert('1/2') == 50
    assert convert('3/4') == 75

def test_guage():
    assert guage(50) == '50%'
    assert guage(75) == '75%'
    assert guage(100) == 'F'
    assert guage(0) == 'E'
