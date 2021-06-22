class contato():
    _nome:str = ''
    _telefone:str = '0'
    _email:str = ''

    def __init__(self, nome:str, telefone:str, email:str):
        _nome = nome
        _telefone = telefone
        _email = email

    def __iter__(self):
        yield 'nome', self._nome
        yield 'telefone', self._telefone
        yield 'email', self._email