# Mackay's Implemented Methods:

def load(target_memory_location, registers_dictionary):
    word = registers_dictionary[int(target_memory_location)]
    return word


def store(target_memory_location, registers_dictionary, word):
    registers_dictionary[int(target_memory_location)] = word
    return

# def branch(target_memory_location, registers_dictionary):
#   return target_memory_location
