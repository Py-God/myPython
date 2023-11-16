import random

coin = ['head', 'tail']

def main():
    no = int(input('How many times do you want to simulate? '))
    hp, tp = probability_finder(no)
    print(f"Head probability: {hp} | Tail probability: {tp}")

def simulate(n):
    heads = 0
    tails = 0
    for i in range(n):
        pick = random.choice(coin)
        if pick == 'head':
            heads += 1
        else:
            tails += 1
    print(f"Heads: {heads} | Tails: {tails}")
    return heads, tails

def probability_finder(no):
    headcount, tailcount = simulate(no)
    head_probability = str((headcount/no) * 100) + '%'
    tail_probability = str((tailcount/no) * 100) + '%'

    return head_probability, tail_probability

main()

    
        
        
    
