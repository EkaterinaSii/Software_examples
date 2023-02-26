#! usr/bin/python3

"""    EXPLANATION:

The id of dictionary stays the same in every function because the purpose of the code is to change the initial dictionary without changing the ID of it. 
Meanwhile the id of variable count and acc_log are changing:
1. acc_log - we change the value of the variable when changing the account number we are working with. As well the acc_log is int, so there is no possibility
to re-assing it without changing id
2. count - before function new_account() and inside this function the id is the same, because I use it to set the key for new record
Then afte creating new account, we make cout +=1 so the id of the variable changing since it is int and cannot be changed witout that. 

"""

import random

def check_log_in(acc_login, acc_password,accounts):
    """ Takes account login, password and dictionary as arguments. Checks that login and passwords are correct. If so, returns TRUE if not FALSE"""

    for key,value in accounts.items():
        if accounts[key]['account_login'] == acc_login and accounts[key]['account_password'] == acc_password:
            print(f'Id of dictionary with accounts inside check_log_in function is {id(accounts)}')
            return True
        else:
            return False


def check_balance(accounts,acc_login):
    """ Takes dictionary and account login info as arguments. Checks the account number user logged in and prints following info: contact info, account number, BIC and balance. """
    for key,value in accounts.items():
        if accounts[key]['account_login'] == acc_login:
            print(f'''Your account information:
                        Contact information: {accounts[key]['name']}
                        Account number: {accounts[key]["account_number"]}
                        BIC number: {accounts[key]["BIC"]}
                        Balance: {accounts[key]["balance"]}$\n''')

    print(f"The id of dictionary with accounts inside check_balance function {id(accounts)}\n")
    

def deposit_money(accounts,acc_log):
    """ Takes dictionary and login info as arguments. Asking what amount of money would like to add. Updates the balance info and prints it out."""

    money = int(input("What amount of money would you like to deposit?: "))
    for key,value in accounts.items():
        if accounts[key]['account_login'] == acc_log:
            accounts[key]['balance'] += money
            print(f'The account balance of your account is: {accounts[key]["balance"]}$\n')

    print(f"The id of dictionary with accounts inside deposit_money function {id(accounts)}\n")
    

def withdrawal_money(accounts,acc_log):
    """ Takes dictionary and login info as arguments. Asking what amount of money need to withdraw. Updates the balance information and prints it out."""

    money = int(input("What amount of money would you like to withdraw: "))

    for key,value in accounts.items():
        if accounts[key]['account_login'] == acc_log:
            accounts[key]['balance'] -= money
            print(f'The account balance of your account is: {accounts[key]["balance"]}$\n')

    print(f"The id of dictionary with accounts inside withdrawal_money function {id(accounts)}\n")

    
def new_account(accounts,count):
    """ Takes dictionary and key count variable as arguments. Asks for owner name, new login and passwords.
        Create new account with random account number, balance is 0.0
        Prints information of new account."""

    name = input("Enter here account owner: ")
    account_login = int(input("Enter here account login (only numbers): "))
    account_password = int(input("Enter here account password (only numbers): "))

    accounts[count] = {'account_login':account_login,'account_password':account_password,'name': name,'account_number': random.randint(10000,99998), 'BIC': 'KAKOKR22XXX', 'balance': 0.0}
    print(f'''Your new account:
                Contact information: {accounts[count]['name']}
                Account number: {accounts[count]["account_number"]}
                BIC number: {accounts[count]["BIC"]}
                Balance: {accounts[count]["balance"]}$\n''')

    print(f"The id of dictionary with accounts inside new_account function {id(accounts)}\n")
    print(f"The id of variable count inside new_account function is {id(count)}\n")

    

def switch_acc(accounts):
    """ Takes dictionary as argument. Asking what account number need to change to. Checks login and password
        if correct ->> saves login information to variable acc_log """


    acc_ask = int(input("Enter here account login to switch: "))
    acc_pas = int(input("Enter here password: "))

    for key,value in accounts.items():
        if acc_ask ==  accounts[key]['account_login'] and acc_pas == accounts[key]['account_password']:
            acc_log = accounts[key]['account_login']

    print(f"The id of dictionary with accounts inside switch_acc function {id(accounts)}\n")
    print(f"The id of acc_log inside switch_acc function {id(acc_log)}\n")

    return acc_log

    
    

def main():
    """ Asking for log-in and password of the account. Then offering oprions of the menu and re-direct to specific functions based on choice."""


    count = 2
    accounts = {1:{'account_login':1234,'account_password':1234,'name': 'Kata Sii','account_number': 12345, 'BIC': 'KAKOKR22XXX', 'balance': 0.0}}

    acc_log = int(input('Enter account number to log-in: '))
    acc_password = int(input('Enter password to log-in: '))

    right_or_not  = check_log_in(acc_log,acc_password,accounts)

    if right_or_not == True:
        print("Welcome!\n")

        while True:

            ask_menu = int(input('''What would you like to do? 
                                        1. Check balance / all info
                                        2. Deposit money
                                        3. Withdrawal money
                                        4. Add new account
                                        5. Switch accounts
                                        6. Exit
                                        Enter here: '''))

            if ask_menu == 1:
                check_balance(accounts,acc_log)

            elif ask_menu == 2:
                deposit_money(accounts,acc_log)

            elif ask_menu == 3:
                withdrawal_money(accounts,acc_log)
                
            elif ask_menu == 4:
                print(f"The id of count outside new_account function {id(count)}")
                new_account(accounts,count)
                count += 1
                print(f"The id of count outside new_account function {id(count)}")

            elif ask_menu == 5:
                print(f"The id of acc_log outside switch_acc function {id(acc_log)}")
                acc_log = switch_acc(accounts)
                print(f"The id of acc_log outsidde switch_acc function {id(acc_log)}")
            elif ask_menu == 6:
                print('Exiting...')
                break
            else:
                print('Something went wrong, try again.')



    else:
        print("Password or log-in is wrong, try again.")
        main() 

    

if __name__ == "__main__":
    main()