#! python3
import random

deck = [card for card in range(1, 16)]
eight_random_cards_list = random.sample(deck, 8)

def game():
    score = 0
    for no in range(8):
        if no < 7:
            print(f"The no {no+1} card is: {str(eight_random_cards_list[no])}")
            print('Is the next card higher or lower? (h = higher, l=lower)')
            ans = input().lower()
            next_card = eight_random_cards_list[no+1]
            current_card = eight_random_cards_list[no]
            if ans == 'h' and next_card > current_card:
                score += 20
                print('Correct! Your score is: ' + str(score) + 'points.')
            elif ans == 'l' and next_card < current_card:
                score += 20
                print('Correct! Your score is: ' + str(score) + 'points.')
            else:
                if score < 15:
                    score = 0
                    print('Incorrect! Your score is: ' + str(score) + 'points.')
                else:
                    score -= 15
                    print('Incorrect! Your score is: ' + str(score) + 'points.')
    print('Your total score is: ' + str(score))

game()