from bank import value

def test_value_hello():
    assert value('hello world') == '$0'
    assert value('hello govn\'r') == '$0'

def test_value_h():
    assert value('hey mate, how you') == '$20'
    assert value('heyyooo') == '$20'

def test_value_not_h_or_hello():
    assert value('who goes you') == '$100'
    assert value('of course i love you, i just love him more') == '$100'
