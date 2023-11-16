def main():
    ans = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').strip().lower()
    print(thinker(ans))

def thinker(ans):
    match ans:
        case '42'|'forty-two'|'forty two':
            return 'Yes'
        case _:
            return 'No'

main()
