import emoji
def main():
    text = input('Input: ')
    print(emoji_converter(text))

def emoji_converter(text):
    return emoji.emojize(text, language='alias')
    
if __name__ == '__main__':
    main()
