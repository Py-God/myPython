import pprint

message = 'it was a bright cold day in April, the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
print('----------')
print(pprint.pformat(count))

# dont stress understanding how the computer works, this code is written to count how many times a character appears DAZALL

