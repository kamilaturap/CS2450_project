# Mackay's Implemented Methods:

def load(target_memory_location, registers_dictionary):
    try:
        word = registers_dictionary[int(target_memory_location)]
        return word

    except KeyError:
        print("Target memory location out of bounds.")


def store(target_memory_location, registers_dictionary, word):
    try:
        if registers_dictionary[int(target_memory_location)] is None:
            raise KeyError
        registers_dictionary[int(target_memory_location)] = word
        return

    except KeyError:
        print("Target memory location out of bounds.")


def branch(target_memory_location, registers_dictionary):
    try:
        if registers_dictionary[int(target_memory_location)] is None:
            raise KeyError
        return int(target_memory_location) - 1

    except KeyError:
        print("Target memory location out of bounds.")
