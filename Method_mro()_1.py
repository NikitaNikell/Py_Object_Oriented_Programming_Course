""" Аббревиатура MRO – method resolution order (переводится как «порядок разрешения методов»).
Этот порядок относится не только к поискам методов, но и к прочим атрибутам класса, так как методы –
это частный случай более общего понятия «атрибут»"""

class O():
    pass
class A(O):
    pass
class B(O):
    pass
class C(O):
    pass
class D(O):
    pass
class E(O):
    pass
class K1(C, A, B):
    pass
class K2(A, D):
    pass
class K3(B, D, E):
    pass
class Z(K1, K2, K3):
    pass

def get_mro(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')


get_mro(Z)
