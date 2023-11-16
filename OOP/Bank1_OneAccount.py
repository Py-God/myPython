#Create (an account)
#Deposit
#Withdraw
#Check balance

#Customer name
#Password
#Balance

import sys
from pprint import pprint

def main(): 
    while True:
        print('''Create (an account): c
Deposit: d
Withdraw: w
Check balance: b
Exit: e
list of accounts: l        ''')
        ans = input().lower()
        if ans == 'c':
            create_an_account()
        elif ans == 'd':
            deposit()
        elif ans == 'w':
            withdraw()
        elif ans == 'b':
            check_balance()
        elif ans == 'l':
            account_list()
        else:
            sys.exit()

def create_an_account():
    global accounts
    accounts = []

    acc_name = input('Account name: ')
    acc_password = input('Account password: ')
    account_balance = 0

    global account_dict
    account_dict = {
        'Customer name': acc_name,
        'password': acc_password,
        'balance': account_balance
    }
    accounts.append(account_dict)

def deposit():
    amount = int(input('How much money do you want to deposit? '))
    account_dict['balance'] += amount
    print('Successful deposit!')
    print('Account balance: $' + str(account_dict['balance']))
    return account_dict

def withdraw():
    if account_dict['balance'] > 0:
        amount = int(input('How much money do you want to withdraw? '))
        if amount <= account_dict['balance']:
            account_dict['balance'] -= amount
            print('Successful withdraw!')
            print('Account balance: $' + str(account_dict['balance']))
            return account_dict
        else:
            print('Insufficient balance.')
    else:
        print('You have no money.')

def check_balance():
    print('Account balance: $' + str(account_dict['balance']))

def account_list():    
    pprint(accounts)

main()