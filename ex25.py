def break_words(stuff):
    print "split"
    words = stuff.split(' ')
    return words

def sort_words(words):
    print "sort"
    return sorted(words)

def print_first_word(words)    :
    print "pops and prints first"
    word = words.pop(0)
    print word


def print_last_word(words)    :
    print "pops and prints first"
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    print "sorts full sentence"
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
