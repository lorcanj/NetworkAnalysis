import random


def create_id_alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    return alphabet + alphabet.upper() + numbers


def generate_random_id(alphabet: str, list_with_component_id: list[str], id_length: int = 11):
    for i in range(id_length):
        list_with_component_id.append(alphabet[random.randint(0, len(alphabet) - 1)])
    return ''.join(list_with_component_id)
