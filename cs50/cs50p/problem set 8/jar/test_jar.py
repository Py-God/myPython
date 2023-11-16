from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(10)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    jar.deposit(10)
    assert jar.size == -2

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == '🍪🍪🍪🍪🍪🍪🍪🍪'
    jar.withdraw(20)
    assert jar.size == -12
