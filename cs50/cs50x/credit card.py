while True:
    try:
        card_no = int(input('Number: '))
    except ValueError:
        continue

    card_no = str(card_no)
    card_no_length = len(card_no)

    def card_checker():
        if card_no_length == 15:
            if card_verifier():
                print('AMEX')
            else:
                print('INVALID')
        elif card_no_length == 16:
            if card_verifier():
                print('MASTERCARD | VISA')
            else:
                print('INVALID')
        elif card_no_length == 13:
            if card_verifier():
                print('VISA')
            else:
                print('INVALID')
        else:
            print('INVALID')
            

    def card_verifier():
        total_list = []
        for i in range(0, card_no_length, 2):
            no = int(card_no[i])
            no = no*2
            no_string = str(no)
            for no in no_string:
                total_list += [int(no)]
            total1 = sum(total_list)

            
        total2 = 0
        for i in range(1, len(card_no), 2):
            no = int(card_no[i])
            total2 += no

        total = str(total1 + total2)

        if total[-1] == '0':
            return True
        else:
            return False

    card_checker()


    
