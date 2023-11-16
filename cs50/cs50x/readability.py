import re

text = input('Text: ')

def main():
    reading_level = reading_level_calculator()
    if reading_level < 1:
        print('Before Grade 1')
    elif reading_level >= 16:
        print('Grade 16+')
    else:
        print(f"Grade {reading_level}")

def reading_level_calculator():
    char_count = character_counter()
    word_count = word_counter()
    sentence_count = sentence_counter()

    L = (char_count/word_count)*100
    S = (sentence_count/word_count) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    reading_level = round(index)
    return reading_level

def character_counter():
    re_object = re.compile(r'[a-zA-Z]')
    character_list = re.findall(re_object, text)
    character_count = len(character_list)
    return character_count

def  word_counter():
    re_object = re.compile(r' ')
    word_list = re.split(re_object, text)
    word_count = len(word_list)
    return word_count

def sentence_counter():
    re_object = re.compile(r'\.|\!|\?')
    sentence_list = re.split(re_object, text)
    for sentence in sentence_list:
        if sentence == '':
            sentence_list.remove(sentence)
    sentence_count = len(sentence_list)
    return sentence_count


main()

