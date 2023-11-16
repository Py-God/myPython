from um import count

def test_count1():
    assert count('um...') == 1
    assert count('um?') == 1

def test_count2():
    assert count('hello, um, world') == 1
    assert count('um, hello, um, world') == 2

def test_count3():
    assert count('um') == 1
    assert count('yum') == 0
    assert count('yummy...') == 0
