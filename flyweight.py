# Flyweight class
class Character:
    def __init__(self, symbol):
        self.symbol = symbol

    def render(self, context):
        print(f"Rendering character '{self.symbol}' in context {context}")


# Flyweight factory class
class CharacterFactory:
    characters = {}

    @staticmethod
    def get_character(symbol):
        if symbol not in CharacterFactory.characters:
            CharacterFactory.characters[symbol] = Character(symbol)
        return CharacterFactory.characters[symbol]


# Client code
characters = [
    CharacterFactory.get_character('A'),
    CharacterFactory.get_character('B'),
    CharacterFactory.get_character('A'),
    CharacterFactory.get_character('C'),
    CharacterFactory.get_character('B'),
    CharacterFactory.get_character('A'),
]

for index, character in enumerate(characters):
    character.render(f"context {index}")