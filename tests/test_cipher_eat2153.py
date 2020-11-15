from cipher_eat2153 import cipher_eat2153 

def test_cipher_symbol():
    expected = "zpeb?"
    result = cipher_eat2153.cipher(text = "yoda?", shift = 1, encrypt = True)
    assert result == expected