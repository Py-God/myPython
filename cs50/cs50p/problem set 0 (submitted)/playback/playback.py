def main():
    phrase = input()
    print(playback(phrase))

def playback(phrase):
    return '...'.join(phrase.split())

main()
