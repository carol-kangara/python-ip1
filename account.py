#!/usr/bin/env python3.6
from credentials import Credentials
from user import Users
def create_credentials(account_name,usern,password):
    '''
    function that creates credentials
    '''
    new_credentials=Credentials(account,usern,password)
    return new_credentials
def save_credentials(credentials):
    '''
    functionto save credentials
    ''' 
    credentials.save_credentials()
def del_credentials(credentials):
    '''
    function to deletes credentials
    '''
    credentials.delete_credentials()
def  find_credentials(account_name):
    '''
    function to find credentials by account name
    '''
    return Credentials.find_by_account_name(account_name)
def  check_existing_credentials(account-name):
    '''
    function that checks if a credentials exists with that account name 
    and return a boolean
    '''
    return Credentials.credentials_exist(account_name)
def display_contacts():
    '''
    function that returns all the saved contacts
    '''
    return Credentials.display_credentials()
def generate_password():
	'''
	Function to generate a password for a user
	'''
	gen_pass = Credential.generate_password()
	return gen_pass    
def main(): 
    while True:
        print("welcome to password locker")
        print('.\n')
        print("select a short code to navigate through:to create new user 'nu':to log in to your account 'l' or 'e' to exit")
        short_code = input().lower() 
        print('.\n')

        if short_code =='nu':
            print('create username')
            created_user_name = input()

            print('create password')
            created_user_password = input()

            print('confirm password')
            confirm_password = input()
        elif short_code =='l':          
            print("welcome")
            print(" username")
            entered_username= input()
            print("enter your password")
            entered_password=input()


            while confirm_password != created_user_password:
                print("password did not match,")
                print('enter your password')
                created_user_password = input()
                print('confirm your password')
                confirm_password = input()
            else:
                print(f"Congratulations {created_user_name},account sucessfully created")
                print('\n')
                print("You can now log in")
                print("username")
                entered_username= input()
                print("enter your password")
                entered_password=input()
            while entered_username != created_user_name or entered_password != created_user_password:
                print("invalid username or password")
                print("username")
                entered_username=input()
                print("your password")
                entered_password=input()
            else:
                print(f"welcome:{entered_username} to you account,please choose the following short_code to add an accounts and their password")
                print('\n') 
                while True:
					print('Navigation codes: \n ac-add an account \n dc-display credentials \n cp-copy pasword and username \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
                    if short_code == 'ex':
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'ac':
						print('Enter your credential details:')
						site_name = input('Enter the account\'s account-name- ').strip()
						account_name = input('Enter your account\'s user-name - ').strip()
                        print('\n')
						while True:
							print('Please choose an option for entering a password_choice: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							password_choice = input('Enter an option: ').lower().strip()
							print('\n')
							if password_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif password_choice == 'gp':
								password = generate_password()
								break
							elif password_choice == 'ex':
								break
                        else:
                            print("wrong choice please try again")
                            save_credentials(create_credentials(account_name,account_user_name,account_password))
						    print(f'Credentials Created: Account Name: {account_name} -Account User Name: {account_user_name}- Password: {account_password}')    
                    elif short_code =='dc':
                        print(' ')
						if display_credentials(account_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(account_name):
                                print(f' Account Name: {Credentials.account_name} -Account User Name: {Credentials.account_user_name}- Password: {Credentials.account_password}')
							print('/n')	
						else:
							print("There are no credentials,please add")
                            print('/n')
                    elif short_code=="cp":
						account_wanted = input('Please enter the account name: ')
						copy_credentials(account_wanted)
						print('')
					else:
						print(' Try again.')				
                       