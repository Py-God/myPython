from plates import is_valid

def test_plates1():
    assert is_valid('GOODBYE') == False
    assert is_valid('MY NAME IS BARRY ALLEN AND I AM THE FASTEST MAN ALIVE') == False

def test_plates2():
    assert is_valid('HELLO') == True
    assert is_valid('OUTATIME') == False

def test_plates3():
    assert is_valid('PI3.14') == False
    assert is_valid('H') == False

def test_plates4():
    assert is_valid('CS50') == True
    assert is_valid('AAA222') == True
    
