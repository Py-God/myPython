import requests, sys, json, re

if len(sys.argv) != 2:
    print('Missing command-line argument')
    sys.exit()
    
try:
    number = float(sys.argv[1])
except ValueError:
    print('Command-line argument is not a number')
    sys.exit()
    
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    print('Something went wrong.')
    sys.exit()
else:
    o = response.json()

result = o['bpi']['USD']['rate']

obj = re.compile(r'(\d+),(\d+.\d+)')
match = re.search(obj, result)
price = float(match.group(1) + match.group(2))

converted_price = '$' + str(f'{(price * number):,}')

print(converted_price)
