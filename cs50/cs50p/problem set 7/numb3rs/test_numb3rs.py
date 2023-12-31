from numb3rs import validate

def test_trues():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True

def test_falses():
    assert validate('256.256.256.256') == False
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
