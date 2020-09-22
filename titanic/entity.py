from dataclasses import dataclass

@dataclass
class Entity:

    context: str = '/Users/kwonhyunah/Desktop/SBAPROJECTS/titanic/data/'
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''