def main():
    text = input('Input: ')
    print('Output:', shorten(text))

def shorten(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if vowel in text.lower():
            text = text.replace(vowel, '')
    return text

if __name__ == '__main__':
    main()
