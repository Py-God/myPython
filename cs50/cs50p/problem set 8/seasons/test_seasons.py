from seasons import calculator

def test_algorithm():
    assert calculator('') == None
    assert calculator('1990, September 2') == None
