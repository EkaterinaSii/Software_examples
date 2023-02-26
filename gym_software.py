#! usr/bin/python3

import secrets
import string


def register(count):

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password2 = input("Enter your password again: ")

    if password == password2:
        while True:
            try: 
                print(f"You are sucessfully registered! You ID number is {count+1}")
                print("Please, enter the following information: \n")

                name = input('What is your name? ')
                surname = input('What is your surname? ')

                while True:
                    try:
                        phone = int(input('Enter your phone number without prefix: '))
                        break
                    except ValueError:
                        print('Now valid answer, try again.')
                        
                while True:
                    try:
                        weight_start = float(input("What is your starting weight in KG? "))
                        break
                    except ValueError:
                        print('Now valid answer, try again.')

                while True:

                    try:
                        height = float(input("What is your height in CM? "))
                        break

                    except ValueError:
                        print('Now valid answer, try again.')

                while True:
                    try:
                        age = int(input("What is your age? "))
                        break
                    except ValueError:
                        print('Now valid answer, try again.')

                while True:
                    try:
                        weight_goal = float(input("What is your goal weight in KG? "))
                        break
                    except ValueError:
                        print('Now valid answer, try again.')
                            
                BMI_start = round((weight_start / (height * height))*10000,2)
                BMI_goal = round((weight_goal / (height * height))*10000,2)

                print(f'''You entered information:
                    Weight right now is {weight_start}
                    The goal weight is {weight_goal}
                    Your age is {age}
                    Your height is {height}''')
                            
            except ValueError:
                print('You entered something wrong. Try again.')   

            while True:
                ask = input("Enter 'Yes' if everything is right and 'No' if you need to change: ")

                if ask.lower() == 'yes':
                    new_params = {"username": username, "password": password, 'name':name, 'surname':surname,'phone':phone, 'paid':'N', "starting_weight": weight_start, "height": height, "age": age, "weight": weight_start, "weight_goal": weight_goal, "BMI_start": BMI_start, "BMI_current": BMI_start, "BMI_goal": BMI_goal}
                    count +=1
                    print(f'''Sucessfully safed!
                    Your BMI now is {BMI_start}
                    And your goal BMI is {BMI_goal}''')
                    return new_params,count

                elif ask.lower() == 'no':
                    print('Okay, lets change something')
                    break

                else:
                    print('You entered something wrong. Try again')

    else:
        print("Passwords do not match")
        register()


def update_weight(users,user_id) -> dict:

    ask = float(input('What is your current weight? '))
    users[user_id]['weight'] = ask
    height = users[user_id]['height']
    BMI = round((ask / (height * height))*10000,2)
    users[user_id]['BMI_current'] = BMI

    print(f'''Information is sucessfully updated!
    Now your weight is {ask}
    Your current BMI is {BMI}''')

    return users

def change_info(users,user_id):
    while True:
            print ("""
            1. Change username
            2. Change password
            3. Change height
            4. Change weight goal
            5. Quit
            Enter here: 
            """)
            ask = int(input("What kind of information you want to change? Choose between(1-5): "))
                
            if ask == 1:
                ask_2 = input("Write your new username which you want to change?")
                print("Username is changed.")
                users[user_id]["username"] = ask_2
                return users
                
                    
            elif ask == 2:
                ask = input("Write your new password which you want to change?")
                print("password is changed.")
                users[user_id]["password"] = ask
                return users
                

            elif ask == 3:
                ask = input("Write your height which you want to change?")
                print("height is changed.")
                users[user_id]["height"] = ask
                return users
                
                    
            elif ask == 4:
                ask = input("Write your new weight_goal which you want to change?")
                print("weight_goal is changed.")
                users[user_id]["weight_goal"] = ask 
                return users
                

            elif ask == 5:
                print("Saving all...Thank you")
                main_menu(users, user_id)
            else:
                continue


def delete_customer(users,user_id):
    print('We are sorry you are leaving us :( ')
    del users[user_id]
    return users

def login(users):

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for key, value in users.items():
        if users[key]["username"] == username and users[key]["password"] == password:
            print(f"Logged in user {username} with login id {key}")
            main_menu(users,key)
        else:
            print("Invalid username or password")
            login(users)

    

def paid_or_not(users,user_id):

    if users[user_id]['paid'] == 'Y':
        print('The monthly fee is paid')
    else:
        print('The monthly fee is not paid')
    
    
def main_menu(users, user_id):
    print(f'Hello, {users[user_id]["username"]}\n')

    while True:

        try:
            ask = int(input('''
            What would you like to do? Enter 1-5
            1. Update weight and BMI
            2. Change your information
            3. Check if monthly fee is paid
            4. Delete account
            5. Sign out
            '''))

            if ask == 1:
                users = update_weight(users,user_id)
            elif ask == 2:
                users = change_info(users,user_id)
            elif ask == 3:
                paid_or_not(users,user_id)
            elif ask == 4:
                users = delete_customer(users,user_id)
                main()
                break
            elif ask == 5:
                print('Thank you! See you soon!')
                break
            else:
                print('You entered wrong number. Try again')
                main_menu(users, user_id)

        except ValueError:
            print('You entered something wrong. Try again.')
            main_menu(users, user_id)
    


def main():

    count = 0
    users = {}

    try:

        while True:

            ask_main_menu = int(input((""" Welcome to main menu!
            Choose what would you like to do:
            1. Register
            2. Log-in
            3. Exit
            """)))

            if ask_main_menu == 1:
                new_params, count = register(count)
                users[count] = new_params

            elif ask_main_menu == 2:
                login(users)

            elif ask_main_menu == 3:
                print('Thank you! See you again soon!')
                break

            else:
                print('You entered wrong number. Try again')
                continue
           
    except ValueError:
        print('You entered something wrong. Try again')
        main()


if __name__ == "__main__":
    main()