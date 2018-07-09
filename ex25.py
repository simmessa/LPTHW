# @SM more practice, hating.

def break_words(stuff):
    # this format is for python documentation! try help(ex25.break_words) in console...
    # these are called documentation comments
    """This will break words on spaces"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort words, yay"""
    return sorted(words)

def print_first_word(words):
    """Prints first word, nasty"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints last word, Ingenious"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """From full sentence to sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Do I have to explain?"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

