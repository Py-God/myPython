def main():
    text = input()
    print(convert(text))

def convert(text):
    smily_face = ':)'
    frowny_face = ':('
    if smily_face in text and frowny_face in text:
        new_text = text.replace(smily_face, '🙂')
        new_text2 = new_text.replace(frowny_face, '🙁')
        return new_text2
    if smily_face in text:
        new_text = text.replace(smily_face, '🙂')
    if frowny_face in text:
        new_text = text.replace(frowny_face, '🙁')

    return new_text

main()
