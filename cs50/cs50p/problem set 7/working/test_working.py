from working import convert

def test_am_to_pm():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:30 PM') == '09:00 to 17:30'

def test_pm_to_am():
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('5:00 PM to 9:00 AM') == '17:00 to 09:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_errors():
    assert convert('9:60 AM to 5:60 PM') == '09:60 to 17:60'
    assert convert('9 AM - 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM - 17:00 PM') == '09:00 to 17:00'
